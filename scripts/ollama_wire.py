#!/usr/bin/env python3
"""Ollama wiring: ensure the configured local ollama model is set in:
  - ~/AppData/Local/hermes/config.yaml (providers.ollama-launch.*)
  - opencode.json (oh-my-opencode)
  - .codex/mcp.json
  - .copilot/mcp.json

Reads the requested model from --model (default qwen3-vl:2b). Falls back to
existing gemma4:12b if qwen3-vl:2b is not on disk.

Usage:
  python scripts/ollama_wire.py [--model qwen3-vl:2b] [--ollama-url http://127.0.0.1:11434/v1]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERMES_HOME = Path.home() / "AppData" / "Local" / "hermes"
SANDBOX = Path("C:/Users/Alexa/Desktop/SandBox")
CONFIG_YAML = HERMES_HOME / "config.yaml"
OPENCODE_JSON = HERMES_HOME.parent.parent / ".config" / "opencode" / "opencode.json"
OLLAMA_MODELS_DIR = Path.home() / ".ollama" / "models" / "manifests" / "registry.ollama.ai" / "library"


def get_local_models() -> list[str]:
    """Get list of ollama models on disk (parse manifest dirs)."""
    if not OLLAMA_MODELS_DIR.exists():
        return []
    out: list[str] = []
    for vendor in OLLAMA_MODELS_DIR.iterdir():
        if not vendor.is_dir():
            continue
        for tag in vendor.iterdir():
            if tag.is_file():
                out.append(f"{vendor.name}:{tag.name}")
    return out


def patch_config_yaml(model: str, ollama_url: str) -> bool:
    """Update providers.ollama-launch.* in config.yaml.

    Uses targeted string replacement — does not parse/re-serialize the whole YAML.
    """
    if not CONFIG_YAML.exists():
        print(f"  ✗ config.yaml not found: {CONFIG_YAML}")
        return False
    text = CONFIG_YAML.read_text(encoding="utf-8", errors="ignore")
    orig = text
    # Replace default_model under ollama-launch
    import re
    # Find the ollama-launch block and replace its default_model
    pattern = re.compile(
        r"(ollama-launch:\s*\n\s+api:\s+[^\n]+\n\s+default_model:\s+)([^\n]+)",
        re.M,
    )
    new_text, n = pattern.subn(rf"\g<1>{model}", text)
    if n == 0:
        # Section doesn't exist — insert after providers: header
        if "providers:" in new_text:
            insert = f"  ollama-launch:\n    api: {ollama_url}\n    default_model: {model}\n    name: Ollama Local\n"
            new_text = new_text.replace("providers:\n", f"providers:\n{insert}", 1)
        else:
            print("  ✗ No providers: section in config.yaml")
            return False
    if new_text == orig:
        print(f"  ✓ config.yaml already has ollama-launch.default_model={model}")
    else:
        CONFIG_YAML.write_text(new_text, encoding="utf-8")
        print(f"  ✓ config.yaml: ollama-launch.default_model={model}")
    return True


def patch_json(path: Path, key_path: list[str], value) -> bool:
    """Update a value in a JSON file at the given key path. Creates file if missing."""
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        data: dict = {}
    else:
        try:
            data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
        except json.JSONDecodeError:
            data = {}
    cur = data
    for k in key_path[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    cur[key_path[-1]] = value
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"  ✓ {path}: {key_path} = {value}")
    return True


def find_opencode_json() -> Path | None:
    """Find oh-my-opencode config file."""
    candidates = [
        Path.home() / ".config" / "opencode" / "opencode.json",
        HERMES_HOME / "opencode.json",
        SANDBOX / ".opencode" / "opencode.json",
        Path.home() / ".opencode" / "opencode.json",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="qwen3-vl:2b")
    p.add_argument("--ollama-url", default="http://127.0.0.1:11434/v1")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    local = get_local_models()
    print(f"Local ollama models on disk: {local}")
    if args.model not in local:
        # Try fallback
        if "gemma4:12b" in local:
            print(f"⚠ Requested {args.model} not on disk, using gemma4:12b")
            args.model = "gemma4:12b"
        else:
            print(f"✗ {args.model} not on disk; run: ollama pull {args.model}")
            return 1

    print(f"\nWiring model={args.model} url={args.ollama_url}")
    if args.dry_run:
        print("(dry-run)")

    if not args.dry_run:
        patch_config_yaml(args.model, args.ollama_url)

        # opencode.json (oh-my-opencode)
        oc = find_opencode_json()
        if oc:
            patch_json(oc, ["model", "ollama-local", "baseURL"], args.ollama_url)
            patch_json(oc, ["model", "ollama-local", "model"], args.model)
        else:
            print("  ⚠ opencode.json not found in expected locations")

        # .codex/mcp.json
        codex_mcp = SANDBOX / ".codex" / "mcp.json"
        if codex_mcp.exists():
            patch_json(codex_mcp, ["mcpServers", "ollama-local", "env", "OLLAMA_MODEL"], args.model)

        # .copilot/mcp.json
        copilot_mcp = SANDBOX / ".copilot" / "mcp.json"
        if copilot_mcp.exists():
            patch_json(copilot_mcp, ["mcpServers", "ollama-local", "env", "OLLAMA_MODEL"], args.model)

    print("\nDone. Verify with:")
    print(f"  ollama list | grep {args.model}")
    print(f"  hermes chat -m {args.model} --provider ollama-launch -q 'Reply OK' --oneshot")
    return 0


if __name__ == "__main__":
    sys.exit(main())
