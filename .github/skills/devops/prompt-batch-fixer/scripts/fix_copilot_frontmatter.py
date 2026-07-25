#!/usr/bin/env python3
"""
Fix remaining Copilot-style prompt files that have:
1. Frontmatter starting with toolsets: instead of name:
2. Multiple --- blocks (duplicate frontmatter from previous fix)
3. CRLF line endings

Strategy: Find the LAST --- block (the one added by the comprehensive fix),
merge it with the first block's non-standard fields, and produce a clean single frontmatter.

Usage: python3 fix_copilot_frontmatter.py [--dry-run]
"""

import os
import re
import glob

PROMPTS_DIR = os.path.expanduser("~/Desktop/SandBox/prompts")
AUTHOR = "Hermes Agent"
LICENSE = "MIT"
DRY_RUN = "--dry-run" in sys.argv


def slugify(name):
    s = name.replace(".prompt.md", "")
    s = re.sub(r'[^a-zA-Z0-9_-]', '-', s)
    return s.lower().strip('-')


def titleize(name):
    s = slugify(name)
    return s.replace('-', ' ').replace('_', ' ').title()


def fix_file(filepath):
    with open(filepath, 'rb') as f:
        raw = f.read()
    
    content = raw.replace(b'\r\n', b'\n').decode('utf-8')
    lines = content.split('\n')
    
    # Find all --- positions in first 200 lines
    dashes = [i for i, line in enumerate(lines[:200]) if line.strip() == '---']
    
    if len(dashes) < 2:
        return False
    
    # Find the last pair of --- that form a frontmatter block
    last_dash = dashes[-1]
    second_last_dash = dashes[-2]
    
    last_fm = lines[second_last_dash+1:last_dash]
    first_fm = lines[1:dashes[1]] if len(dashes) >= 2 else []
    
    body = '\n'.join(lines[last_dash+1:]).lstrip()
    
    # Check if last block has our fields
    has_name = any(l.startswith('name:') for l in last_fm)
    
    if not has_name:
        for i in range(len(dashes)-2, -1, -1):
            fm = lines[dashes[i]+1:dashes[i+1]]
            if any(l.startswith('name:') for l in fm):
                last_fm = fm
                has_name = True
                break
    
    new_fm = list(last_fm)
    
    # Merge non-standard fields from first block
    first_fields = {}
    for line in first_fm:
        if ':' in line and not line.strip().startswith('-'):
            key, val = line.split(':', 1)
            first_fields[key.strip()] = val.strip()
    
    standard_keys = {'name', 'title', 'version', 'author', 'license', 'tags', 'description', 'trigger', 'dependencies', 'skills'}
    for key, val in first_fields.items():
        existing_keys = [l.split(':')[0].strip() for l in new_fm if ':' in l]
        if key not in existing_keys and key not in standard_keys:
            new_fm.append(f"{key}: {val}")
    
    # Ensure required fields
    existing_keys = [l.split(':')[0].strip() for l in new_fm if ':' in l]
    if 'name' not in existing_keys:
        new_fm.insert(0, f"name: {slugify(os.path.basename(filepath))}")
    if 'version' not in existing_keys:
        new_fm.append("version: 1.0.0")
    
    new_content = '---\n' + '\n'.join(new_fm) + '\n---\n\n' + body
    
    if not DRY_RUN:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(new_content)
    
    return True


def main():
    files = sorted(glob.glob(os.path.join(PROMPTS_DIR, "*.prompt.md")))
    
    fixed = 0
    for filepath in files:
        basename = os.path.basename(filepath)
        if fix_file(filepath):
            print(f"Fixed: {basename}")
            fixed += 1
    
    if DRY_RUN:
        print(f"\n[DRY RUN] {fixed} files would be fixed.")
    else:
        print(f"\nFixed {fixed} Copilot-style files.")


if __name__ == "__main__":
    main()
