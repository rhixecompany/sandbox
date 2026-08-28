#!/usr/bin/env python3
"""
disk_cleanup.py — Safe cache cleanup + large-file inventory for Windows.

NON-DESTRUCTIVE: does NOT uninstall any apps. Only cleans caches and
reports large files for manual review.

Usage:
    python scripts/disk_cleanup.py --dry-run   # show what would be cleaned
    python scripts/disk_cleanup.py              # actually clean caches
"""
import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Cache directories to clean
CACHE_DIRS = [
    # npm / node
    (Path.home() / ".npm", "npm cache"),
    (Path.home() / "AppData" / "Roaming" / "npm-cache", "npm roaming cache"),
    (Path.home() / "AppData" / "Local" / "pnpm", "pnpm store"),
    (Path.home() / "AppData" / "Local" / "bun", "bun cache"),
    # VS Code
    (Path.home() / "AppData" / "Roaming" / "Code" / "Cache", "VS Code cache"),
    (Path.home() / "AppData" / "Roaming" / "Code" / "User" / "globalStorage" / "cache", "VS Code globalStorage cache"),
    # pip / uv
    (Path.home() / ".cache" / "pip", "pip cache"),
    (Path.home() / "AppData" / "Local" / "uv" / "cache", "uv cache"),
    # Browser caches
    (Path.home() / "AppData" / "Local" / "Google" / "Chrome" / "User Data" / "Default" / "Cache", "Chrome cache"),
    (Path.home() / "AppData" / "Local" / "Microsoft" / "Edge" / "User" / "Default" / "Cache", "Edge cache"),
    # Windows temp
    (Path.home() / "AppData" / "Local" / "Temp", "user temp (files >7d only)"),
    # Winget cache
    (Path.home() / "AppData" / "Local" / "Packages" / "Microsoft.DesktopAppInstaller_8wek3aa_ccef4xse" / "LocalState" / "Cache", "winget cache"),
]

# Large file scan roots (top 3 levels)
SCAN_ROOTS = [
    Path.home() / "Downloads",
    Path.home() / "AppData" / "Local" / "Temp",
    Path.home() / "Desktop",
]

LARGE_FILE_THRESHOLD_MB = 50


def dir_size_bytes(path: Path) -> int:
    """Calculate total size of a directory in bytes (best-effort)."""
    total = 0
    try:
        for item in path.rglob("*"):
            if item.is_file():
                try:
                    total += item.stat().st_size
                except (OSError, PermissionError):
                    pass
    except (PermissionError, OSError):
        pass
    return total


def find_large_files(roots: list[Path], threshold_mb: int) -> list[dict]:
    """Find files larger than threshold, scanning top 3 levels of each root."""
    threshold = threshold_mb * 1024 * 1024
    large_files = []
    for root in roots:
        if not root.exists():
            continue
        try:
            for item in root.rglob("*"):
                if item.is_file():
                    try:
                        depth = len(item.relative_to(root).parts)
                        if depth > 3:
                            continue
                        size = item.stat().st_size
                        if size > threshold:
                            large_files.append({
                                "path": str(item),
                                "size_mb": round(size / (1024 * 1024), 1),
                                "modified": datetime.fromtimestamp(
                                    item.stat().st_mtime, tz=timezone.utc
                                ).isoformat(),
                            })
                    except (OSError, PermissionError):
                        pass
        except (PermissionError, OSError):
            pass
    large_files.sort(key=lambda x: x["size_mb"], reverse=True)
    return large_files[:50]  # top 50


def clean_cache_dir(path: Path, label: str, dry_run: bool) -> dict[str, Any]:
    """Clean a cache directory. Returns before/after size info."""
    result: dict[str, Any] = {"label": label, "path": str(path), "existed": path.exists(), "before_mb": 0.0, "after_mb": 0.0, "freed_mb": 0.0, "action": "none"}

    if not path.exists():
        return result

    before = dir_size_bytes(path)
    result["before_mb"] = round(before / (1024 * 1024), 1)

    if dry_run or before == 0:
        result["action"] = "dry_run" if dry_run else "empty"
        return result

    # Delete contents but keep the directory
    for item in path.iterdir():
        try:
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
        except (OSError, PermissionError) as e:
            result["error"] = str(e)

    after = dir_size_bytes(path) if path.exists() else 0
    result["after_mb"] = round(after / (1024 * 1024), 1)
    result["freed_mb"] = round((before - after) / (1024 * 1024), 1)
    result["action"] = "cleaned"
    return result


def main():
    parser = argparse.ArgumentParser(description="Safe disk cleanup + large-file inventory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be cleaned without deleting")
    parser.add_argument("--scan-large", action="store_true", help="Also scan for large files (>50MB)")
    args = parser.parse_args()

    report: dict[str, Any] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dry_run": args.dry_run,
        "cache_cleanup": [],
        "large_files": [],
        "total_freed_mb": 0.0,
    }

    print(f"{'DRY RUN: ' if args.dry_run else ''}Disk Cleanup Report")
    print("=" * 60)
    print("\nCache Directories:")
    print("-" * 60)

    total_freed = 0
    for path, label in CACHE_DIRS:
        result = clean_cache_dir(path, label, args.dry_run)
        report["cache_cleanup"].append(result)
        total_freed += result["freed_mb"]
        status = "→" if not args.dry_run and result["freed_mb"] > 0 else " "
        print(f"  {status} {label:45s} {result['before_mb']:>8.1f} MB → {result['after_mb']:>8.1f} MB  (freed: {result['freed_mb']:.1f} MB) [{result['action']}]")

    report["total_freed_mb"] = round(total_freed, 1)

    if args.scan_large:
        print("\nLarge Files (>50 MB, top 50):")
        print("-" * 60)
        large_files = find_large_files(SCAN_ROOTS, LARGE_FILE_THRESHOLD_MB)
        report["large_files"] = large_files
        for f in large_files[:25]:
            print(f"  {f['size_mb']:>8.1f} MB  {f['path']}")
        if len(large_files) > 25:
            print(f"  ... and {len(large_files) - 25} more (see full report)")

    print(f"\n{'Would have freed' if args.dry_run else 'Freed'}: {total_freed:.1f} MB total")

    # Write report
    report_dir = Path(__file__).resolve().parent.parent / ".hermes" / "plans" / "2026-08-28-unified-platform-remediation"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"disk-cleanup-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nReport written: {report_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
