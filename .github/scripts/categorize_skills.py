#!/usr/bin/env python3
"""Categorize skills — scan skill directories and categorize by domain, tags, and usage patterns.

Usage:
    python categorize_skills.py [--skills-dir PATH] [--output PATH] [--format json|csv|md]
"""

import argparse
import asyncio
import json
import sys
from collections import defaultdict
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Categorize Hermes skills")
    parser.add_argument("--skills-dir", default=None, help="Path to skills directory")
    parser.add_argument("--output", default=None, help="Output path")
    parser.add_argument("--format", choices=["json", "csv", "md"], default="md", help="Output format")
    return parser.parse_args(argv)


def _parse_tags(fm_text: str) -> list[str]:
    """Extract tags from YAML frontmatter (CPU-bound)."""
    tags: list[str] = []
    in_tags = False
    for line in fm_text.splitlines():
        if line.startswith("tags:"):
            rest = line[5:].strip()
            if rest.startswith("["):
                # Inline list: [tag1, tag2]
                inner = rest.strip("[]").strip()
                if inner:
                    tags = [t.strip().strip('"').strip("'") for t in inner.split(",")]
                in_tags = False
            elif not rest:
                in_tags = True
            else:
                tags = [rest]
                in_tags = False
        elif in_tags and line.strip().startswith("- "):
            tags.append(line.strip()[2:].strip())
        elif (in_tags and not line.strip()) or (in_tags and not line.strip().startswith("- ")):
            in_tags = False
    return tags


def _categorize_skills(skills_dir: Path) -> dict:
    """Scan all skills and build categories (CPU-bound)."""
    categories: dict[str, list[dict]] = defaultdict(list)

    for skill_md in sorted(skills_dir.rglob("SKILL.md")):
        try:
            text = skill_md.read_text(encoding="utf-8")
        except Exception:
            continue

        name = skill_md.parent.name
        # Extract frontmatter
        if not text.startswith("---"):
            categories["uncategorized"].append({"name": name, "path": str(skill_md)})
            continue

        parts = text.split("---", 2)
        if len(parts) < 3:
            categories["uncategorized"].append({"name": name, "path": str(skill_md)})
            continue

        fm = parts[1]
        tags = _parse_tags(fm)

        # Get title and description
        title = ""
        desc = ""
        for line in fm.splitlines():
            if line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("description:"):
                desc = line.split(":", 1)[1].strip().strip('"').strip("'")

        entry = {
            "name": name,
            "title": title or name,
            "description": desc[:150] if desc else "",
            "path": str(skill_md),
            "tags": tags,
        }

        # Determine primary category from tags or directory path
        primary_cat = None
        for tag in tags:
            tag_lower = tag.lower().replace(" ", "-")
            if tag_lower in [
                "development",
                "devops",
                "mlops",
                "security",
                "research",
                "creative",
                "productivity",
                "gaming",
                "qa",
                "finance",
                "data-science",
                "reference",
            ]:
                primary_cat = tag_lower
                break

        if primary_cat:
            categories[primary_cat].append(entry)
        elif len(tags) > 0:
            categories[tags[0].lower().replace(" ", "-")].append(entry)
        else:
            categories["uncategorized"].append(entry)

    return dict(categories)


async def categorize_skills_async(skills_dir: Path) -> dict:
    """Categorize skills asynchronously."""
    return await asyncio.to_thread(_categorize_skills, skills_dir)


def format_markdown(categories: dict) -> str:
    """Format categories as markdown."""
    lines = ["# Hermes Skills by Category", "", f"Total categories: {len(categories)}", ""]
    for cat_name in sorted(categories.keys()):
        skills = categories[cat_name]
        lines.append(f"## {cat_name.title()} ({len(skills)})")
        lines.append("")
        for s in sorted(skills, key=lambda x: x["name"]):
            tags = ", ".join(s["tags"][:5]) if s["tags"] else "-"
            lines.append(f"- **{s['name']}** — {s['description'][:100]}")
            lines.append(f"  Tags: {tags}")
        lines.append("")
    return "\n".join(lines)


def format_csv(categories: dict) -> str:
    """Format categories as CSV."""
    lines = ["category,name,title,description,tags,path"]
    for cat_name in sorted(categories.keys()):
        for s in sorted(categories[cat_name], key=lambda x: x["name"]):
            tags = "; ".join(s["tags"]) if s["tags"] else ""
            lines.append(f'{cat_name},{s["name"]},"{s["title"]}","{s["description"]}","{tags}",{s["path"]}')
    return "\n".join(lines)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    skills_dir = Path(args.skills_dir or Path.home() / "AppData/Local/hermes/skills")

    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Categorizing skills from {skills_dir}...")
    categories = await categorize_skills_async(skills_dir)

    total = sum(len(v) for v in categories.values())
    print(f"Found {total} skills across {len(categories)} categories")

    output = ""
    if args.format == "md":
        output = format_markdown(categories)
    elif args.format == "csv":
        output = format_csv(categories)
    elif args.format == "json":
        output = json.dumps(categories, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"\nOutput written to {args.output}")
    else:
        print(output[:2000])  # Show preview
        if len(output) > 2000:
            print(f"... ({len(output) - 2000} more chars)")


if __name__ == "__main__":
    asyncio.run(main())
