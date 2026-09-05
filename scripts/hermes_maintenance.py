#!/usr/bin/env python3
"""Comprehensive Hermes maintenance orchestrator (safe, additive).

Default mode is read-only: inventory, dedupe report, and Docker dry-run.
Apply modes (config-sync, scripts-judge update, dedupe, Docker cleanup) are
gated by an explicit ``--apply`` flag and an approved manifest path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


def hermes_home() -> Path:
    return Path(os.environ.get("HERMES_HOME", Path.home() / "AppData" / "Local" / "hermes")).expanduser()


def repo_root() -> Path:
    return Path(os.environ.get("SANDBOX_ROOT", Path.home() / "Desktop" / "SandBox")).expanduser()


def scripts_root(home: Path) -> Path:
    return home / "scripts"


def find_supported_scripts(root: Path) -> list[Path]:
    suffixes = {".py", ".sh", ".bash", ".ps1", ".ts", ".js"}
    return sorted(
        (p for p in root.iterdir() if p.is_file() and p.suffix.lower() in suffixes),
        key=lambda p: p.name.casefold(),
    )


def find_nested_repos(repo: Path) -> list[Path]:
    repos: list[Path] = []
    for candidate in (repo, *repo.glob("projects/*")):
        if not candidate.is_dir():
            continue
        if (candidate / ".git").exists():
            repos.append(candidate)
    return repos


def git_status(repo: Path) -> dict[str, Any]:
    try:
        branch = subprocess.run(
            ["git", "-C", str(repo), "branch", "--show-current"],
            capture_output=True,
            text=True,
            timeout=15,
            check=True,
        ).stdout.strip()
        sha = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            timeout=15,
            check=True,
        ).stdout.strip()
        dirty_lines = subprocess.run(
            ["git", "-C", str(repo), "status", "--porcelain"],
            capture_output=True,
            text=True,
            timeout=15,
            check=True,
        ).stdout.splitlines()
        return {
            "repo": str(repo),
            "branch": branch,
            "head": sha,
            "dirty": len(dirty_lines),
        }
    except subprocess.SubprocessError as exc:
        return {"repo": str(repo), "error": str(exc)[:200]}


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dedupe_report(repo: Path) -> dict[str, Any]:
    """Group supported scripts by SHA-256 across repo and Hermes scripts.

    Only exact-content duplicates are reported. No file is deleted.
    """
    sources: list[Path] = [scripts_root(hermes_home()), *find_supported_scripts_paths(repo)]
    groups: dict[str, list[str]] = {}
    for source in sources:
        if not source.is_file():
            continue
        try:
            digest = hash_file(source)
        except OSError:
            continue
        groups.setdefault(digest, []).append(str(source))
    duplicates = {h: paths for h, paths in groups.items() if len(paths) > 1}
    return {
        "total_sources": len(sources),
        "unique_hashes": len(groups),
        "duplicate_groups": len(duplicates),
        "duplicates": duplicates,
    }


def find_supported_scripts_paths(repo: Path) -> list[Path]:
    """Return candidate duplicates: root-level scripts/ in the repo only.

    Nested project scripts are intentionally excluded to avoid touching
    autonomous project tooling.
    """
    candidate = repo / "scripts"
    if not candidate.is_dir():
        return []
    suffixes = {".py", ".sh", ".bash", ".ps1", ".ts", ".js"}
    return [p for p in candidate.iterdir() if p.is_file() and p.suffix.lower() in suffixes]


def inventory(repo: Path, home: Path) -> dict[str, Any]:
    return {
        "workspace": str(repo),
        "hermes_home": str(home),
        "hermes_scripts": [p.name for p in find_supported_scripts(scripts_root(home))],
        "nested_repos": [git_status(r) for r in find_nested_repos(repo)],
    }


def docker_inventory() -> dict[str, Any]:
    """Return ``docker system df`` and short listings, or an error string."""
    try:
        df = subprocess.run(
            [
                "docker",
                "system",
                "df",
                "--format",
                "{{.Type}}\t{{.TotalCount}}\t{{.Active}}\t{{.Size}}\t{{.Reclaimable}}",
            ],
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        ).stdout
        images = subprocess.run(
            ["docker", "image", "ls", "-a", "--format", "{{.Repository}}:{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}"],
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        ).stdout
        containers = subprocess.run(
            ["docker", "ps", "-a", "--format", "{{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}"],
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        ).stdout
        volumes = subprocess.run(
            ["docker", "volume", "ls", "--format", "{{.Name}}"],
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        ).stdout
        return {
            "df": [line.split("\t") for line in df.splitlines() if line],
            "images": [line.split("\t") for line in images.splitlines() if line],
            "containers": [line.split("\t") for line in containers.splitlines() if line],
            "volumes": [v for v in volumes.splitlines() if v],
        }
    except (subprocess.SubprocessError, FileNotFoundError) as exc:
        return {"error": str(exc)[:200]}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=repo_root())
    ap.add_argument("--hermes-home", type=Path, default=hermes_home())
    sub = ap.add_subparsers(dest="command", required=True)

    sub.add_parser("inventory")
    sub.add_parser("dedupe-report")
    sub.add_parser("docker-inventory")
    sub.add_parser("git-status")

    sync = sub.add_parser("config-sync")
    sync.add_argument("--apply", action="store_true", help="actually call hermes config set")
    sync.add_argument("--registry", type=Path, required=True)
    sync.add_argument("--profile", action="append", default=[])

    judge = sub.add_parser("scripts-judge")
    judge.add_argument("--registry", type=Path, required=True)
    judge.add_argument("--output", type=Path, default=Path(".hermes/reports/scripts-judge-final.json"))

    args = ap.parse_args(argv)
    if args.command == "inventory":
        print(json.dumps(inventory(args.repo, args.hermes_home), indent=2))
        return 0
    if args.command == "dedupe-report":
        print(json.dumps(dedupe_report(args.repo), indent=2))
        return 0
    if args.command == "docker-inventory":
        print(json.dumps(docker_inventory(), indent=2))
        return 0
    if args.command == "git-status":
        print(json.dumps([git_status(r) for r in find_nested_repos(args.repo)], indent=2))
        return 0
    if args.command == "config-sync":
        if not args.apply:
            print(json.dumps({"apply": False, "hint": "rerun with --apply to mutate live config"}, indent=2))
            return 0
        raise SystemExit("config-sync --apply is not yet implemented; required explicit owner approval")
    if args.command == "scripts-judge":
        raise SystemExit("scripts-judge gating is a follow-up; requires owner decision on which copies to update")
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    sys.exit(main())
