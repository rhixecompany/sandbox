#!/usr/bin/env python3
"""Dedupe skills — scan skills and identify duplicate or near-duplicate skills.

Usage:
    python dedupe_skills.py [--skills-dir PATH] [--output PATH] [--threshold FLOAT]
                            [--dry-run] [--report PATH]
"""

import asyncio
import argparse
import json
import sys
from pathlib import Path
from collections import defaultdict


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dedupe Hermes skills")
    parser.add_argument("--skills-dir", default=None, help="Path to skills directory")
    parser.add_argument("--output", default=None, help="Output path for dedupe report")
    parser.add_argument("--threshold", type=float, default=0.8,
                        help="Similarity threshold (0.0-1.0, default: 0.8)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without changes")
    parser.add_argument("--report", default=None, help="Save detailed report")
    return parser.parse_args(argv)


def _read_skill_text(skill_dir: Path) -> dict | None:
    """Read a skill's metadata from its SKILL.md (CPU-bound)."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None
    try:
        text = skill_md.read_text(encoding="utf-8")
    except Exception:
        return None

    name = skill_dir.name
    title = name
    description = ""
    tags: list[str] = []

    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            for line in fm.splitlines():
                if line.startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("description:"):
                    description = line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("tags:"):
                    rest = line[5:].strip()
                    if rest.startswith("["):
                        inner = rest.strip("[]").strip()
                        if inner:
                            tags = [t.strip().strip('"').strip("'") for t in inner.split(",")]

    return {
        "name": name,
        "title": title,
        "description": description,
        "tags": tags,
        "path": str(skill_dir),
        "text_length": len(text),
    }


def _compute_similarity(a: dict, b: dict) -> float:
    """Compute similarity between two skills (CPU-bound)."""
    score = 0.0
    total = 0

    # Name similarity (exact or close)
    if a["name"].lower() == b["name"].lower():
        score += 3
    elif a["name"].lower() in b["name"].lower() or b["name"].lower() in a["name"].lower():
        score += 2
    total += 3

    # Title similarity
    if a["title"].lower() == b["title"].lower():
        score += 2
    total += 2

    # Tag overlap
    a_tags = set(t.lower() for t in a["tags"])
    b_tags = set(t.lower() for t in b["tags"])
    if a_tags and b_tags:
        overlap = len(a_tags & b_tags)
        score += overlap / max(len(a_tags | b_tags), 1) * 2
    total += 2

    # Description similarity (word overlap)
    a_words = set(a["description"].lower().split())
    b_words = set(b["description"].lower().split())
    if a_words and b_words:
        overlap = len(a_words & b_words)
        score += overlap / max(len(a_words | b_words), 1) * 3
    total += 3

    return score / total if total > 0 else 0


def _scan_and_find_duplicates(skills_dir: Path, threshold: float) -> list[dict]:
    """Scan skills and find duplicates (CPU-bound)."""
    skills: list[dict] = []
    for skill_dir in sorted(skills_dir.iterdir()):
        if skill_dir.is_dir():
            info = _read_skill_text(skill_dir)
            if info:
                skills.append(info)

    duplicates = []
    checked: set[str] = set()

    for i, a in enumerate(skills):
        if a["name"] in checked:
            continue
        for j, b in enumerate(skills):
            if i >= j or b["name"] in checked:
                continue
            sim = _compute_similarity(a, b)
            if sim >= threshold:
                duplicates.append({
                    "skill_a": a["name"],
                    "skill_a_path": a["path"],
                    "skill_b": b["name"],
                    "skill_b_path": b["path"],
                    "similarity": round(sim, 3),
                    "name_match": a["name"].lower() == b["name"].lower(),
                    "exact_copy": a["text_length"] == b["text_length"],
                })
                checked.add(b["name"])
        checked.add(a["name"])

    return duplicates


async def scan_and_find_duplicates_async(skills_dir: Path, threshold: float) -> list[dict]:
    """Find duplicates asynchronously."""
    return await asyncio.to_thread(_scan_and_find_duplicates, skills_dir, threshold)


def format_report(duplicates: list[dict]) -> str:
    """Generate markdown dedupe report."""
    lines = [
        "# Skill Deduplication Report",
        "",
        f"Total duplicate pairs found: {len(duplicates)}",
        "",
        "| Skill A | Skill B | Similarity | Name Match | Exact Copy |",
        "|---------|---------|-----------|-----------|-----------|",
    ]
    for d in sorted(duplicates, key=lambda x: x["similarity"], reverse=True):
        name_match = "✅" if d["name_match"] else "❌"
        exact_copy = "✅" if d["exact_copy"] else "❌"
        lines.append(f"| {d['skill_a']} | {d['skill_b']} | {d['similarity']:.1%} | {name_match} | {exact_copy} |")

    # Group by category
    name_dupes = [d for d in duplicates if d["name_match"]]
    fuzzy_dupes = [d for d in duplicates if not d["name_match"]]

    if name_dupes:
        lines.extend(["", "## Name Duplicates (exact name match)", ""])
        for d in name_dupes:
            lines.append(f"- `{d['skill_a']}` → {d['skill_a_path']}")
            lines.append(f"- `{d['skill_b']}` → {d['skill_b_path']}")
            lines.append("")

    if fuzzy_dupes:
        lines.extend(["", "## Fuzzy Duplicates (similar but different names)", ""])
        for d in fuzzy_dupes:
            lines.append(f"- `{d['skill_a']}` ↔ `{d['skill_b']}` (similarity: {d['similarity']:.1%})")
            lines.append("")

    return "\n".join(lines)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    skills_dir = Path(args.skills_dir or Path.home() / "AppData/Local/hermes/skills")

    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning for duplicates in {skills_dir} (threshold={args.threshold})...")
    duplicates = await scan_and_find_duplicates_async(skills_dir, args.threshold)

    print(f"Found {len(duplicates)} duplicate pair(s)")

    if duplicates:
        report = format_report(duplicates)
        print(report[:1500])
        if len(report) > 1500:
            print(f"... ({len(report) - 1500} more chars)")
    else:
        print("No duplicates found above threshold.")
        report = "# Skill Deduplication Report\n\nTotal duplicate pairs found: 0\n"

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"\nReport written to {args.output}")


if __name__ == "__main__":
    asyncio.run(main())
