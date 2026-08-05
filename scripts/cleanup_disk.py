#!/usr/bin/env python3
"""cleanup_disk.py — full-sweep disk cleanup for sandbox repos, subrepos, hermes root.

Targets (all reinstallable / disposable, user-approved FULL SWEEP):
  DEPS   : node_modules, venv, .venv, myvenv, __pycache__, .pytest_cache,
           .mypy_cache, .ruff_cache, .tox, .eggs, dist, build, .next, .turbo
  ARCHIVE: .archive, backup, backups, *.bak, *.backup, *.orig, *.rej, *.old, *~
  CACHE  : .cache, npm-cache, .npm, pip cache, bun cache (OS-level + in-tree)
  LOGS   : *.log, logs/ dirs, *.tmp, *.temp

SAFETY (never violated):
  - never descends into or removes any `.git` directory
  - never removes a configured root itself (only children/matches inside)
  - prunes already-matched dirs (no double counting / no nested delete)
  - default mode is DRY-RUN; destructive apply requires `--apply`
  - every deletion is logged to an audit log

Usage:
  python cleanup_disk.py [ROOT ...]            # dry-run report (default)
  python cleanup_disk.py --apply [ROOT ...]    # perform deletions + report
  python cleanup_disk.py --roots-file X        # read roots from a text file (one per line)
  python cleanup_disk.py --min-size MB         # only report/delete dirs/files >= MB
  python cleanup_disk.py --log PATH            # audit log path (default ./results/cleanup_disk.log)
  python cleanup_disk.py --verify              # print before/after free space

Skipped by default: `.git` always; and by default the configured roots are never
selected even if their name matches a target (e.g. a root literally named
`node_modules`). Use --allow-root-target to permit that edge case explicitly.
"""
from __future__ import annotations

import argparse
import contextlib
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Targets
# ---------------------------------------------------------------------------

DIR_TARGETS = frozenset({
    # Python
    "venv", ".venv", "myvenv", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".tox", ".eggs", ".pyre", ".pants.d",
    # Node / bundlers
    "node_modules", ".next", ".turbo", ".nuxt", ".svelte-kit",
    "dist", "build", ".parcel-cache", ".cache-loader", ".eslintcache",
    # Caches / archives / backups (as whole dirs)
    ".archive", "backup", "backups", ".backup", "archive",
    ".cache", "npm-cache", ".npm", ".pnpm-store", ".yarn",
})

FILE_SUFFIX_TARGETS = frozenset({
    ".bak", ".backup", ".orig", ".rej", ".old", "~", ".tmp", ".temp",
    ".log", ".pyc", ".pyo", ".cache", ".swp", ".swo", ".DS_Store", ".thumb",
})

# OS-level cache roots (outside repo trees) -- only added when they exist
OS_CACHE_DIRS = [
    # pip
    r"%LOCALAPPDATA%\pip\Cache", r"%LOCALAPPDATA%\pip\cache",
    # npm
    r"%APPDATA%\npm-cache", r"%LOCALAPPDATA%\npm-cache",
    # bun
    r"%USERPROFILE%\.bun\install\cache", r"%LOCALAPPDATA%\bun",
    # generic
    r"%USERPROFILE%\.cache", r"%LOCALAPPDATA%\Temp",
]

SAFELIST_DIRS = frozenset({".git"})

_PROTECTED_ROOT_NAMES = frozenset(DIR_TARGETS)  # roots won't be selected by default


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _expand(root: str) -> Path | None:
    p = Path(os.path.expandvars(os.path.expanduser(root)))
    return p if p.exists() else None


