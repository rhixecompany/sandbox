#!/usr/bin/env python3
"""
Quick fix: Add missing title field to skills failing audit.
"""

import os
import re
from pathlib import Path

SKILLS_DIR = Path(r'C:\Users\Alexa\AppData\Local\hermes\skills')

def find_skills_missing_title():
    """Find all SKILL.md files missing the title field."""
    missing = []
    for root, dirs, files in os.walk(SKILLS_DIR):
        if 'SKILL.md' in files:
            path = Path(root) / 'SKILL.md'
            try:
                content = path.read_text(encoding='utf-8', errors='ignore')
                # Check if frontmatter exists
                if content.startswith('---'):
                    end = content.find('\n---', 4)
                    if end > 0:
                        fm = content[4:end]
                        has_title = 'title:' in fm
                        has_name = 'name:' in fm
                        if has_name and not has_title:
                            # Extract name
                            name_match = re.search(r'^name:\s*(.+)$', fm, re.MULTILINE)
                            if name_match:
                                name = name_match.group(1).strip().strip('"').strip("'")
                                title = name.replace('-', ' ').title()
                                missing.append({'path': path, 'name': name, 'title': title})
            except:
                continue
    return missing


def fix_skill(path, title):
    """Add title field to a skill's frontmatter."""
    content = path.read_text(encoding='utf-8', errors='ignore')
    
    # Find the name field and add title after it
    lines = content.split('\n')
    new_lines = []
    name_found = False
    
    for line in lines:
        new_lines.append(line)
        if line.startswith('name:') and not name_found:
            new_lines.append(f'title: {title}')
            name_found = True
    
    new_content = '\n'.join(new_lines)
    path.write_text(new_content, encoding='utf-8')
    return True


def main():
    print("=== FIXING MISSING TITLE FIELD ===")
    
    missing = find_skills_missing_title()
    print(f"Skills missing title: {len(missing)}")
    
    fixed = 0
    for item in missing:
        try:
            fix_skill(item['path'], item['title'])
            fixed += 1
        except Exception as e:
            print(f"  ERROR: {item['name']}: {e}")
    
    print(f"Fixed: {fixed}")


if __name__ == '__main__':
    main()
