#!/usr/bin/env python3
"""Reconcile the public MCP registry with one Hermes profile.

The registry is a client projection, not a credential store.  This utility only
copies server names and non-secret transport metadata.  It retains registry-only
entries as disabled records so an explicit later opt-in remains possible.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment failure
    raise SystemExit("PyYAML is required to reconcile MCP registry metadata") from exc


_SECRET_KEY_RE = re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|auth|password|secret|bearer)")
_SECRET_VALUE_RE = re.compile(
    r"(?i)^(?:sk[-_]|pk[-_]|rk[-_]|ghp_|github_pat_|xox[bap]-|AIza|Bearer\s)"
)


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("servers"), dict):
        raise ValueError(f"invalid MCP registry shape: {path}")
    return value


def _load_hermes(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(value, dict) or not isinstance(value.get("mcp_servers"), dict):
        raise ValueError(f"invalid Hermes MCP config shape: {path}")
    return value


def _safe_url(value: Any) -> str | None:
    if not isinstance(value, str) or not value.startswith(("http://", "https://")):
        return None
    parts = urlsplit(value)
    # Query strings are the most common place for accidental credential leakage.
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def _safe_args(value: Any) -> list[str] | None:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        return None
    args: list[str] = []
    skip_next = False
    for index, item in enumerate(value):
        if skip_next:
            skip_next = False
            continue
        if _SECRET_KEY_RE.search(item) and not item.startswith("${env:"):
            if "=" in item:
                continue
            skip_next = index + 1 < len(value)
            continue
        if _SECRET_VALUE_RE.search(item) or (len(item) > 48 and "${" not in item):
            continue
        args.append(item)
    return args


def _public_transport(spec: Mapping[str, Any]) -> dict[str, Any]:
    public: dict[str, Any] = {}
    server_type = spec.get("type")
    if isinstance(server_type, str):
        public["type"] = server_type
    command = spec.get("command")
    if isinstance(command, str) and command:
        public["command"] = command
    args = _safe_args(spec.get("args"))
    if args is not None:
        public["args"] = args
    url = _safe_url(spec.get("url"))
    if url:
        public["url"] = url
    if "type" not in public:
        public["type"] = "http" if "url" in public else "stdio"
    if spec.get("auth") is not None:
        public["auth_mode"] = "configured"
    return public


def _reconciled(registry: dict[str, Any], hermes: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    existing = registry["servers"]
    hermes_servers = hermes["mcp_servers"]
    enabled = {
        name for name, spec in hermes_servers.items()
        if isinstance(spec, Mapping) and spec.get("enabled", True)
    }
    result = dict(registry)
    result_servers: dict[str, Any] = {}
    added: list[str] = []
    enabled_existing: list[str] = []
    disabled: list[str] = []

    for name, raw in existing.items():
        if not isinstance(raw, dict):
            raise ValueError(f"registry server {name!r} is not an object")
        record = dict(raw)
        if name in enabled:
            record["enabled"] = True
            record.pop("disabled_reason", None)
            enabled_existing.append(name)
        else:
            record["enabled"] = False
            record["disabled_reason"] = "not enabled in the selected Hermes profile"
            disabled.append(name)
        result_servers[name] = record

    for name in sorted(enabled - set(existing)):
        spec = hermes_servers[name]
        if not isinstance(spec, Mapping):
            continue
        record = _public_transport(spec)
        record["enabled"] = True
        record["description"] = "Imported from the selected Hermes profile; review before enabling in clients."
        record["tags"] = ["hermes-profile"]
        result_servers[name] = record
        added.append(name)

    result["servers"] = result_servers
    summary = {
        "hermes_enabled": len(enabled),
        "registry_enabled_before": sum(
            isinstance(value, dict) and value.get("enabled", True)
            for value in existing.values()
        ),
        "registry_enabled_after": sum(
            isinstance(value, dict) and value.get("enabled", True)
            for value in result_servers.values()
        ),
        "enabled_existing": sorted(enabled_existing),
        "added": added,
        "disabled": sorted(disabled),
    }
    return result, summary


def _write_registry(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent="\t", ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default=".mcp/registry.json")
    parser.add_argument("--hermes-config", required=True)
    parser.add_argument("--apply", action="store_true", help="write the reconciled registry")
    args = parser.parse_args()

    registry_path = Path(args.registry).expanduser()
    hermes_path = Path(args.hermes_config).expanduser()
    try:
        registry = _load_json(registry_path)
        hermes = _load_hermes(hermes_path)
        reconciled, summary = _reconciled(registry, hermes)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    changed = reconciled != registry
    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"{mode} registry reconciliation")
    print(f"registry={registry_path}")
    print(f"hermes_config={hermes_path}")
    print(f"changed={changed}")
    print(json.dumps(summary, indent=2, sort_keys=True))
    if args.apply and changed:
        _write_registry(registry_path, reconciled)
        print("write=ok")
    elif args.apply:
        print("write=skipped (already reconciled)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
