#!/usr/bin/env python3
"""Trim Research Reports — Remove research report content sections.

Async CLI for cleaning RESEARCH_REPORT.md sections from markdown files.
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path

# Headings identifying research report sections
REPORT_SECTION_PATTERNS: list[str] = [
    r"^##\s+Research\s+Report",
    r"^##\s+Research\s+Overview",
    r"^##\s+Methodology",
    r"^##\s+Literature\s+Review",
    r"^##\s+Findings?\b",
    r"^##\s+Analysis\s+of\s+Results",
    r"^##\s+Discussion\b",
    r"^##\s+Conclusion\s*(?:and\s+Future\s+Work)?",
    r"^##\s+References?\b",
    r"^##\s+Bibliography",
]


async def trim_report_sections(file_path: Path, dry_run: bool = False) -> dict:
    """Remove research report sections from a markdown file."""
    try:
        content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception as exc:
        return {"file": str(file_path), "error": str(exc), "trimmed": False}

    lines = content.splitlines()
    sections: list[tuple[int, int]] = []
    start_idx = None

    for i, line in enumerate(lines):
        if any(re.match(p, line) for p in REPORT_SECTION_PATTERNS):
            start_idx = i
        elif start_idx is not None and line.startswith("## ") and i > start_idx:
            sections.append((start_idx, i))
            start_idx = None

    if start_idx is not None:
        sections.append((start_idx, len(lines)))

    if not sections:
        return {"file": str(file_path), "trimmed": False, "sections_removed": 0}

    trimmed = list(lines)
    removed_lines = 0
    removed_headings = []
    for start, end in reversed(sections):
        removed_headings.append(lines[start].strip())
        del trimmed[start:end]
        removed_lines += end - start

    new_content = "\n".join(trimmed)
    if new_content == content:
        return {"file": str(file_path), "trimmed": False, "sections_removed": 0}

    if not dry_run:
        await asyncio.to_thread(file_path.write_text, new_content, encoding="utf-8")

    return {
        "file": str(file_path),
        "trimmed": True,
        "sections_removed": len(sections),
        "lines_removed": removed_lines,
        "headings": removed_headings,
        "dry_run": dry_run,
    }


async def main() -> None:
    parser = argparse.ArgumentParser(description="Remove research report sections from markdown files.")
    parser.add_argument(
        "--workspace",
        type=str,
        default=".",
        help="Root directory (default: .)",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default="**/*.md",
        help="File glob (default: **/*.md)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without modifying files",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    files = list(workspace.glob(args.pattern))
    if not files:
        print(f"No files matching {args.pattern} in {workspace}", file=sys.stderr)
        sys.exit(1)

    results = await asyncio.gather(*(trim_report_sections(f, dry_run=args.dry_run) for f in files))

    trimmed = [r for r in results if r.get("trimmed")]
    total_removed = sum(r.get("sections_removed", 0) for r in trimmed)

    print("\n=== Trim Research Reports ===")
    print(f"Scanned {len(files)} file(s)")
    print(f"Modified: {len(trimmed)} file(s)")
    print(f"Total research sections removed: {total_removed}")
    if args.dry_run:
        print("(dry-run — no files were modified)")
    for r in trimmed:
        print(f"  {r['file']}: {r['sections_removed']} section(s), {r['lines_removed']} line(s)")
        for h in r.get("headings", []):
            print(f"    - {h}")
    for r in results:
        if r.get("error"):
            print(f"  ERROR: {r['file']}: {r['error']}", file=sys.stderr)

    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
