#!/usr/bin/env python3
"""Update AGENTS.md — Add Architecture sections to AGENTS.md files.

Async CLI for scanning projects and injecting architecture blueprints,
folder structures, and tech stacks into AGENTS.md files.
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path

ARCHITECTURE_BOILERPLATE = """## Architecture

### Technology Stack
<!-- Auto-populated tech stack will go here -->

### Folder Structure
<!-- Auto-populated folder structure will go here -->

### Architecture Overview
<!-- Project architecture description -->

### Key Components
- _Component 1_: description
- _Component 2_: description

### Data Flow
<!-- Data flow description -->
"""


async def read_file_safe(file_path: Path) -> str | None:
    """Read file content safely via thread."""
    try:
        return await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception:
        return None


async def write_file_safe(file_path: Path, content: str) -> bool:
    """Write file content safely via thread."""
    try:
        await asyncio.to_thread(file_path.write_text, content, encoding="utf-8")
        return True
    except Exception:
        return False


async def find_agents_md_files(workspace: Path) -> list[Path]:
    """Find all AGENTS.md files in workspace."""
    return list(workspace.rglob("AGENTS.md"))


async def add_architecture_section(file_path: Path, dry_run: bool = False) -> dict:
    """Add the Architecture section to an AGENTS.md file if missing."""
    content = await read_file_safe(file_path)
    if content is None:
        return {"file": str(file_path), "error": "Cannot read file", "updated": False}

    # Check if Architecture section already exists
    if re.search(r"^##\s+Architecture", content, re.MULTILINE):
        return {"file": str(file_path), "updated": False, "reason": "Already has Architecture section"}

    # Append architecture section
    new_content = content.rstrip() + "\n\n" + ARCHITECTURE_BOILERPLATE + "\n"

    if not dry_run and not await write_file_safe(file_path, new_content):
        return {"file": str(file_path), "error": "Cannot write file", "updated": False}

    return {"file": str(file_path), "updated": True, "dry_run": dry_run}


async def main() -> None:
    parser = argparse.ArgumentParser(description="Add Architecture sections to AGENTS.md files.")
    parser.add_argument(
        "--workspace",
        type=str,
        default=".",
        help="Root directory (default: .)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    agents_files = await find_agents_md_files(workspace)

    if not agents_files:
        print(f"No AGENTS.md files found in {workspace}", file=sys.stderr)
        sys.exit(1)

    results = await asyncio.gather(*(add_architecture_section(f, dry_run=args.dry_run) for f in agents_files))

    updated = [r for r in results if r.get("updated")]
    skipped = [r for r in results if not r.get("updated") and not r.get("error")]
    errors = [r for r in results if r.get("error")]

    print("\n=== Update AGENTS.md Report ===")
    print(f"Found {len(agents_files)} AGENTS.md file(s)")
    print(f"Updated: {len(updated)}")
    print(f"Skipped (already has section): {len(skipped)}")
    print(f"Errors: {len(errors)}")
    if args.dry_run:
        print("(dry-run — no files were modified)")
    for r in updated:
        print(f"  + {r['file']}")
    for r in skipped:
        print(f"  = {r['file']} ({r.get('reason', 'skipped')})")
    for r in errors:
        print(f"  ! {r['file']}: {r['error']}")

    sys.exit(0 if len(errors) == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
