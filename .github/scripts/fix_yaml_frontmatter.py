#!/usr/bin/env python3
"""Fix YAML frontmatter with embedded quotes in description fields."""
import os, re, yaml
from pathlib import Path

BASE = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")

# Skills known to have YAML parse errors (from batch_judge YAML failures)
all_skills = list(BASE.rglob("SKILL.md"))

fixed = 0
errors = 0
skipped = 0

for path in all_skills:
    try:
        content = path.read_text(encoding="utf-8")
    except:
        continue

    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        # Try with \r\n
        fm_match = re.match(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
    if not fm_match:
        skipped += 1
        continue

    fm_text = fm_match.group(1)
    try:
        parsed = yaml.safe_load(fm_text)
        if parsed and "name" in parsed:
            skipped += 1  # YAML is fine
            continue
    except yaml.YAMLError as e:
        pass  # Needs fixing

    # Fix embedded quotes in description lines
    lines = fm_text.split("\n")
    new_lines = []
    changed = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("description:"):
            val = stripped[stripped.index(":")+1:].strip()
            # Check for quoted string with embedded quotes
            if val.startswith('"') and not val.endswith('"') and '"' in val[1:]:
                # Unclosed quote - find and fix
                changed = True
            if val.startswith('"') and val.endswith('"'):
                inner = val[1:-1]
                if '"' in inner and ("'" not in inner or '\\"' not in inner):
                    inner = inner.replace('"', "'")
                    indent = " " * (len(line) - len(line.lstrip()))
                    new_lines.append(f'{indent}description: "{inner}"')
                    changed = True
                    continue
        new_lines.append(line)

    if changed:
        new_fm = "\n".join(new_lines)
        new_content = content[:fm_match.start(1)] + new_fm + content[fm_match.end(1):]
        path.write_text(new_content, encoding="utf-8")
        print(f"✅ {path.parent.name}: fixed")
        fixed += 1
    else:
        # Try block scalar conversion
        lines = fm_text.split("\n")
        new_lines = []
        changed = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("description:") and '"' in stripped:
                val = stripped[stripped.index(":")+1:].strip()
                if val.startswith('"') and val.endswith('"') and val.count('"') > 2:
                    inner = val[1:-1]
                    indent = " " * (len(line) - len(line.lstrip()))
                    new_lines.append(f'{indent}description: "{inner}"')
                    changed = True
                    continue
            new_lines.append(line)
        if changed:
            new_fm = "\n".join(new_lines)
            new_content = content[:fm_match.start(1)] + new_fm + content[fm_match.end(1):]
            path.write_text(new_content, encoding="utf-8")
            print(f"✅ {path.parent.name}: fixed (alt)")
            fixed += 1
        else:
            print(f"⏩ {path.parent.name}: needs manual fix")
            errors += 1

print(f"\nDone: {fixed} fixed, {errors} needs manual, {skipped} ok/skipped")
