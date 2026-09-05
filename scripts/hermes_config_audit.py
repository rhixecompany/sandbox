#!/usr/bin/env python3
"""Audit Hermes/repository environment and YAML schemas without secret values.

The command reports paths, metadata, variable names, and YAML key paths only.
It never prints, copies, hashes, or synchronizes environment values.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable

ENV_NAME = re.compile(r"^\.env(?:\..*)?$")
CONFIG_NAMES = {"config.yaml", "config.yml"}
ASSIGNMENT = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$")
YAML_KEY = re.compile(r"^(\s*)([\"']?[A-Za-z0-9_.-]+[\"']?)\s*:")
EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".ruff_cache",
    ".pytest_cache",
    "node_modules",
    ".venv",
    "venv",
    "venv.stale.20260819181026-b42a9fb808bf449287b43e4e795002b1",
    "cache",
    "caches",
    "logs",
    "spillover",
    "checkpoints",
}


def utc_mtime(path: Path) -> str:
    """Return a stable UTC modification timestamp."""
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def is_excluded(path: Path) -> bool:
    """Return whether a path contains an excluded directory component."""
    return any(part in EXCLUDED_DIRS for part in path.parts)


def iter_named_files(root: Path, predicate: Callable[[Path], bool]) -> Iterable[Path]:
    """Yield matching regular files below root without following symlinks."""
    if not root.is_dir():
        return
    for current, dirs, files in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        dirs[:] = sorted(name for name in dirs if name not in EXCLUDED_DIRS)
        for name in sorted(files):
            path = current_path / name
            if path.is_file() and not is_excluded(path) and predicate(path):
                yield path


def classify_env(path: Path) -> str:
    """Classify an environment file without inspecting its values."""
    name = path.name.casefold()
    parts = {part.casefold() for part in path.parts}
    if ".example" in name or name.endswith(".sample") or name.endswith(".template"):
        return "example"
    if any(token in name for token in ("backup", "bak", "old", "snapshot")):
        return "backup-or-snapshot"
    if "profile" in parts or "profiles" in parts:
        return "profile-runtime"
    return "runtime"


def env_record(path: Path, repo: Path, hermes_home: Path) -> dict[str, Any]:
    """Return secret-safe metadata and assignment names for one env file."""
    names: set[str] = set()
    value_assignments = 0
    try:
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            match = ASSIGNMENT.match(line)
            if not match:
                continue
            names.add(match.group(1))
            if match.group(2).strip():
                value_assignments += 1
    except OSError as exc:
        return {"path": str(path), "error": str(exc)[:200]}
    scope = "hermes" if path == hermes_home or hermes_home in path.parents else "repo"
    return {
        "path": str(path),
        "scope": scope,
        "class": classify_env(path),
        "bytes": path.stat().st_size,
        "mtime_utc": utc_mtime(path),
        "variable_names": sorted(names),
        "value_assignment_count": value_assignments,
        "values_emitted": False,
    }


def yaml_key_paths(path: Path) -> list[str]:
    """Extract conservative YAML mapping key paths without reading values."""
    stack: list[tuple[int, str]] = []
    result: set[str] = set()
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return []
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#") or raw.lstrip().startswith("-"):
            continue
        match = YAML_KEY.match(raw)
        if not match:
            continue
        indent, raw_key = match.groups()
        key = raw_key.strip("\"'")
        width = len(indent.expandtabs(2))
        while stack and width <= stack[-1][0]:
            stack.pop()
        stack.append((width, key))
        result.add(".".join(item[1] for item in stack))
    return sorted(result)


def classify_config(path: Path) -> str:
    """Classify a YAML config path by filename and parent names."""
    parts = {part.casefold() for part in path.parts}
    name = path.name.casefold()
    if any(token in name for token in ("backup", "bak", "old", "snapshot")):
        return "backup-or-snapshot"
    if "profiles" in parts or "profile" in parts:
        return "profile"
    if "example" in name or "template" in name:
        return "example"
    return "live-or-project"


def config_record(path: Path, repo: Path, hermes_home: Path) -> dict[str, Any]:
    """Return key paths and metadata for one YAML config, never values."""
    scope = "hermes" if path == hermes_home or hermes_home in path.parents else "repo"
    return {
        "path": str(path),
        "scope": scope,
        "class": classify_config(path),
        "bytes": path.stat().st_size,
        "mtime_utc": utc_mtime(path),
        "key_paths": yaml_key_paths(path),
        "values_emitted": False,
    }


def env_drift(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize environment key-set drift without comparing values."""
    key_sets = {
        record["path"]: set(record.get("variable_names", []))
        for record in records
        if "variable_names" in record
    }
    union = set().union(*key_sets.values()) if key_sets else set()
    return {
        "files_compared": len(key_sets),
        "union_variable_names": sorted(union),
        "per_file_missing_from_union": {
            path: sorted(union - names) for path, names in sorted(key_sets.items())
        },
        "values_compared": False,
    }


