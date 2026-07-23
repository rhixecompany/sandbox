#!/usr/bin/env python3
"""Build path mapping — build path-mapping index from Hermes skills for cross-referencing.

Usage:
    python build_path_mapping.py [--skills-dir PATH] [--output PATH] [--format json|md]
"""

import asyncio
import argparse
import json
import sys
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build path mapping from Hermes skills")
    parser.add_argument("--skills-dir", default=None, help="Path to skills directory")
    parser.add_argument("--output", default=None, help="Output path for mapping file")
    parser.add_argument("--format", choices=["json", "md"], default="json", help="Output format")
    return parser.parse_args(argv)


def _read_frontmatter_field(text: str, field: str) -> str | None:
    """Extract a YAML frontmatter field value from text (CPU-bound)."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    fm = parts[1]
    for line in fm.splitlines():
        if line.startswith(f"{field}:") or line.startswith(f"{field}: "):
            val = line.split(":", 1)[1].strip().strip('"').strip("'")
            return val if val else None
    return None


def _build_mapping(skills_dir: Path) -> dict:
    """Build mapping dict from skills directory (CPU-bound)."""
    mapping: dict[str, dict] = {}
    for skill_md in sorted(skills_dir.rglob("SKILL.md")):
        try:
            text = skill_md.read_text(encoding="utf-8")
        except Exception:
            continue

        name = skill_md.parent.name
        title = _read_frontmatter_field(text, "title") or name
        description = _read_frontmatter_field(text, "description") or ""
        tags_raw = _read_frontmatter_field(text, "tags") or ""
        tags = [t.strip() for t in tags_raw.replace("[", "").replace("]", "").split(",") if t.strip()]

        mapping[name] = {
            "name": name,
            "title": title,
            "description": description[:200],
            "path": str(skill_md),
            "dir": str(skill_md.parent),
            "tags": tags,
            "has_workflow": "## Workflow" in text,
            "has_pitfalls": "## Pitfalls" in text,
        }
    return mapping


async def build_mapping_async(skills_dir: Path) -> dict:
    """Build path mapping asynchronously."""
    return await asyncio.to_thread(_build_mapping, skills_dir)


def format_markdown(mapping: dict) -> str:
    """Format mapping as markdown table."""
    lines = [
        "# Hermes Skills Path Mapping",
        "",
        f"Total skills: {len(mapping)}",
        "",
        "| Name | Title | Path | Tags |",
        "|------|-------|------|------|",
    ]
    for name, info in sorted(mapping.items()):
        tags = ", ".join(info["tags"][:5]) if info["tags"] else "-"
        lines.append(f"| {name} | {info['title']} | {info['path']} | {tags} |")
    return "\n".join(lines)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    skills_dir = Path(args.skills_dir or Path.home() / "AppData/Local/hermes/skills")

    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Building path mapping from {skills_dir}...")
    mapping = await build_mapping_async(skills_dir)
    print(f"Found {len(mapping)} skills")

    if args.format == "json":
        output = json.dumps(mapping, indent=2, ensure_ascii=False)
    else:
        output = format_markdown(mapping)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(output, encoding="utf-8")
        print(f"Mapping written to {output_path}")
    else:
        print(output)


if __name__ == "__main__":
    asyncio.run(main())
