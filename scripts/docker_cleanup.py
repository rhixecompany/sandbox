#!/usr/bin/env python3
"""Docker cleanup helper (default mode is read-only inventory).

Apply mode requires an explicit allowlist file (one resource reference per
line) and an ``--apply`` flag. The helper never deletes resources whose
name contains ``mcp`` or ``model`` without an extra ``--include-toolkit``
flag, because those resources may be load-bearing for Hermes/MCP servers.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def _run(cmd: list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout


def inventory() -> dict[str, Any]:
    df = _run(["docker", "system", "df", "--format", "{{.Type}}\t{{.TotalCount}}\t{{.Size}}\t{{.Reclaimable}}"])
    images = _run(["docker", "image", "ls", "-a", "--format", "{{.Repository}}:{{.Tag}}\t{{.Size}}\t{{.ID}}"])
    containers = _run(["docker", "ps", "-a", "--format", "{{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}"])
    volumes = _run(["docker", "volume", "ls", "--format", "{{.Name}}\t{{.Driver}}"])
    networks = _run(["docker", "network", "ls", "--format", "{{.Name}}\t{{.Driver}}"])
    return {
        "df": [line.split("\t") for line in df.splitlines() if line],
        "images": [line.split("\t") for line in images.splitlines() if line],
        "containers": [line.split("\t") for line in containers.splitlines() if line],
        "volumes": [line.split("\t") for line in volumes.splitlines() if line],
        "networks": [line.split("\t") for line in networks.splitlines() if line],
    }


def classify(images: list[list[str]], containers: list[list[str]], volumes: list[list[str]]) -> dict[str, Any]:
    toolkit_keywords = ("mcp", "model", "toolkit", "ollama")
    tool_resources: list[list[str]] = []
    unused_resources: list[list[str]] = []
    for row in images:
        ref = row[0].lower() if row else ""
        if any(keyword in ref for keyword in toolkit_keywords):
            tool_resources.append(row)
        else:
            unused_resources.append(row)
    return {
        "tool_resources": tool_resources,
        "unused_candidates": unused_resources,
        "preserved_volumes": volumes,
        "preserved_containers": containers,
    }


def apply_allowlist(path: Path, include_toolkit: bool) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"allowlist not found: {path}")
    deletions: list[dict[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        item = line.strip()
        if not item or item.startswith("#"):
            continue
        kind, _, target = item.partition("=")
        kind = kind.strip().lower()
        target = target.strip()
        if any(keyword in target.lower() for keyword in ("mcp", "model", "toolkit")) and not include_toolkit:
            deletions.append({"skipped": item, "reason": "toolkit resource; pass --include-toolkit to delete"})
            continue
        if kind == "image":
            subprocess.run(["docker", "image", "rm", target], check=False)
        elif kind == "container":
            subprocess.run(["docker", "container", "rm", target], check=False)
        elif kind == "volume":
            subprocess.run(["docker", "volume", "rm", target], check=False)
        elif kind == "prune-buildx":
            subprocess.run(["docker", "buildx", "prune", "-af"], check=False)
        else:
            deletions.append({"skipped": item, "reason": "unknown kind"})
            continue
        deletions.append({"deleted": item})
    return {"deletions": deletions}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("inventory")
    sub.add_parser("classify")
    apply_cmd = sub.add_parser("apply")
    apply_cmd.add_argument("--allowlist", type=Path, required=True)
    apply_cmd.add_argument("--include-toolkit", action="store_true")
    args = ap.parse_args(argv)

    if args.command == "inventory":
        print(json.dumps(inventory(), indent=2))
        return 0
    if args.command == "classify":
        data = inventory()
        print(
            json.dumps(
                classify(data["images"], data["containers"], data["volumes"]),
                indent=2,
            )
        )
        return 0
    if args.command == "apply":
        print(json.dumps(apply_allowlist(args.allowlist, args.include_toolkit), indent=2))
        return 0
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    sys.exit(main())