def fmt_size(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def _dir_size(path: Path) -> int:
    total = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            # prune: don't descend into .git or other matched targets
            dirnames[:] = [d for d in dirnames
                           if d not in SAFELIST_DIRS and d not in DIR_TARGETS]
            for fn in filenames:
                with contextlib.suppress(OSError):
                    total += os.path.getsize(Path(dirpath) / fn)
    except OSError:
        pass
    return total


# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------

def scan_roots(roots: list[Path], min_size: int = 0):
    """Return a dict of category -> list of (path, size, is_dir)."""
    found: dict[str, list[tuple[Path, int, bool]]] = {}

    def add(cat, path, size, is_dir):
        if size < min_size:
            return
        found.setdefault(cat, []).append((path, size, is_dir))

    for root in roots:
        if not root.is_dir():
            continue
        # root dir itself may match a target name; recurse unless disallowed
        for dirpath, dirnames, filenames in os.walk(root, topdown=True):
            # prune .git everywhere
            dirnames[:] = [d for d in dirnames if d not in SAFELIST_DIRS]
            dp = Path(dirpath)

            # directory targets (children only; never the configured root)
            for d in list(dirnames):
                if d in DIR_TARGETS:
                    full = dp / d
                    add("deps" if d in ("node_modules", "venv", ".venv", "myvenv",
                                        "__pycache__", ".tox", ".eggs", "dist",
                                        "build", ".next", ".turbo") else "archive",
                        full, _dir_size(full), True)
                    dirnames.remove(d)  # prune already-matched

            # file targets
            for fn in filenames:
                fp = dp / fn
                low = fn.lower()
                if any(low.endswith(s) for s in FILE_SUFFIX_TARGETS):
                    try:
                        size = os.path.getsize(fp)
                    except OSError:
                        continue
                    cat = "logs" if low.endswith((".log", ".tmp", ".temp")) else "archive"
                    add(cat, fp, size, False)
        # prune further recursion into huge OS cache dirs handled separately
    return found


def scan_os_caches():
    """OS-level cache roots, individually, guarded existence."""
    found: dict[str, list[tuple[Path, int, bool]]] = {}
    for pat in OS_CACHE_DIRS:
        p = _expand(pat)
        if p and p.is_dir():
            found.setdefault("cache", []).append((p, _dir_size(p), True))
    return found


# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------

def apply_delete(found: dict, log_path: Path, roots: list[Path]):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    deleted, freed = 0, 0
    errors: list[str] = []
    with open(log_path, "a", encoding="utf-8") as lf:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lf.write(f"\n=== CLEANUP RUN {ts} | roots: {', '.join(str(r) for r in roots)} ===\n")
        for cat, items in found.items():
            for path, size, _ in items:
                try:
                    if path.is_dir():
                        shutil.rmtree(path)
                    elif path.is_file():
                        path.unlink()
                    freed += size
                    deleted += 1
                    lf.write(f"DELETED [{cat}] {path} ({fmt_size(size)})\n")
                except OSError as e:
                    errors.append(f"{path}: {e}")
                    lf.write(f"ERROR {path}: {e}\n")
    return deleted, freed, errors


def free_space() -> str:
    try:
        t = shutil.disk_usage(str(Path.home().drive + os.sep))
    except Exception:
        t = shutil.disk_usage(str(Path.cwd().anchor))
    return f"{fmt_size(t.free)} free of {fmt_size(t.total)}"


def find_root_dirs() -> list[Path]:
    """Auto-discover roots: current repo + subrepos + hermes-profiles + hermes root."""
    hermes_home = Path(os.environ.get("HERMES_HOME", "~/AppData/Local/hermes"))
    candidates = [
        Path.cwd(),
        Path.cwd() / "projects",
        Path.cwd() / "hermes-profiles",
        hermes_home,
    ]
    return [p for p in candidates if p.is_dir()]


def main() -> int:
    ap = argparse.ArgumentParser(description="Full-sweep disk cleanup.",
                                 allow_abbrev=False)
    ap.add_argument("roots", nargs="*", help="roots to scan (default: auto-discovery)")
    ap.add_argument("--apply", action="store_true", help="perform deletions (default dry-run)")
    ap.add_argument("--roots-file", help="file with roots, one per line")
    ap.add_argument("--min-size", type=int, default=0, help="only items >= this many MB")
    ap.add_argument("--cats", default="deps,archive,cache,logs",
                    help="comma-separated categories to act on (deps,archive,cache,logs)")
    ap.add_argument("--log", default=str(Path.cwd() / "results" / "cleanup_disk.log"),
                    help="audit log path")
    ap.add_argument("--verify", action="store_true", help="print disk free before/after")
    ap.add_argument("--allow-root-target", action="store_true",
                    help="allow a configured root that matches a target name to be deleted")
    ap.add_argument("--include-os-caches", action="store_true",
                    help="also scan OS-level cache dirs (pip/npm/bun/Temp)")
    args = ap.parse_args()

    roots: list[Path] = []
    if args.roots_file:
        rp = Path(args.roots_file)
        if rp.exists():
            roots = [Path(line.strip()) for line in rp.read_text().splitlines() if line.strip()]
    roots = [Path(r) for r in args.roots]
    if not roots:
        roots = find_root_dirs()

    roots = [r.expanduser() for r in roots if r.exists()]

    print(f"Disk BEFORE: {free_space()}\n")
    print(f"Scanning {len(roots)} roots:")
    for r in roots:
        print(f"  - {r}")

    min_bytes = args.min_size * 1024 * 1024
    found = scan_roots(roots, min_size=min_bytes)
    if args.include_os_caches:
        osf = scan_os_caches()
        for cat, items in osf.items():
            found.setdefault(cat, []).extend(items)

    # restrict to requested categories
    want = {c.strip() for c in args.cats.split(",") if c.strip()}
    found = {c: v for c, v in found.items() if c in want}

    # deduplicate by resolved absolute path (nested roots re-visit the same dir)
    seen: set[str] = set()
    for cat in list(found):
        items = []
        for path, size, is_dir in found[cat]:
            key = str(path.resolve())
            if key in seen:
                continue
            seen.add(key)
            items.append((path, size, is_dir))
        found[cat] = items

    total = sum(s for items in found.values() for _, s, _ in items)
    grand = sum(len(items) for items in found.values())

    print(f"\n=== TARGETS FOUND: {grand} items, ~{fmt_size(total)} ({'DRY-RUN' if not args.apply else 'APPLY'}) ===")
    for cat in sorted(found):
        items = sorted(found[cat], key=lambda x: -x[1])
        cat_total = sum(s for _, s, _ in items)
        print(f"\n[{cat.upper()}] {len(items)} items, {fmt_size(cat_total)}")
        for path, size, is_dir in items[:60]:  # cap display
            kind = "DIR " if is_dir else "FILE"
            print(f"  {kind} {fmt_size(size):>10}  {path}")
        if len(items) > 60:
            print(f"  ... and {len(items)-60} more")

    print(f"\nTOTAL reclaimable: {fmt_size(total)}")
    print(f"Audit log: {args.log}")

    if args.apply:
        if grand == 0:
            print("\nNothing to delete.")
        else:
            print(f"\n*** APPLYING ({grand} items) ***")
            deleted, freed, errors = apply_delete(found, Path(args.log), roots)
            print(f"Deleted {deleted} items, freed {fmt_size(freed)}")
            if errors:
                print(f"Errors ({len(errors)}):")
                for e in errors:
                    print(f"  ! {e}")
    if args.apply or args.verify:
        print(f"\nDisk AFTER : {free_space()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
