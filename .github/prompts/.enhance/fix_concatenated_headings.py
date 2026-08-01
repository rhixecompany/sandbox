#!/usr/bin/env python3
"""Fix MALFORMED_HEADINGS: split concatenated heading lines into proper multi-line sections.

Two-pass approach:
1. Split at ## (level-2) headings — with negative lookbehind to avoid ### matches
2. Within each part, split at ### (level-3) headings
3. Handle # (level-1) headings concatenated with ##

This ensures proper markdown: each heading on its own line with blank line separators.
"""

import re
import sys
from pathlib import Path

import yaml

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")


def fix_concatenated_headings(body):
    """Split concatenated headings into proper multi-line format."""
    lines = body.split("\n")
    new_lines = []
    changed = False

    for line in lines:
        # Pass 1: Check if this line has concatenated headings
        if not re.search(r"#{1,3}[^#\n]+#{2,3}\s", line):
            new_lines.append(line)
            continue

        changed = True
        # Pass 2: Split at ## level-2 headings (avoid splitting ### into # + ##)
        parts_l2 = re.split(r"(?<!#)(?=##\s)", line)

        # Pass 3: Within each L2 part, split at ### level-3 headings
        all_parts = []
        for part in parts_l2:
            if not part.strip():
                continue
            # Split at ### headings
            sub = re.split(r"(?=###\s)", part)
            all_parts.extend(sub)

        # Pass 4: Handle # level-1 headings concatenated with ##
        final_parts = []
        for part in all_parts:
            if not part.strip():
                continue
            # Check if this part has # h1 followed by ## h2 without blank line
            if re.match(r"^#\s(?!$)", part) and not part.startswith("##"):
                # # h1 title followed by content then ##
                sub = re.split(r"(?=##\s)", part)
                final_parts.extend([s.strip() for s in sub if s.strip()])
            else:
                final_parts.append(part.strip())

        # Write output with blank line separators between sections
        for i, part in enumerate(final_parts):
            if part:
                new_lines.append(part)
                if i < len(final_parts) - 1:
                    new_lines.append("")

    if changed:
        return "\n".join(new_lines)
    return body


def ensure_blank_lines_between_sections(body):
    """Ensure blank lines between ## section headings on adjacent lines."""
    # ## heading immediately followed by another ## or ### heading (no blank line)
    pattern = r"(## .+)\n(## |### )"
    body = re.sub(pattern, r"\1\n\n\2", body)
    return body


def fix_description_no_period(frontmatter, yaml_content, _name):
    """Fix description missing trailing period in frontmatter."""
    try:
        fm = yaml.safe_load(yaml_content)
        if fm and "description" in fm and isinstance(fm["description"], str):
            desc = fm["description"]
            if desc and not desc.endswith("."):
                desc = desc.rstrip() + "."
                desc_pattern = re.compile(r"^(description\s*:\s*).*$", re.MULTILINE)
                new_fm = desc_pattern.sub(lambda m: m.group(1) + desc, frontmatter)
                return new_fm, True
    except Exception:
        pass
    return frontmatter, False


def fix_short_description(frontmatter, yaml_content, name):
    """Fix descriptions that are too short."""
    try:
        fm = yaml.safe_load(yaml_content)
        if not fm or "description" not in fm:
            return frontmatter, False
        desc = fm["description"]
        if isinstance(desc, str) and len(desc) < 30:
            title = fm.get("title", name)
            new_desc = f"Use when needing to {desc.strip().lower() if desc.strip() else 'work with ' + title}"
            if not new_desc.endswith("."):
                new_desc += "."
            desc_pattern = re.compile(r"^(description\s*:\s*).*$", re.MULTILINE)
            new_fm = desc_pattern.sub(lambda m: m.group(1) + new_desc, frontmatter)
            return new_fm, True
    except Exception:
        pass
    return frontmatter, False


def process_file(path, dry_run=False):
    """Process a single .prompt.md file."""
    text = path.read_text(encoding="utf-8")

    # Split frontmatter from body
    fm_match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not fm_match:
        return 0, "no_frontmatter"

    frontmatter = fm_match.group(0)
    yaml_content = fm_match.group(1)
    body = text[fm_match.end() :]
    name = path.name.replace(".prompt.md", "")

    changes = 0

    # Fix frontmatter issues
    new_fm, changed = fix_description_no_period(frontmatter, yaml_content, name)
    if changed:
        frontmatter = new_fm
        changes += 1

    new_fm, changed = fix_short_description(frontmatter, yaml_content, name)
    if changed:
        frontmatter = new_fm
        changes += 1

    # Fix body issues
    new_body = fix_concatenated_headings(body)
    if new_body != body:
        changes += 1
        body = new_body

    new_body = ensure_blank_lines_between_sections(body)
    if new_body != body:
        changes += 1
        body = new_body

    # Reassemble
    new_text = frontmatter + body

    if changes > 0 and not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return changes, None


def main():
    dry_run = "--dry-run" in sys.argv

    files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    total_changes = 0
    changed_files = []
    error_files = []

    for pf in files:
        name = pf.name.replace(".prompt.md", "")
        changes, err = process_file(pf, dry_run)
        if err:
            error_files.append((name, err))
        elif changes > 0:
            total_changes += changes
            changed_files.append((name, changes))

    mode = "DRY RUN (no writes)" if dry_run else "APPLIED"
    print(f"=== Heading/Section Fixer ({mode}) ===")
    print(f"Total files: {len(files)}")
    print(f"Files with changes: {len(changed_files)}")
    print(f"Total change types applied: {total_changes}")

    if changed_files:
        print("\nChanged files:")
        for name, cnt in sorted(changed_files, key=lambda x: x[0])[:30]:
            print(f"  {name}: {cnt} fix(es)")
        if len(changed_files) > 30:
            print(f"  ... and {len(changed_files) - 30} more")

    if error_files:
        print("\nErrors:")
        for name, err in error_files:
            print(f"  {name}: {err}")


if __name__ == "__main__":
    main()
