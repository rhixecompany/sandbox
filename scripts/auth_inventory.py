#!/usr/bin/env python3
"""
auth_inventory.py — Build provider inventory from `hermes auth list`.

Parses the text output of `hermes auth list` into a structured JSON
inventory of all authorized providers, their credentials, and static
capability defaults.

Output: scripts/.runtime/provider_inventory.json

Usage:
    python scripts/auth_inventory.py
    python scripts/auth_inventory.py --output /tmp/inventory.json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


# Per-provider static capability defaults. Used as fallback when the
# provider's own /models endpoint is unreachable. Keys map 1:1 to the
# provider name in `hermes auth list`.
PROVIDER_CAPABILITIES: dict[str, dict] = {
    "openrouter": {
        "vision": True,        # depends on model; many support
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 32768,
        "max_output_default": 4096,
        "api_style": "openai_compat",
        "base_url": "https://openrouter.ai/api/v1",
        "default_model": "openrouter/auto",
    },
    "openai-codex": {
        "vision": True,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 200000,
        "max_output_default": 16384,
        "api_style": "openai_compat",
        "base_url": "https://api.openai.com/v1",
        "auth": "oauth",
        "default_model": "gpt-4o",
    },
    "deepseek": {
        "vision": False,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 64000,
        "max_output_default": 8192,
        "api_style": "openai_compat",
        "base_url": "https://api.deepseek.com/v1",
        "default_model": "deepseek-chat",
    },
    "gemini": {
        "vision": True,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 1000000,
        "max_output_default": 8192,
        "api_style": "openai_compat",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
        "default_model": "gemini-2.0-flash",
    },
    "xai": {
        "vision": False,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 131072,
        "max_output_default": 8192,
        "api_style": "openai_compat",
        "base_url": "https://api.x.ai/v1",
        "default_model": "grok-2",
    },
    "xai-oauth": {
        "vision": False,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 131072,
        "max_output_default": 8192,
        "api_style": "openai_compat",
        "base_url": "https://api.x.ai/v1",
        "auth": "oauth",
        "default_model": "grok-2",
    },
    "nous": {
        "vision": False,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 32768,
        "max_output_default": 4096,
        "api_style": "openai_compat",
        "base_url": "https://inference-api.nousresearch.com/v1",
        "auth": "oauth",
        "default_model": "solar-pro4",
    },
    "opencode-zen": {
        "vision": False,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 32768,
        "max_output_default": 4096,
        "api_style": "openai_compat",
        "base_url": "https://opencode.ai/zen/v1",
        "default_model": "big-pickle",
    },
    "ollama-cloud": {
        "vision": False,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 32768,
        "max_output_default": 4096,
        "api_style": "openai_compat",
        "base_url": "https://api.ollama.com/v1",
        "default_model": "llama3.3",
    },
    "huggingface": {
        "vision": False,
        "tools": False,
        "json_mode": False,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 8192,
        "max_output_default": 1024,
        "api_style": "openai_compat",
        "base_url": "https://api-inference.huggingface.co/v1",
        "default_model": "meta-llama/Meta-Llama-3-8B-Instruct",
    },
    "copilot": {
        "vision": True,
        "tools": True,
        "json_mode": True,
        "streaming": True,
        "system_prompt": True,
        "context_window_default": 128000,
        "max_output_default": 8192,
        "api_style": "github_copilot",
        "default_model": "gpt-4o",
    },
}


def parse_hermes_auth_list(text: str) -> list[dict]:
    """
    Parse text output of `hermes auth list`.

    Format (verified 2026-08-28, hermes v0.20.6):
        <provider> (<n> credentials):
          #<i>  <label>             api_key|oauth   env:<env_var>|manual|device_code [<- active] [auth failed ...]
    """
    providers: list[dict] = []
    current: dict | None = None
    cred_re = re.compile(
        r"^\s*#(\d+)\s+(\S+)\s+(api_key|oauth)\s+(\S+)(?:\s+auth\s+failed.*?)?(?:\s+←)?\s*$"
    )
    header_re = re.compile(r"^(\S+)\s+\((\d+)\s+credentials?\):\s*$")
    for raw in text.splitlines():
        line = raw.rstrip()
        m = header_re.match(line)
        if m:
            if current is not None:
                providers.append(current)
            current = {
                "name": m.group(1),
                "credential_count": int(m.group(2)),
                "credentials": [],
            }
            continue
        m = cred_re.match(line)
        if m and current is not None:
            idx, label, auth_type, source = m.groups()
            is_active = "←" in line
            current["credentials"].append({
                "index": int(idx),
                "label": label,
                "auth_type": auth_type,
                "source": source,
                "is_active": is_active,
            })
        # blank lines and unrecognized lines are skipped
    if current is not None:
        providers.append(current)
    return providers


def build_inventory(parsed: list[dict]) -> dict:
    out_providers: list[dict] = []
    for p in parsed:
        name = p["name"]
        caps = PROVIDER_CAPABILITIES.get(name, {})
        # Choose the active credential as primary (or first)
        active = next((c for c in p["credentials"] if c["is_active"]),
                      p["credentials"][0] if p["credentials"] else None)
        primary = None
        if active:
            primary = {
                "label": active["label"],
                "auth_type": active["auth_type"],
                "source": active["source"],
            }
        out_providers.append({
            "name": name,
            "credential_count": p["credential_count"],
            "primary": primary,
            "credentials": p["credentials"],
            "capabilities_static": caps,
        })
    return {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "source": "hermes auth list",
        "hermes_version": _safe_hermes_version(),
        "provider_count": len(out_providers),
        "providers": out_providers,
    }


def _safe_hermes_version() -> str:
    try:
        return subprocess.check_output(
            ["hermes", "--version"], text=True, timeout=10
        ).strip().splitlines()[0]
    except Exception:
        return "unknown"


def main() -> int:
    p = argparse.ArgumentParser(description="Build provider inventory from `hermes auth list`")
    p.add_argument("--output", default="scripts/.runtime/provider_inventory.json")
    p.add_argument("--hermes-bin", default="hermes")
    args = p.parse_args()

    try:
        text = subprocess.check_output(
            [args.hermes_bin, "auth", "list"], text=True, timeout=30
        )
    except FileNotFoundError:
        print(f"ERROR: `{args.hermes_bin}` not on PATH", file=sys.stderr)
        return 2
    except subprocess.CalledProcessError as e:
        print(f"ERROR: `hermes auth list` failed: {e}", file=sys.stderr)
        return 2

    parsed = parse_hermes_auth_list(text)
    if not parsed:
        print("ERROR: parsed 0 providers from `hermes auth list`", file=sys.stderr)
        print("--- raw output ---", file=sys.stderr)
        print(text, file=sys.stderr)
        return 1

    inventory = build_inventory(parsed)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(inventory, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✓ Wrote {out}")
    print(f"  providers: {inventory['provider_count']}")
    for p in inventory["providers"]:
        active = next((c for c in p["credentials"] if c["is_active"]), None)
        label = active["label"] if active else "(none)"
        print(f"  - {p['name']:18s} creds={p['credential_count']} active={label}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
