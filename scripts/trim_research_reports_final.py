#!/usr/bin/env python3
"""Trim Research Reports Final — Final aggressive trim pass.

Async CLI for a tighter trim pass targeting RESEARCH_REPORT.md files
with stricter line limits and additional patterns.
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path

# Aggressive patterns for the final trim pass
FINAL_PATTERNS: list[str] = [
    r"^##\s+Research\s+Report",
    r"^##\s+Research\s+Overview",
    r"^##\s+Methodology",
    r"^##\s+Literature\s+Review",
    r"^##\s+Findings?\b",
    r"^##\s+Analysis\s+of\s+Results",
    r"^##\s+Discussion\b",
    r"^##\s+Conclusion\b",
    r"^##\s+References?\b",
    r"^##\s+Bibliography",
    r"^##\s+Appendix\b",
    r"^##\s+Limitations",
    r"^##\s+Future\s+Work",
    r"^##\s+Related\s+Work",
    r"^##\s+Data\s+(?:Collection|Analysis|Sources)",
    r"^##\s+Experimental\s+Setup",
    r"^##\s+Results\s+and\s+Discussion",
]

MAX_LINE_COUNT = 300  # Hard cap on remaining lines


async def final_trim(file_path: Path, max_lines: int = 300, dry_run: bool = False) -> dict:
    """Aggressively trim research report files, then cap line count."""
    try:
        content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception as exc:
        return {"file": str(file_path), "error": str(exc), "trimmed": False}

    lines = content.splitlines()

    # First pass: remove matching sections
    sections: list[tuple[int, int]] = []
    start_idx = None
    for i, line in enumerate(lines):
        if any(re.match(p, line) for p in FINAL_PATTERNS):
            start_idx = i
        elif start_idx is not None and line.startswith("## ") and i > start_idx:
            sections.append((start_idx, i))
            start_idx = None
    if start_idx is not None:
        sections.append((start_idx, len(lines)))

    trimmed = list(lines)
    removed_lines = 0
    for start, end in reversed(sections):
        del trimmed[start:end]
        removed_lines += end - start

    # Second pass: cap total lines if still over limit
    if len(trimmed) > max_lines:
        trimmed = trimmed[:max_lines]
        trimmed.append("")
        trimmed.append("<!-- Content truncated by final trim pass -->")

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
        "lines_after_trim": len(trimmed),
        "dry_run": dry_run,
    }


async def main() -> None:
    parser = argparse.ArgumentParser(description="Final aggressive trim pass for research report files.")
    parser.add_argument(
        "--workspace",
        type=str,
        default=".",
        help="Root directory (default: .)",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default="**/RESEARCH_REPORT*.md",
        help="File glob (default: **/RESEARCH_REPORT*.md)",
    )
    parser.add_argument(
        "--max-lines",
        type=int,
        default=None,
        help="Hard line cap (default: 300)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without modifying files",
    )
    args = parser.parse_args()

    max_line_count = args.max_lines if args.max_lines else MAX_LINE_COUNT

    workspace = Path(args.workspace).resolve()
    files = list(workspace.glob(args.pattern))
    if not files:
        print(f"No files matching {args.pattern} in {workspace}", file=sys.stderr)
        sys.exit(1)

    results = await asyncio.gather(*(final_trim(f, max_lines=max_line_count, dry_run=args.dry_run) for f in files))

    trimmed = [r for r in results if r.get("trimmed")]
    total_removed = sum(r.get("sections_removed", 0) for r in trimmed)

    print("\n=== Final Research Report Trim ===")
    print(f"Scanned {len(files)} file(s)")
    print(f"Modified: {len(trimmed)} file(s)")
    print(f"Total sections removed: {total_removed}")
    if args.dry_run:
        print("(dry-run — no files were modified)")
    for r in trimmed:
        lines_after = r.get("lines_after_trim", "?")
        print(f"  {r['file']}: {r['sections_removed']} section(s), {r['lines_removed']} line(s) → {lines_after} lines")
    for r in results:
        if r.get("error"):
            print(f"  ERROR: {r['file']}: {r['error']}", file=sys.stderr)

    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
