#!/usr/bin/env python3
"""
mcp_sync.py — Propagate .mcp/registry.json to disk configs.

Targets (always overwritten from registry):
  1. opencode.json                 — preserves non-mcp keys (model, plugin, small_model)
  2. .codex/mcp.json               — mcpServers
  3. .copilot/mcp.json             — mcpServers (pretty-printed, indented)
  4. .vscode/mcp.json              — servers + inputs

Hermes config.yaml (~/AppData/Local/hermes/config.yaml) is NOT auto-edited
because hermes has its own mcp_servers schema and `hermes mcp add/remove` flow.
Use the optional --hermes flag to print the diff instead.

Usage:
    python scripts/mcp_sync.py --registry .mcp/registry.json           # apply
    python scripts/mcp_sync.py --registry .mcp/registry.json --dry-run  # report only
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def to_stdio_entry(srv: dict[str, Any]) -> dict[str, Any]:
    """Convert a registry entry to codex/copilot/vscode stdio format."""
    out: dict[str, Any] = {"type": srv.get("type", "stdio")}
    if "command" in srv:
        out["command"] = srv["command"]
    if "args" in srv:
        out["args"] = srv["args"]
    if "env" in srv:
        out["env"] = srv["env"]
    return out


def to_http_entry(srv: dict[str, Any]) -> dict[str, Any]:
    """Convert to http/sse format."""
    return {"type": srv.get("type", "http"), "url": srv["url"]}


def build_mcp_servers(servers: dict[str, Any]) -> dict[str, Any]:
    """Build the mcpServers map (codex/copilot/vscode)."""
    out: dict[str, Any] = {}
    for name, srv in servers.items():
        if not srv.get("enabled", True):
            continue
        if srv.get("type") in ("http", "sse"):
            out[name] = to_http_entry(srv)
        else:
            out[name] = to_stdio_entry(srv)
    return out


def build_opencode_mcp(servers: dict[str, Any]) -> dict[str, Any]:
    """Build opencode.json mcp section (command is a list)."""
    out: dict[str, Any] = {}
    for name, srv in servers.items():
        entry: dict[str, Any] = {
            "enabled": srv.get("enabled", True),
            "type": "remote" if srv.get("type") in ("http", "sse") else "local",
        }
        if srv.get("type") in ("http", "sse"):
            entry["url"] = srv["url"]
        else:
            # opencode uses "command" as a list, not string
            cmd = srv.get("command", "")
            args = srv.get("args", [])
            if isinstance(cmd, str):
                entry["command"] = [cmd, *args]
            else:
                entry["command"] = cmd
        if "env" in srv:
            entry["env"] = srv["env"]
        out[name] = entry
    return out


def write_json(path: Path, data: Any, indent: int | str = 2) -> tuple[bool, str]:
    """Write JSON file. Returns (changed, message)."""
    new_text = json.dumps(data, indent=indent, ensure_ascii=False) + "\n"
    if path.exists():
        try:
            old = json.loads(path.read_text(encoding="utf-8-sig"))
            if json.dumps(old, indent=indent, ensure_ascii=False, sort_keys=True) == json.dumps(
                json.loads(new_text), indent=indent, ensure_ascii=False, sort_keys=True
            ):
                return False, "no change"
        except (json.JSONDecodeError, OSError):
            pass
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(new_text, encoding="utf-8")
    return True, "written"


def sync_one(name: str, target_path: Path, new_data: Any, indent: int | str, dry: bool) -> dict[str, Any]:
    if dry:
        try:
            old = json.loads(target_path.read_text(encoding="utf-8-sig"))
            same = json.dumps(old, indent=indent, sort_keys=True) == json.dumps(new_data, indent=indent, sort_keys=True)
        except (FileNotFoundError, json.JSONDecodeError):
            same = False
        return {"target": name, "path": str(target_path), "changed": not same, "action": "would write" if not same else "no change"}
    changed, msg = write_json(target_path, new_data, indent=indent)
    return {"target": name, "path": str(target_path), "changed": changed, "action": msg}


def sync(root: Path, registry: dict[str, Any], dry: bool) -> list[dict[str, Any]]:
    servers = registry.get("servers", {})
    results: list[dict[str, Any]] = []

    # 1) opencode.json — preserve non-mcp keys
    opencode_path = root / "opencode.json"
    if opencode_path.exists():
        try:
            oc = json.loads(opencode_path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError:
            oc = {}
        oc["mcp"] = build_opencode_mcp(servers)
        results.append(sync_one("opencode.json", opencode_path, oc, indent=2, dry=dry))
    else:
        results.append({"target": "opencode.json", "path": str(opencode_path), "changed": False, "action": "missing"})

    # 2) .codex/mcp.json
    codex_path = root / ".codex" / "mcp.json"
    codex_data = {"mcpServers": build_mcp_servers(servers)}
    results.append(sync_one(".codex/mcp.json", codex_path, codex_data, indent="\t", dry=dry))

    # 3) .copilot/mcp.json (pretty-printed, same content as codex)
    copilot_path = root / ".copilot" / "mcp.json"
    results.append(sync_one(".copilot/mcp.json", copilot_path, codex_data, indent=4, dry=dry))

    # 4) .vscode/mcp.json — needs `inputs` section too
    vscode_path = root / ".vscode" / "mcp.json"
    if vscode_path.exists():
        try:
            vs = json.loads(vscode_path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError:
            vs = {}
    else:
        vs = {}
    if "inputs" not in vs:
        vs["inputs"] = [
            {
                "id": "workspaceFolder",
                "type": "promptString",
                "description": "Workspace root path",
                "default": "${workspaceFolder}",
            }
        ]
    vs["servers"] = build_mcp_servers(servers)
    results.append(sync_one(".vscode/mcp.json", vscode_path, vs, indent="\t", dry=dry))

    return results


def hermes_diff(registry: dict[str, Any], hermes_cfg: Path) -> str:
    """Print a diff of what would need to change in hermes config.yaml."""
    import re

    if not hermes_cfg.exists():
        return "ERROR: hermes config not found"
    text = hermes_cfg.read_text(encoding="utf-8")

    # Extract mcp_servers block
    m = re.search(r"^mcp_servers:\s*\n((?:^  \w.*\n|^    .*\n)*)", text, re.MULTILINE)
    if not m:
        return "WARN: mcp_servers block not found in hermes config.yaml"

    lines = ["# Hermes mcp_servers diff (manual — use `hermes mcp add/remove` to apply):", ""]
    in_block = m.group(0).splitlines()
    current_servers: set[str] = set()
    for ln in in_block:
        mm = re.match(r"^  (\w[\w-]*):\s*$", ln)
        if mm:
            current_servers.add(mm.group(1))

    wanted = {n for n, s in registry.get("servers", {}).items() if s.get("enabled", True)}
    only_in_hermes = current_servers - wanted
    only_in_registry = wanted - current_servers
    if only_in_hermes:
        lines.append(f"# In hermes but NOT in registry: {sorted(only_in_hermes)}")
    if only_in_registry:
        lines.append(f"# In registry but NOT in hermes: {sorted(only_in_registry)}")
    if not only_in_hermes and not only_in_registry:
        lines.append("# hermes mcp_servers matches registry (enabled set)")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Sync MCP registry to disk configs")
    p.add_argument("--registry", default=".mcp/registry.json")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--hermes-diff", action="store_true", help="Print hermes config diff")
    p.add_argument("--hermes-cfg", default=r"C:\Users\Alexa\AppData\Local\hermes\config.yaml")
    args = p.parse_args()

    registry_path = Path(args.registry)
    if not registry_path.exists():
        print(f"ERROR: registry not found: {registry_path}", file=sys.stderr)
        return 2

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    root = registry_path.resolve().parent  # .mcp dir
    workspace_root = root.parent

    results = sync(workspace_root, registry, dry=args.dry_run)
    print(f"\n{'DRY-RUN' if args.dry_run else 'APPLIED'} sync results:")
    for r in results:
        flag = "✓" if r["changed"] else "·"
        print(f"  {flag} {r['target']:25s} {r['action']:20s} ({r['path']})")

    if args.hermes_diff:
        print()
        print(hermes_diff(registry, Path(args.hermes_cfg)))

    # Exit non-zero if any file was changed and not in dry-run (caller can ignore)
    return 0


if __name__ == "__main__":
    sys.exit(main())
