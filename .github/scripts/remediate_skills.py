#!/usr/bin/env python3
"""Bulk auto-remediate failing skills — add missing frontmatter fields."""

import os
import re
from pathlib import Path

SKILLS_ROOT = Path(os.environ.get("HOME", "C:/Users/Alexa")) / "AppData/Local/hermes/skills"
fixed = 0
errors = 0


def remediate_one(path: Path) -> bool:
    global fixed, errors
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  ERROR reading {path.name}: {e}")
        errors += 1
        return False

    original = text
    name = path.parent.name  # directory name = skill name

    # CASE 1: Has proper frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)

    if fm_match:
        fm = fm_match.group(1)
        if not fm.endswith("\n"):
            fm += "\n"
        body = text[fm_match.end() :]
        changed = False

        # Add name: if missing
        if not re.search(r"^name:", fm, re.M):
            # Insert after first line or before description
            fm = f"name: {name}\n" + fm
            changed = True

        # Add description: if missing
        if not re.search(r"^description:", fm, re.M):
            # Use title field if present, otherwise use name
            title_match = re.search(r"^title:\s*[\"']?([^\"'\n]+)", fm, re.M)
            desc = title_match.group(1) if title_match else name.replace("-", " ").title()
            fm = fm + f'description: "{desc}"\n'
            changed = True

        if changed:
            text = f"---\n{fm}\n---\n{body}"
    else:
        # CASE 2: No frontmatter at all — detect if there's a title heading
        title_match = re.search(r"^#\s+(.+)$", text, re.M)
        title = title_match.group(1) if title_match else name.replace("-", " ").title()
        fm = f'---\nname: {name}\ndescription: "{title}"\n---\n\n'
        text = fm + text.lstrip()
        changed = True

    if text != original:
        path.write_text(text, encoding="utf-8")
        fixed += 1
        return True
    return False


# Find all SKILL.md files
all_skills = sorted(SKILLS_ROOT.rglob("SKILL.md"))
print(f"Scanning {len(all_skills)} skills...")

for s in all_skills:
    remediate_one(s)

print(f"\nFixed: {fixed}")
print(f"Errors: {errors}")
print(f"Unchanged: {len(all_skills) - fixed - errors}")
