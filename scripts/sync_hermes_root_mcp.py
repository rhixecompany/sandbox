#!/usr/bin/env python3
"""Add missing profile MCP definitions to Hermes root config safely.

Only public transport fields are copied. Existing root text is preserved so
provider, model, hook, and credential settings are not reserialized wholesale.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

import yaml


_TOP_LEVEL_KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*:\s*(?:#.*)?$")


def _load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(value, dict) or not isinstance(value.get("mcp_servers"), dict):
        raise ValueError(f"invalid Hermes config: {path}")
    return value


def _safe_url(value: Any) -> str | None:
    if not isinstance(value, str) or not value.startswith(("http://", "https://")):
        return None
    parts = urlsplit(value)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def _public_spec(spec: Any) -> dict[str, Any]:
    if not isinstance(spec, dict):
        raise ValueError("MCP server definition must be an object")
    result: dict[str, Any] = {}
    for key in ("type", "enabled", "command"):
        if key in spec and isinstance(spec[key], (str, bool)):
            result[key] = spec[key]
    url = _safe_url(spec.get("url"))
    if url:
        result["url"] = url
    if spec.get("auth") == "oauth":
        result["auth"] = "oauth"
    if "type" not in result:
        result["type"] = "http" if "url" in result else "stdio"
    return result


def _mcp_block_end(text: str) -> int:
    match = re.search(r"(?m)^mcp_servers:\s*$", text)
    if not match:
        raise ValueError("mcp_servers block not found")
    for line_match in re.finditer(r"(?m)^(\S.*)$", text[match.end() :]):
        candidate = line_match.group(1)
        if _TOP_LEVEL_KEY.match(candidate):
            return match.end() + line_match.start()
    return len(text)


def _render_missing(missing: list[tuple[str, dict[str, Any]]]) -> str:
    chunks: list[str] = []
    for name, spec in missing:
        dumped = yaml.safe_dump(spec, sort_keys=False, default_flow_style=False).rstrip()
        chunks.append(f"  {name}:\n" + "\n".join(f"    {line}" for line in dumped.splitlines()))
    return "\n" + "\n".join(chunks) + "\n"


def reconcile(root_path: Path, profile_path: Path) -> tuple[str, dict[str, Any]]:
    root_text = root_path.read_text(encoding="utf-8")
    root = _load(root_path)
    profile = _load(profile_path)
    root_servers = root["mcp_servers"]
    profile_servers = profile["mcp_servers"]
    missing = [
        (name, _public_spec(profile_servers[name]))
        for name in sorted(set(profile_servers) - set(root_servers))
    ]
    if not missing:
        return root_text, {"missing_before": [], "root_servers_after": len(root_servers), "changed": False}
    end = _mcp_block_end(root_text)
    updated = root_text[:end].rstrip("\n") + _render_missing(missing) + root_text[end:]
    parsed = _load_from_text(updated)
    if not set(profile_servers).issubset(parsed["mcp_servers"]):
        raise ValueError("post-build validation did not include every profile server")
    return updated, {
        "missing_before": [name for name, _ in missing],
        "root_servers_after": len(parsed["mcp_servers"]),
        "changed": updated != root_text,
    }


def _load_from_text(text: str) -> dict[str, Any]:
    value = yaml.safe_load(text) or {}
    if not isinstance(value, dict) or not isinstance(value.get("mcp_servers"), dict):
        raise ValueError("generated root config is invalid")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root-config", required=True)
    parser.add_argument("--profile-config", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root_path = Path(args.root_config).expanduser()
    profile_path = Path(args.profile_config).expanduser()
    try:
        updated, summary = reconcile(root_path, profile_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print("APPLY" if args.apply else "DRY-RUN", "root Hermes MCP reconciliation")
    print(f"root_config={root_path}")
    print(f"profile_config={profile_path}")
    print(yaml.safe_dump(summary, sort_keys=False).rstrip())
    if args.apply and summary["changed"]:
        root_path.write_text(updated, encoding="utf-8")
        print("write=ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
