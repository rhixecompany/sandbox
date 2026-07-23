#!/usr/bin/env python3
"""Fix Copilot frontmatter — fix YAML frontmatter in GitHub Copilot skill files.

Usage:
    python fix_copilot_frontmatter.py [--skills-dir PATH] [--dry-run] [--verbose] [--report PATH]
"""

import asyncio
import argparse
import re
import sys
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fix Copilot frontmatter in skill files")
    parser.add_argument("--skills-dir", default=None, help="Path to skills directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--verbose", action="store_true", help="Detailed output")
    parser.add_argument("--report", default=None, help="Save fix report to file")
    return parser.parse_args(argv)


COPIOP_FIXES = [
    # agent: → remove (Copilot-specific)
    (r"^agent:\s*.*\n?", "", "Remove 'agent:' field"),
    # model: → remove (Copilot-specific)
    (r"^model:\s*.*\n?", "", "Remove 'model:' field"),
    # tools: → toolsets:
    (r"^tools:\s*", "toolsets: ", "Rename 'tools:' to 'toolsets:'"),
    # Convert Python-style tags [...] to YAML list
    (r"^tags:\s*\[([^\]]*)\]", lambda m: _convert_tags(m.group(1)), "Fix tags format"),
    # Add missing --- at start
    (r"^(?!---)", "---\n", "Add YAML frontmatter opener"),
]


def _convert_tags(tag_str: str) -> str:
    """Convert Python-style tag list to YAML list."""
    tags = [t.strip().strip('"').strip("'") for t in tag_str.split(",")]
    tags = [t for t in tags if t]
    if not tags:
        return "tags: []"
    result = "tags:\n"
    for t in tags:
        result += f"  - {t}\n"
    return result.rstrip()


REQUIRED_FIELDS = ["name", "title", "description", "version", "author", "license", "tags"]


def _fix_file(filepath: Path, dry_run: bool) -> dict:
    """Fix frontmatter in a single file (CPU-bound)."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return {"file": str(filepath), "status": "error", "error": str(e), "fixes": []}

    original = text
    fixes: list[str] = []

    # Ensure YAML frontmatter exists
    if not text.startswith("---"):
        text = "---\n" + text
        fixes.append("ADD_FRONTMATTER_OPENER")

    # Split frontmatter and body
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {"file": str(filepath), "status": "error",
                "error": "Cannot parse frontmatter", "fixes": fixes}

    fm_text = parts[1]
    body = parts[2]
    fm_lines = fm_text.splitlines()

    # Remove Copilot-specific fields
    new_fm_lines = []
    removed_fields = []
    for line in fm_lines:
        field = line.split(":")[0].strip() if ":" in line else ""
        if field in ("agent", "model"):
            removed_fields.append(field)
            continue
        # Fix tags: [...] format
        if field == "tags" and "[" in line:
            m = re.match(r"tags:\s*\[([^\]]*)\]", line)
            if m:
                tags = [t.strip().strip('"').strip("'") for t in m.group(1).split(",") if t.strip()]
                if tags:
                    new_fm_lines.append("tags:")
                    for t in tags:
                        new_fm_lines.append(f"  - {t}")
                else:
                    new_fm_lines.append("tags: []")
                fixes.append("FIX_TAGS_FORMAT")
                continue
        # Fix tools: → toolsets:
        if field == "tools":
            val = line.split(":", 1)[1].strip() if ":" in line else ""
            new_fm_lines.append(f"toolsets: {val}")
            fixes.append("CONVERT_TOOLS_TO_TOOLSETS")
            continue
        new_fm_lines.append(line)

    if removed_fields:
        fixes.append(f"REMOVED_{'_'.join(f.upper() for f in removed_fields)}")

    # Add missing required fields
    existing_fields = set()
    for line in new_fm_lines:
        if ":" in line:
            existing_fields.add(line.split(":")[0].strip())

    name = filepath.parent.name
    for field in REQUIRED_FIELDS:
        if field not in existing_fields and field not in ("tags",):
            default = name if field == "name" else name.replace("-", " ").title() if field == "title" else "1.0.0" if field == "version" else "Hermes Agent" if field == "author" else "MIT" if field == "license" else ""
            new_fm_lines.insert(0, f"{field}: {default}")
            fixes.append(f"ADD_{field.upper()}")
        elif field == "tags" and field not in existing_fields:
            new_fm_lines.append("tags: []")
            fixes.append("ADD_TAGS")

    # Rebuild
    new_fm = "\n".join(new_fm_lines)
    new_text = f"---\n{new_fm}\n---\n{body.lstrip()}"

    if new_text == original or not fixes:
        return {"file": str(filepath), "status": "unchanged", "fixes": []}

    if not dry_run:
        filepath.write_text(new_text, encoding="utf-8")

    return {"file": str(filepath), "status": "fixed", "fixes": fixes}


async def fix_file_async(filepath: Path, dry_run: bool) -> dict:
    """Fix a single file asynchronously."""
    return await asyncio.to_thread(_fix_file, filepath, dry_run)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    skills_dir = Path(args.skills_dir or Path.home() / "AppData/Local/hermes/skills")

    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    skill_md_files = sorted(skills_dir.rglob("SKILL.md"))
    print(f"Scanning {len(skill_md_files)} SKILL.md files in {skills_dir}...")

    tasks = [fix_file_async(f, args.dry_run) for f in skill_md_files]
    results = await asyncio.gather(*tasks)

    fixed = [r for r in results if r["status"] == "fixed"]
    unchanged = [r for r in results if r["status"] == "unchanged"]
    errors = [r for r in results if r["status"] == "error"]

    mode = "DRY-RUN" if args.dry_run else "APPLIED"
    print(f"\n{mode}: {len(fixed)} fixed, {len(unchanged)} unchanged, {len(errors)} errors")

    if args.verbose:
        for r in fixed:
            print(f"  {r['file']}: {', '.join(r['fixes'])}")
        for r in errors:
            print(f"  ERROR: {r['file']}: {r.get('error', '')}")

    if args.report:
        report_path = Path(args.report)
        import json
        report_path.write_text(
            json.dumps({"fixed": fixed, "errors": errors, "dry_run": args.dry_run}, indent=2),
            encoding="utf-8",
        )
        print(f"\nReport written to {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
