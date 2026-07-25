#!/usr/bin/env python3
"""Consolidate skills — merge, deduplicate, and reorganize overlapping/redundant skills.

Usage:
    python consolidate_skills.py [--skills-dir PATH] [--output PATH] [--dry-run] [--report PATH]
"""

import argparse
import asyncio
import json
import shutil
import sys
from collections import defaultdict
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Consolidate overlapping Hermes skills")
    parser.add_argument("--skills-dir", default=None, help="Path to skills directory")
    parser.add_argument("--output", default=None, help="Output report path")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--report", default=None, help="Save consolidation report to file")
    return parser.parse_args(argv)


def _find_duplicates_by_name(skills_dir: Path) -> list[dict]:
    """Find skills with duplicate names across categories (CPU-bound)."""
    name_map: dict[str, list[dict]] = defaultdict(list)

    for skill_dir in skills_dir.iterdir():
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        name = skill_dir.name
        try:
            text = skill_md.read_text(encoding="utf-8")
        except Exception:
            text = ""

        is_categorized = "/" in str(skill_md.relative_to(skills_dir))
        entry = {
            "name": name,
            "path": str(skill_dir),
            "skill_md": str(skill_md),
            "is_categorized": is_categorized,
            "size": len(text),
        }
        name_map[name].append(entry)

    duplicates = []
    for name, entries in name_map.items():
        if len(entries) > 1:
            duplicates.append(
                {
                    "name": name,
                    "occurrences": entries,
                    "total": len(entries),
                }
            )
    return duplicates


async def find_duplicates_async(skills_dir: Path) -> list[dict]:
    """Find duplicates asynchronously."""
    return await asyncio.to_thread(_find_duplicates_by_name, skills_dir)


def _consolidate_duplicate(dup: dict, skills_dir: Path, dry_run: bool) -> dict:
    """Consolidate a set of duplicate skills (CPU-bound)."""
    entries = dup["occurrences"]
    name = dup["name"]

    # Prefer categorized entries as canonical
    categorized = [e for e in entries if e["is_categorized"]]
    flat = [e for e in entries if not e["is_categorized"]]

    if categorized:
        canonical = max(categorized, key=lambda e: e["size"])
        to_remove = [e for e in flat] + [e for e in categorized if e["path"] != canonical["path"]]
    else:
        canonical = max(entries, key=lambda e: e["size"])
        to_remove = [e for e in entries if e["path"] != canonical["path"]]

    results = []
    for entry in to_remove:
        entry_path = Path(entry["path"])
        if entry_path.exists():
            if not dry_run:
                shutil.rmtree(entry_path)
            results.append(
                {
                    "removed": str(entry_path),
                    "canonical": canonical["path"],
                    "name": name,
                }
            )

    return {
        "name": name,
        "canonical": canonical["path"],
        "removed": len(results),
        "details": results,
    }


async def consolidate_duplicate_async(dup: dict, skills_dir: Path, dry_run: bool) -> dict:
    """Consolidate duplicate asynchronously."""
    return await asyncio.to_thread(_consolidate_duplicate, dup, skills_dir, dry_run)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    skills_dir = Path(args.skills_dir or Path.home() / "AppData/Local/hermes/skills")

    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning for duplicate skills in {skills_dir}...")
    duplicates = await find_duplicates_async(skills_dir)

    print(f"Found {len(duplicates)} duplicate skill name(s)")
    for dup in duplicates:
        print(f"  {dup['name']}: {dup['total']} occurrences")

    if not duplicates:
        print("\nNo duplicates found. Nothing to consolidate.")
        if args.report:
            Path(args.report).write_text("[]", encoding="utf-8")
            print(f"\nReport written to {args.report}")
        return

    # Consolidate
    tasks = [consolidate_duplicate_async(d, skills_dir, args.dry_run) for d in duplicates]
    results = await asyncio.gather(*tasks)

    total_removed = sum(r["removed"] for r in results)
    mode = "DRY-RUN" if args.dry_run else "CONSOLIDATED"

    print(f"\n{mode}: {total_removed} duplicate skill copies removed")
    for r in results:
        if r["removed"] > 0:
            print(f"  '{r['name']}' kept: {r['canonical']}")
            for detail in r["details"]:
                print(f"    Removed: {detail['removed']}")

    if args.report:
        report_path = Path(args.report)
        report_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(f"\nReport written to {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
