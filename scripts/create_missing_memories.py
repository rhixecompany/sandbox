#!/usr/bin/env python3
"""Create missing memories — scan Hermes profiles and create missing USER.md, MEMORY.md files.

Usage:
    python create_missing_memories.py [--profiles-dir PATH] [--dry-run] [--verbose]
"""

import argparse
import asyncio
import sys
from pathlib import Path

USER_TEMPLATE = """# User Profile

## About

<!-- Describe yourself, your background, and your relationship with Hermes -->

## Preferences

- Preferred communication style:
- Expertise areas:
- Goals with Hermes:

## Communication

- How you like to receive information:
- Feedback preferences:
"""

MEMORY_TEMPLATE = """# Session Memory

## Key Points

<!-- Record important facts, decisions, and context from sessions -->

## Active Context

<!-- Current projects, tasks, and their status -->

## Learned Patterns

<!-- Recurring behaviors, preferences, and approaches discovered over time -->
"""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create missing Hermes profile memory files")
    parser.add_argument("--profiles-dir", default=None, help="Path to Hermes profiles directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview without creating files")
    parser.add_argument("--verbose", action="store_true", help="Detailed output")
    return parser.parse_args(argv)


def find_profiles(profiles_dir: Path) -> list[Path]:
    """Find all Hermes profile directories."""
    if not profiles_dir.is_dir():
        print(f"ERROR: profiles directory not found: {profiles_dir}", file=sys.stderr)
        sys.exit(1)
    return sorted([d for d in profiles_dir.iterdir() if d.is_dir()])


def check_missing_files(profile_dir: Path) -> list[str]:
    """Check which memory files are missing from a profile (CPU-bound)."""
    required = ["USER.md", "MEMORY.md"]
    return [f for f in required if not (profile_dir / f).exists()]


async def create_file_async(path: Path, content: str, dry_run: bool) -> bool:
    """Create a file with given content asynchronously."""
    if dry_run:
        return True
    await asyncio.to_thread(path.write_text, content, encoding="utf-8")
    return True


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    profiles_dir = Path(args.profiles_dir or Path.home() / "AppData/Local/hermes/profiles")

    profiles = find_profiles(profiles_dir)
    print(f"Found {len(profiles)} profile(s)")

    all_created = 0
    tasks = []

    for profile_dir in profiles:
        profile_name = profile_dir.name
        missing = check_missing_files(profile_dir)

        if not missing:
            if args.verbose:
                print(f"  {profile_name}: all files present")
            continue

        if args.verbose:
            print(f"  {profile_name}: missing {missing}")

        for filename in missing:
            content = USER_TEMPLATE if filename == "USER.md" else MEMORY_TEMPLATE
            filepath = profile_dir / filename
            tasks.append((profile_name, filename, filepath, content))
            all_created += 1

    if not tasks:
        print("All profiles have required memory files. Nothing to create.")
        return

    print(f"\nCreating {all_created} missing file(s)...")

    created = 0
    for profile_name, filename, filepath, content in tasks:
        success = await create_file_async(filepath, content, args.dry_run)
        if success:
            created += 1
            marker = "[DRY-RUN]" if args.dry_run else "[CREATED]"
            print(f"  {marker} {profile_name}/{filename}")

    mode = "would be created" if args.dry_run else "created"
    print(f"\n{created} file(s) {mode}")


if __name__ == "__main__":
    asyncio.run(main())
