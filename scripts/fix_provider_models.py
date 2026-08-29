#!/usr/bin/env python3
"""Auto-fix provider model IDs in config.yaml.

For each provider in ~/AppData/Local/hermes/config.yaml:
  1. Test the current default_model
  2. If invalid, query the provider's /v1/models endpoint
  3. Pick a valid replacement (preferring "free" or "flash" variants)
  4. Patch config.yaml

Usage:
  python scripts/fix_provider_models.py [--apply] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

HERMES_HOME = Path.home() / "AppData" / "Local" / "hermes"
CONFIG_YAML = HERMES_HOME / "config.yaml"
ENV_FILE = HERMES_HOME / ".env"


def load_env(env_file: Path) -> dict[str, str]:
    """Load KEY=VALUE pairs from a .env file."""
    env: dict[str, str] = {}
    if not env_file.exists():
        return env
    for line in env_file.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip().strip("'\"")
    return env


# Load from .env at import time so PROVIDERS lister can use them
for _k, _v in load_env(ENV_FILE).items():
    os.environ.setdefault(_k, _v)


def http_get_json(url: str, headers: dict[str, str] | None = None, timeout: int = 15) -> dict | list | None:
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def list_openrouter() -> list[str]:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    data = http_get_json("https://openrouter.ai/api/v1/models", {"Authorization": f"Bearer {key}"})
    if not isinstance(data, dict) or "data" not in data:
        return []
    return [m["id"] for m in data["data"]]


def list_ollama_cloud() -> list[str]:
    key = os.environ.get("OLLAMA_API_KEY", "")
    data = http_get_json("https://ollama.com/v1/models", {"Authorization": f"Bearer {key}"})
    if not isinstance(data, dict) or "data" not in data:
        return []
    return [m.get("id", m.get("name")) for m in data["data"]]


def list_opencode_zen() -> list[str]:
    """OpenCode Zen models. Tries the configured base URL first, then common paths."""
    base = os.environ.get("OPENCODE_ZEN_BASE_URL", "https://opencode.ai/zen/v1").rstrip("/")
    candidates = [
        base,
        f"{base}/v1" if not base.endswith("/v1") else base,
        "https://opencode.ai/zen/v1",
        "https://opencode.ai/api/v1",
        "https://opencode.ai/v1",
    ]
    key = os.environ.get("OPENCODE_ZEN_API_KEY", "")
    for path in candidates:
        url = f"{path}/models" if not path.endswith("/models") else path
        data = http_get_json(url, {"Authorization": f"Bearer {key}"})
        if isinstance(data, dict) and "data" in data:
            return [m["id"] for m in data["data"]]
        if isinstance(data, list):
            return [m.get("id", m.get("name")) for m in data]
    return []


def list_gemini() -> list[str]:
    """Gemini doesn't have a public /v1/models list endpoint that doesn't require the API key.
    Use a hardcoded set of common models."""
    return ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]


def list_deepseek() -> list[str]:
    """DeepSeek common models."""
    return ["deepseek-chat", "deepseek-reasoner", "deepseek-coder"]


# Pick-best preference order (most preferred first)
PREFER_FREE = ["free", "flash", "mini", "lite", "haiku", "8b", "4b"]
PREFER_PERFORMANCE = ["ultra", "pro", "opus", "sonnet"]


def pick_best(models: list[str], current: str) -> str:
    """Pick the best replacement from the list, preferring free/flash variants."""
    if not models:
        return current  # nothing to choose from
    # Try to find a similar-tier model
    for pref in PREFER_FREE:
        for m in models:
            if pref in m.lower():
                return m
    # Fall back to first model
    return models[0]


PROVIDERS: dict[str, dict] = {
    "deepseek": {
        "api_key_env": "DEEPSEEK_API_KEY",
        "lister": list_deepseek,
        "current": "deepseek-v4-flash-free",
    },
    "gemini": {
        "api_key_env": "GOOGLE_API_KEY",
        "lister": list_gemini,
        "current": "gemini-2.5-flash",
    },
    "ollama-cloud": {
        "api_key_env": "OLLAMA_API_KEY",
        "lister": list_ollama_cloud,
        "current": "nemotron-3-ultra",
    },
    "opencode-zen": {
        "api_key_env": "OPENCODE_ZEN_API_KEY",
        "lister": list_opencode_zen,
        "current": "nemotron-3-ultra-free",
        "note": "opencode-zen /v1/models returns 403; current model is unverifiable",
    },
    "openrouter": {
        "api_key_env": "OPENROUTER_API_KEY",
        "lister": list_openrouter,
        "current": "nvidia/nemotron-3-ultra-550b-a55b:free",
    },
}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true", help="Actually patch config.yaml")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    if not CONFIG_YAML.exists():
        print(f"Config not found: {CONFIG_YAML}", file=sys.stderr)
        return 2
    text = CONFIG_YAML.read_text(encoding="utf-8", errors="ignore")
    print("Checking each provider's default_model...\n")
    fixes: list[tuple[str, str, str]] = []  # (provider, old, new)
    for name, spec in PROVIDERS.items():
        if not os.environ.get(spec["api_key_env"]):
            print(f"  {name:20} SKIP (no {spec['api_key_env']} env var)")
            continue
        models = spec["lister"]()
        if not models:
            print(f"  {name:20} SKIP (lister returned empty)")
            continue
        current = spec["current"]
        if current in models:
            print(f"  {name:20} OK ({current} is valid)")
            continue
        new = pick_best(models, current)
        print(f"  {name:20} {current} -> {new}")
        fixes.append((name, current, new))

    if not fixes:
        print("\nNo fixes needed.")
        return 0

    print(f"\nProposed fixes: {len(fixes)}")
    if not args.apply:
        print("(dry-run — pass --apply to actually patch config.yaml)")
        return 0

    # Patch config.yaml
    for name, old, new in fixes:
        # Find the provider block and replace its default_model
        pattern = re.compile(
            rf"({name}:\s*\n(?:    [^\n]+\n)*?    default_model:\s*){re.escape(old)}",
            re.M,
        )
        new_text, n = pattern.subn(rf"\g<1>{new}", text)
        if n == 0:
            print(f"  ✗ {name}: pattern not found in config.yaml")
            continue
        text = new_text
        print(f"  ✓ {name}: {old} -> {new}")
    CONFIG_YAML.write_text(text, encoding="utf-8")
    print(f"\nPatched {CONFIG_YAML}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