def config_drift(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize YAML key-path drift without comparing values."""
    key_sets = {
        record["path"]: set(record.get("key_paths", []))
        for record in records
        if "key_paths" in record
    }
    union = set().union(*key_sets.values()) if key_sets else set()
    return {
        "files_compared": len(key_sets),
        "union_key_paths": sorted(union),
        "per_file_missing_from_union": {
            path: sorted(union - keys) for path, keys in sorted(key_sets.items())
        },
        "values_compared": False,
    }


def inventory(repo: Path, hermes_home: Path) -> dict[str, Any]:
    """Build a complete secret-safe environment/config inventory."""
    env_paths = list(iter_named_files(repo, lambda path: ENV_NAME.match(path.name) is not None))
    env_paths.extend(iter_named_files(hermes_home, lambda path: ENV_NAME.match(path.name) is not None))
    env_records = [env_record(path, repo, hermes_home) for path in sorted(set(env_paths), key=lambda p: str(p).casefold())]
    config_paths = list(iter_named_files(repo, lambda path: path.name.casefold() in CONFIG_NAMES))
    config_paths.extend(iter_named_files(hermes_home, lambda path: path.name.casefold() in CONFIG_NAMES))
    config_records = [config_record(path, repo, hermes_home) for path in sorted(set(config_paths), key=lambda p: str(p).casefold())]
    return {
        "repo": str(repo),
        "hermes_home": str(hermes_home),
        "env_files": env_records,
        "config_files": config_records,
        "env_drift": env_drift(env_records),
        "config_drift": config_drift(config_records),
        "secret_values_emitted": False,
        "secret_values_copied": False,
        "secret_values_hashed": False,
    }


def self_test() -> dict[str, Any]:
    """Run deterministic parser tests in an isolated temporary directory."""
    with tempfile.TemporaryDirectory(prefix="hermes-config-audit-") as temp:
        root = Path(temp)
        (root / ".env.example").write_text("TOKEN=do-not-report\nPORT=\n", encoding="utf-8")
        (root / "config.yaml").write_text("mcp:\n  servers:\n    local: true\n", encoding="utf-8")
        result = inventory(root, root)
        assert result["env_files"][0]["variable_names"] == ["PORT", "TOKEN"]
        assert "mcp" in result["config_files"][0]["key_paths"]
        assert result["secret_values_emitted"] is False
        rendered = json.dumps(result)
        assert "do-not-report" not in rendered
    return {"passed": True, "checks": 4}


def main(argv: list[str] | None = None) -> int:
    """Parse arguments, run the audit, and write JSON evidence."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.home() / "Desktop" / "SandBox")
    parser.add_argument("--hermes-home", type=Path, default=Path.home() / "AppData" / "Local" / "hermes")
    parser.add_argument("--output", type=Path, default=Path(".hermes/reports/env-config-inventory.json"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        print(json.dumps(self_test(), indent=2))
        return 0
    result = inventory(args.repo.resolve(), args.hermes_home.resolve())
    output = args.output if args.output.is_absolute() else args.repo.resolve() / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="")
    print(json.dumps({
        "env_files": len(result["env_files"]),
        "config_files": len(result["config_files"]),
        "output": str(output),
        "secret_values_emitted": False,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
