#!/usr/bin/env python3
"""Validate Prompt Inventory — Render inventory of all prompts.

Async CLI that scans prompt files and generates a Markdown inventory
with name, title, version, tags, and duplicate detection.
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path
from typing import Any


def parse_frontmatter_basic(content: str) -> dict[str, Any]:
    """Extract basic frontmatter fields. CPU-bound, purely local."""
    fields: dict[str, Any] = {}
    if not content.startswith("---"):
        return fields
    end = content.find("---", 3)
    if end == -1:
        return fields
    fm = content[3:end]
    for match in re.finditer(r"^(\w+)\s*:\s*(.+)$", fm, re.MULTILINE):
        key = match.group(1)
        val = match.group(2).strip().strip('"').strip("'")
        fields[key] = val
    return fields


async def parse_prompt_file(file_path: Path) -> dict[str, Any] | None:
    """Parse a .prompt.md file and extract frontmatter. I/O offloaded."""
    try:
        content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception:
        return None

    fm = parse_frontmatter_basic(content)
    if not fm:
        return None

    return {
        "path": str(file_path),
        "name": fm.get("name", file_path.stem),
        "title": fm.get("title", ""),
        "version": fm.get("version", ""),
        "tags": fm.get("tags", ""),
        "author": fm.get("author", ""),
    }


async def main() -> None:
    parser = argparse.ArgumentParser(description="Render a Markdown inventory of all prompts.")
    parser.add_argument(
        "--workspace",
        type=str,
        default=".",
        help="Root directory (default: .)",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default="**/*.prompt.md",
        help="File glob (default: **/*.prompt.md)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file (default: stdout)",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    files = list(workspace.glob(args.pattern))
    if not files:
        print(f"No prompt files matching {args.pattern} in {workspace}", file=sys.stderr)
        sys.exit(1)

    prompts = await asyncio.gather(*(parse_prompt_file(f) for f in files))
    valid = [p for p in prompts if p is not None]

    # Detect name duplicates (CPU-bound)
    seen: dict[str, list[dict[str, Any]]] = {}
    for p in valid:
        seen.setdefault(p["name"], []).append(p)

    duplicates = {k: v for k, v in seen.items() if len(v) > 1}

    # Build markdown report
    lines = [
        "# Prompt Inventory",
        "",
        f"**Total prompt files found:** {len(files)}",
        f"**Valid prompt files (with frontmatter):** {len(valid)}",
        f"**Duplicate names:** {len(duplicates)}",
        "",
        "---",
        "",
        "## Valid Prompts",
        "",
        "| # | Name | Title | Version | Tags | Author |",
        "|---|------|-------|---------|------|--------|",
    ]

    for idx, p in enumerate(valid, 1):
        lines.append(f"| {idx} | {p['name']} | {p['title']} | {p['version']} | {p['tags']} | {p['author']} |")

    if duplicates:
        lines.extend(["", "---", "", "## Duplicate Names", ""])
        for name, entries in duplicates.items():
            paths = [e["path"] for e in entries]
            lines.append(f"- **{name}** — {len(entries)} files:")
            for p in paths:
                lines.append(f"  - {p}")

    report = "\n".join(lines) + "\n"

    if args.output:
        await asyncio.to_thread(Path(args.output).write_text, report, encoding="utf-8")
    else:
        print(report)

    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
