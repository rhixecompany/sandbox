#!/usr/bin/env python3
"""Cleanup inventory + dry-run for node_modules/.venv/venv across ~/ and ./.

Classifies every candidate dir as SAFE (repo-local, gitignored, reinstallable),
SYSTEM (managed by tools/extensions — never touch), or ASK (home-level, needs
per-item user decision). Emits results/cleanup-dry-run.md and a stdout summary.

Usage:
  python scripts/cleanup_inventory.py            # dry-run (default, safe)
  python scripts/cleanup_inventory.py --apply    # delete SAFE dirs (destructive,
                                                 # requires --yes after user approval)
  python scripts/cleanup_inventory.py --json     # also write results/cleanup-dry-run.json

Design notes (Windows/MSYS-safe):
  - No `du` subprocess (MSYS du is pathologically slow on big trees).
    Sizes come from a bounded os.scandir recursion with a global time budget.
  - Junction/symlink loops prevented via a visited-realpath set.
  - Git tracking check via `git -C <repo> check-ignore -q <rel>` per owning repo.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

HOME = Path.home()
SANDBOX = HOME / "Desktop" / "SandBox"
RESULTS = SANDBOX / "results"
OUT_MD = RESULTS / "cleanup-dry-run.md"
OUT_JSON = RESULTS / "cleanup-dry-run.json"

TARGET_NAMES = {"node_modules", ".venv", "venv"}

# Path components (lowercased) that mark a directory as system-managed. Never touch.
SYSTEM_MARKERS = {
    ".vscode", ".bun", ".opencode", ".copilot", "pipx", "hermes-profiles",
    "appdata", "application data", "onedrive", ".git", ".config",
}

# Directories never descended into (either protected, huge, or noise).
PRUNE = {
    "node_modules", ".venv", "venv",          # detection targets (prune after detect)
    ".git", ".next", "dist", "build", "__pycache__",
    ".mypy_cache", ".ruff_cache", ".pytest_cache",
    "hermes-profiles", "appdata", "application data", "onedrive",
    "cookies", "favorites", "links", "local settings", "music",
    "my documents", "nethood", "printhood", "recent", "saved games",
    "searches", "sendto", "start menu", "templates", "videos",
    "intelgraphicsprofiles",
}

SIZE_DEADLINE_SECONDS = 180.0  # global budget for all sizing


def classify(path: Path) -> str:
    """SAFE | SYSTEM | ASK."""
    parts_lower = [p.lower() for p in path.parts]
    if any(m in parts_lower for m in SYSTEM_MARKERS):
        return "SYSTEM"
    try:
        if path.is_relative_to(SANDBOX):
            return "SAFE"
    except AttributeError:  # py <3.9
        if str(path).lower().startswith(str(SANDBOX).lower()):
            return "SAFE"
    return "ASK"


def find_target_dirs(root: Path, max_depth: int) -> list[Path]:
    """Walk root, detect node_modules/.venv/venv, never descend into targets or PRUNE."""
    hits: list[Path] = []
    root = root.resolve()
    visited = {str(root)}
    for dirpath, dirnames, filenames in os.walk(root):
        # detect before pruning
        for d in list(dirnames):
            if d in TARGET_NAMES:
                hits.append(Path(dirpath) / d)
        # depth cap
        depth = dirpath[len(str(root)):].count(os.sep)
        # prune
        kept = []
        for d in dirnames:
            if d in PRUNE:
                continue
            child = os.path.join(dirpath, d)
            try:
                rp = os.path.realpath(child)
            except OSError:
                continue
            if rp in visited:
                continue
            visited.add(rp)
            kept.append(d)
        dirnames[:] = kept
        if depth >= max_depth:
            dirnames[:] = []
    return hits


def dir_size(path: Path, deadline: float) -> int | None:
    """Sum file bytes under path. None on timeout/error (reported as n/a)."""
    total = 0

    def rec(p: Path) -> bool:
        nonlocal total
        try:
            with os.scandir(p) as it:
                for e in it:
                    if time.monotonic() > deadline:
                        return False
                    try:
                        if e.is_dir(follow_symlinks=False):
                            if not rec(Path(e.path)):
                                return False
                        else:
                            total += e.stat(follow_symlinks=False).st_size
                    except OSError:
                        continue
        except OSError:
            return False
        return True

    if rec(path):
        return total
    return None


def owning_repo(path: Path) -> Path | None:
    """Walk up until a .git dir/file is found; return repo root or None."""
    cur = path
    while True:
        if (cur / ".git").exists():
            return cur
        if cur.parent == cur:
            return None
        cur = cur.parent


def git_ignored(repo: Path, target: Path) -> str:
    """'ignored' | 'NOT-IGNORED' | 'no-repo' | 'git-error'."""
    try:
        rel = target.relative_to(repo)
    except ValueError:
        return "outside-repo"
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo), "check-ignore", "-q", str(rel)],
            capture_output=True, timeout=20,
        )
    except (subprocess.TimeoutExpired, OSError):
        return "git-error"
    return "ignored" if proc.returncode == 0 else "NOT-IGNORED"


def human_mb(n: int | None) -> str:
    if n is None:
        return "n/a"
    return f"{n / 1048576:.1f} MB"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="delete SAFE dirs (destructive)")
    ap.add_argument("--yes", action="store_true", help="required with --apply")
    ap.add_argument("--json", action="store_true", help="also write JSON sidecar")
    args = ap.parse_args()

    if args.apply and not args.yes:
        print("REFUSING: --apply requires --yes (destructive). Aborting.", file=sys.stderr)
        return 2

    # ---- Phase A: scan ----
    print("Scanning ...")
    t0 = time.monotonic()
    sandbox_hits = find_target_dirs(SANDBOX, max_depth=6)
    home_hits = []
    # HOME walk: skip the SandBox subtree to avoid dupes
    for entry in os.scandir(HOME):
        if not entry.is_dir(follow_symlinks=False):
            continue
        if entry.name in {"AppData", "Application Data", "OneDrive"}:
            continue
        p = Path(entry.path)
        if p.resolve() == SANDBOX:
            continue
        home_hits += find_target_dirs(p, max_depth=4)
    scan_secs = time.monotonic() - t0
    print(f"  scan took {scan_secs:.1f}s; found {len(sandbox_hits)} (SandBox) + {len(home_hits)} (home)")

    # dedupe + order: SandBox first
    seen: set[str] = set()
    hits: list[Path] = []
    for p in sandbox_hits + home_hits:
        key = str(p.resolve())
        if key in seen:
            continue
        seen.add(key)
        hits.append(p)
    hits.sort(key=lambda p: (classify(p) != "SAFE", str(p).lower()))

    # ---- Phase B: classify + size + git check ----
    deadline = time.monotonic() + SIZE_DEADLINE_SECONDS
    rows = []
    for p in hits:
        cls = classify(p)
        size = dir_size(p, deadline) if cls != "SYSTEM" else None
        repo = owning_repo(p) if cls in ("SAFE", "ASK") else None
        tracked = git_ignored(repo, p) if (cls in ("SAFE", "ASK") and repo) else "no-repo"
        rows.append({
            "path": str(p), "kind": p.name, "class": cls, "size": size,
            "repo": str(repo) if repo else None, "tracked": tracked,
        })

    # ---- Phase C: summary + report ----
    by_cls: dict[str, list[dict]] = {"SAFE": [], "ASK": [], "SYSTEM": []}
    for r in rows:
        by_cls[r["class"]].append(r)

    def total(rs: list[dict]) -> int:
        return sum(r["size"] for r in rs if r["size"] is not None)

    safe_mb, ask_mb = total(by_cls["SAFE"]), total(by_cls["ASK"])
    RESULTS.mkdir(parents=True, exist_ok=True)

    def fmt_row(r: dict) -> str:
        note = ""
        if r["class"] == "SYSTEM":
            note = "managed by tool/extension — never touch"
        elif r["tracked"] == "NOT-IGNORED":
            note = "*** NOT GITIGNORED — deletion would remove tracked files ***"
        elif r["tracked"] == "ignored":
            note = "gitignored (safe)"
        else:
            note = r["tracked"]
        return f"| `{r['path']}` | {r['kind']} | {human_mb(r['size'])} | {note} |"

    lines = [
        "# Cleanup Dry-Run Report",
        "",
        f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S')} | cwd: `{SANDBOX}`",
        "",
        "## Summary",
        "",
        f"| Class | Dirs | Reclaimable (known) | Action |",
        "|-------|------|--------------------|--------|",
        f"| SAFE | {len(by_cls['SAFE'])} | {human_mb(safe_mb)} | delete pending approval |",
        f"| ASK | {len(by_cls['ASK'])} | {human_mb(ask_mb)} | per-item decision |",
        f"| SYSTEM | {len(by_cls['SYSTEM'])} | (protected) | never touch |",
        "",
        "## SAFE — ready to delete (pending recorded approval)",
        "",
        "| Path | Kind | Size | Git |",
        "|------|------|------|-----|",
    ]
    lines += [fmt_row(r) for r in by_cls["SAFE"]]
    lines += [
        "",
        "## ASK — needs per-item user decision",
        "",
        "| Path | Kind | Size | Git |",
        "|------|------|------|-----|",
    ]
    lines += [fmt_row(r) for r in by_cls["ASK"]]
    lines += [
        "",
        "## SYSTEM — protected, never touched",
        "",
        "| Path | Kind | Reason |",
        "|------|------|--------|",
    ]
    lines += [f"| `{r['path']}` | {r['kind']} | managed by tool/extension |" for r in by_cls["SYSTEM"]]
    lines += [
        "",
        "## Reinstall reference (post-cleanup)",
        "",
        "- npm/bun: `bun install` (or `npm ci` where lockfile present)",
        "- python: `uv venv` + `uv pip install -r requirements.txt` (or `uv sync`)",
        "",
        "> Gate: SAFE deletions require recorded approval (see executing-plans skill:",
        "> approval request in `.hermes/approvals/`). Nothing was deleted by this dry run.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if args.json:
        OUT_JSON.write_text(
            json.dumps({"generated": time.strftime("%Y-%m-%d %H:%M:%S"), "rows": rows},
                       indent=2, default=str),
            encoding="utf-8",
        )

    # ---- Phase D: stdout summary ----
    print()
    print(f"SAFE    : {len(by_cls['SAFE']):3d} dirs, {human_mb(safe_mb)} reclaimable (gitignored, reinstallable)")
    for r in by_cls["SAFE"]:
        flag = "  <-- NOT GITIGNORED" if r["tracked"] == "NOT-IGNORED" else ""
        print(f"    {r['path']}{flag}")
    print(f"ASK     : {len(by_cls['ASK']):3d} dirs, {human_mb(ask_mb)}")
    for r in by_cls["ASK"]:
        print(f"    {r['path']}")
    print(f"SYSTEM  : {len(by_cls['SYSTEM']):3d} dirs (protected)")
    print(f"Report  : {OUT_MD}")
    if args.json:
        print(f"JSON    : {OUT_JSON}")

    # ---- Phase E: --apply (destructive, gated) ----
    if args.apply:
        print("\nAPPLY MODE — deleting SAFE dirs ...")
        deleted, skipped = [], []
        for r in by_cls["SAFE"]:
            p = Path(r["path"])
            if not p.exists():
                skipped.append((str(p), "missing"))
                continue
            if r["tracked"] == "NOT-IGNORED":
                skipped.append((str(p), "NOT GITIGNORED — refusing"))
                continue
            try:
                shutil.rmtree(p)
                deleted.append(str(p))
            except OSError as e:
                skipped.append((str(p), str(e)))
        print(f"  deleted {len(deleted)}, skipped {len(skipped)}")
        for s in skipped:
            print(f"    SKIP {s[0]} ({s[1]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
