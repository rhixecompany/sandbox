#!/usr/bin/env python3
"""Inventory sensitive configuration filenames without exposing values."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

_ENV_NAME = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=")
_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}


def _is_env(name: str) -> bool:
    return name == ".env" or name.startswith(".env.")


def _is_config(name: str) -> bool:
    return name.startswith("config.yaml") or name.startswith("config.yml")


def _env_names(path: Path) -> list[str]:
    names: set[str] = set()
    try:
        with path.open(encoding="utf-8", errors="ignore") as stream:
            for line in stream:
                match = _ENV_NAME.match(line)
                if match:
                    names.add(match.group(1))
    except OSError:
        return []
    return sorted(names)


def inventory(root: Path, scope: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for current, dirs, files in os.walk(root, topdown=True, followlinks=False):
        dirs[:] = sorted(name for name in dirs if name not in _SKIP_DIRS)
        for filename in sorted(files):
            if not (_is_env(filename) or _is_config(filename)):
                continue
            path = Path(current) / filename
            kind = "env" if _is_env(filename) else "config"
            record: dict[str, Any] = {
                "scope": scope,
                "path": str(path),
                "kind": kind,
                "file_class": filename,
            }
            if kind == "env":
                record["variable_names"] = _env_names(path)
            records.append(record)
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--hermes-home", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    repo = Path(args.repo).expanduser().resolve()
    hermes = Path(args.hermes_home).expanduser().resolve()
    records = inventory(repo, "repository") + inventory(hermes, "hermes")
    payload = {
        "secret_values_emitted": False,
        "scopes": {
            "repository": sum(record["scope"] == "repository" for record in records),
            "hermes": sum(record["scope"] == "hermes" for record in records),
        },
        "counts": {
            "env": sum(record["kind"] == "env" for record in records),
            "config": sum(record["kind"] == "config" for record in records),
        },
        "records": records,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"counts": payload["counts"], "scopes": payload["scopes"], "output": str(output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
