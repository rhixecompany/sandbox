#!/usr/bin/env python3
"""Create missing souls — create missing SOUL.md personality files for Hermes profiles.

Usage:
    python create_missing_souls.py [--profiles-dir PATH] [--dry-run] [--verbose]
"""

import argparse
import asyncio
import sys
from pathlib import Path

SOUL_TEMPLATE = """# SOUL.md — Agent Personality

## Identity

**Name:** {profile_name}
**Role:** AI Assistant
**Version:** 1.0.0

## Personality Traits

- Helpful and knowledgeable
- Clear and direct communicator
- Adaptable to user preferences

## Core Directives

1. Always prioritize the user's goals
2. Be honest about limitations
3. Learn from interactions

## Voice and Tone

- Professional but approachable
- Concise when possible, detailed when needed
- Use appropriate technical language

## Behavioral Patterns

- Proactively suggest improvements
- Verify assumptions before acting
- Admit uncertainty when appropriate

---

*This personality definition was auto-generated. Customize it to better match your preferences.*
"""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create missing SOUL.md files for profiles")
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


async def create_soul_file_async(path: Path, content: str, dry_run: bool) -> bool:
    """Create SOUL.md file asynchronously."""
    if dry_run:
        return True
    await asyncio.to_thread(path.write_text, content, encoding="utf-8")
    return True


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    profiles_dir = Path(args.profiles_dir or Path.home() / "AppData/Local/hermes/profiles")

    profiles = find_profiles(profiles_dir)
    print(f"Found {len(profiles)} profile(s)")

    created = 0
    for profile_dir in profiles:
        profile_name = profile_dir.name
        soul_path = profile_dir / "SOUL.md"

        if soul_path.exists():
            if args.verbose:
                print(f"  {profile_name}/SOUL.md: already exists")
            continue

        content = SOUL_TEMPLATE.format(profile_name=profile_name)
        success = await create_soul_file_async(soul_path, content, args.dry_run)
        if success:
            created += 1
            marker = "[DRY-RUN]" if args.dry_run else "[CREATED]"
            print(f"  {marker} {profile_name}/SOUL.md")

    mode = "would be created" if args.dry_run else "created"
    print(f"\n{created} SOUL.md file(s) {mode}")


if __name__ == "__main__":
    asyncio.run(main())
