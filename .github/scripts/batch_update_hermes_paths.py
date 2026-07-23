#!/usr/bin/env python3
"""Batch update Hermes paths — normalize, update, and audit file/folder paths across workspace.

Usage:
    python batch_update_hermes_paths.py [--scan] [--workspace PATH] [--dry-run] [--apply] [--validate] [--mapping FILE]
"""

import asyncio
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Batch update Hermes paths")
    parser.add_argument("--scan", action="store_true", help="Inventory all path references")
    parser.add_argument("--workspace", default=None, help="Root workspace directory")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without applying")
    parser.add_argument("--apply", action="store_true", help="Apply path updates")
    parser.add_argument("--validate", action="store_true", help="Verify no broken references")
    parser.add_argument("--mapping", default=None, help="Custom path mapping file (JSON)")
    return parser.parse_args(argv)


DEFAULT_MAPPINGS = {
    r"Bash/": "projects/Bash/",
    r"Resume_maker/": "projects/Resume_maker/",
    r"scripts/": "projects/Bash/scripts/",
}


def discover_files(root: Path) -> list[Path]:
    """Discover all text files in workspace that may contain path references."""
    exts = {".md", ".py", ".yaml", ".yml", ".json", ".toml", ".cfg", ".ini", ".txt"}
    files = []
    for ext in exts:
        files.extend(root.rglob(f"*{ext}"))
    # Exclude common non-source dirs
    exclude_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv", ".worktrees"}
    return [f for f in files if not any(p in exclude_dirs for p in f.relative_to(root).parts)]


async def scan_paths_async(file: Path, workspace: str) -> list[dict]:
    """Scan a single file for Hermes path references."""
    return await asyncio.to_thread(_scan_paths, file, workspace)


def _scan_paths(file: Path, workspace: str) -> list[dict]:
    """Scan file for Hermes path references (CPU-bound IO + pattern matching)."""
    try:
        text = file.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []
    references = []
    for i, line in enumerate(text.splitlines(), 1):
        if "hermes" in line.lower() or "AppData" in line or "LOCALAPPDATA" in line:
            references.append({"file": str(file), "line": i, "content": line.strip()})
    return references


async def apply_mapping_async(file: Path, old: str, new: str, dry_run: bool) -> dict:
    """Apply a single path mapping to a file."""
    return await asyncio.to_thread(_apply_mapping, file, old, new, dry_run)


def _apply_mapping(file: Path, old: str, new: str, dry_run: bool) -> dict:
    """Apply mapping and return change info."""
    try:
        text = file.read_text(encoding="utf-8")
    except Exception:
        return {"file": str(file), "changes": 0, "error": "Cannot read"}
    count = text.count(old)
    if count == 0:
        return {"file": str(file), "changes": 0}
    text = text.replace(old, new)
    if not dry_run:
        file.write_text(text, encoding="utf-8")
    return {"file": str(file), "changes": count}


async def validate_references(root: Path) -> list[str]:
    """Check for broken path references in workspace files."""
    files = discover_files(root)
    broken: list[str] = []

    async def _check_file(file: Path) -> None:
        try:
            text = await asyncio.to_thread(file.read_text, encoding="utf-8", errors="replace")
            root_str = str(root).replace("\\", "/").lower()
        except Exception:
            return
        for line in text.splitlines():
            if "AppData/Local/hermes" in line and "AppData/Local/hermes" not in root_str:
                if "refers" not in line.lower():
                    broken.append(f"{file.name}: possibly external path reference")

    tasks = [_check_file(f) for f in files]
    await asyncio.gather(*tasks)
    return broken


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    workspace = Path(args.workspace).expanduser().resolve() if args.workspace else Path.cwd()

    if not workspace.is_dir():
        print(f"ERROR: workspace not found: {workspace}", file=sys.stderr)
        sys.exit(1)

    mappings = DEFAULT_MAPPINGS.copy()
    if args.mapping:
        mapping_path = Path(args.mapping)
        custom = json.loads(mapping_path.read_text(encoding="utf-8"))
        mappings.update(custom)

    if args.scan:
        print(f"Scanning workspace: {workspace}")
        files = discover_files(workspace)
        tasks = [scan_paths_async(f, str(workspace)) for f in files]
        results = await asyncio.gather(*tasks)
        all_refs = [r for batch in results for r in batch]
        print(f"Found {len(all_refs)} path references across {len(files)} files")
        for ref in all_refs[:50]:  # Show first 50
            print(f"  {ref['file']}:{ref['line']}  {ref['content'][:120]}")

        report_path = workspace / "hermes_path_inventory.json"
        report_path.write_text(json.dumps(all_refs, indent=2), encoding="utf-8")
        print(f"\nFull inventory written to {report_path}")

    if args.apply or args.dry_run:
        files = discover_files(workspace)
        all_changes = []
        for old, new in mappings.items():
            tasks = [apply_mapping_async(f, old, new, args.dry_run) for f in files]
            results = await asyncio.gather(*tasks)
            all_changes.extend(results)

        total = sum(c["changes"] for c in all_changes)
        mode = "DRY-RUN" if args.dry_run else "APPLY"
        print(f"\n{mode}: {total} total replacements across {len([c for c in all_changes if c['changes'] > 0])} files")
        for c in all_changes:
            if c["changes"] > 0:
                print(f"  {c['file']}: {c['changes']} change(s)")

    if args.validate:
        print(f"\nValidating references in {workspace}")
        broken = await validate_references(workspace)
        if broken:
            print(f"Found {len(broken)} potential issues:")
            for b in broken:
                print(f"  {b}")
        else:
            print("No issues found.")


if __name__ == "__main__":
    asyncio.run(main())
