#!/usr/bin/env python3
"""
fix_orphaned_brackets.py — Clean up orphaned [...] blocks from multi-line tools: → toolsets: conversion.

The fix_prompts.py conversion of multi-line 'tools:\n  [\n    "item",\n  ]' to 'toolsets: ' 
left the bracket block orphaned. This script finds and removes them, building proper toolsets: value.
"""
import os
import re
import sys
import glob

PROMPTS_DIR = os.path.expanduser("~/Desktop/SandBox/prompts")
DRY_RUN = "--dry-run" in sys.argv

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def has_orphaned_bracket(fm_block):
    """Check if frontmatter block has orphaned [...] block (not assigned to any field)."""
    lines = fm_block.split('\n')
    for i, line in enumerate(lines):
        # Match lines like:  [   or  [ or   "item",
        if re.match(r'^\s*\[', line) or re.match(r'^\s+"', line) or line.strip() == ']':
            # Check it's NOT part of an inline YAML array (no field: preceding it on same line)
            if i == 0 or not re.match(r'^\s*\w+:', lines[i-1]):
                return True
    return False

def extract_bracket_block(fm_block):
    """Extract items from an orphaned [...] block in frontmatter.
    Returns (cleaned_fm, items_list)."""
    lines = fm_block.split('\n')
    bracket_lines = []
    clean_lines = []
    in_bracket = False
    bracket_depth = 0
    items = []
    
    for line in lines:
        stripped = line.strip()
        # Detect start of orphaned bracket block: line that starts with [
        if re.match(r'^\s*\[', line) and not re.match(r'^\s*\w+:', line):
            in_bracket = True
            bracket_depth += stripped.count('[')
            bracket_depth -= stripped.count(']')
            bracket_lines.append(line)
            continue
        
        if in_bracket:
            bracket_lines.append(line)
            bracket_depth += stripped.count('[')
            bracket_depth -= stripped.count(']')
            if bracket_depth <= 0:
                # End of bracket block — parse items
                full = ' '.join(bl.strip() for bl in bracket_lines)
                m = re.match(r'\[([^\]]*)\]', full)
                if m:
                    raw = m.group(1)
                    items = [item.strip().strip('"').strip("'") 
                            for item in re.split(r',\s*', raw) if item.strip()]
                in_bracket = False
            continue
        
        clean_lines.append(line)
    
    return '\n'.join(clean_lines), items

def fix_file(filepath):
    """Fix a single file with orphaned bracket block."""
    basename = os.path.basename(filepath)
    if not basename.endswith('.prompt.md'):
        return (filepath, [], None)
    
    content = read_file(filepath)
    original = content
    
    # Find frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return (filepath, [], "no frontmatter")
    
    fm_block = fm_match.group(1)
    
    if not has_orphaned_bracket(fm_block):
        return (filepath, [], None)  # No orphaned bracket
    
    issues = []
    
    # Check if toolsets: has no value (orphaned conversion)
    toolsets_empty = bool(re.search(r'^toolsets:\s*$', fm_block, re.MULTILINE))
    toolsets_has_value = bool(re.search(r'^toolsets:\s+\S', fm_block, re.MULTILINE))
    
    # Extract bracket items
    cleaned_fm, items = extract_bracket_block(fm_block)
    issues.append(f"REMOVED_BRACKET_BLOCK({len(items)} items)")
    
    if toolsets_empty and items:
        # Replace the empty toolsets: line with proper YAML list
        item_yaml = '\n'.join(f'  - {it}' for it in items)
        cleaned_fm = re.sub(
            r'^toolsets:\s*$', 
            f'toolsets:\n{item_yaml}',
            cleaned_fm,
            flags=re.MULTILINE
        )
        issues.append("TOOLSETS_POPULATED")
    elif toolsets_empty:
        cleaned_fm = re.sub(r'^toolsets:\s*$', 'toolsets: []', cleaned_fm, flags=re.MULTILINE)
        issues.append("TOOLSETS_EMPTIED")
    
    if toolsets_has_value and items:
        issues.append("TOOLSETS_ALREADY_HAS_VALUE(orphan items discarded)")
    
    new_content = f"---\n{cleaned_fm}\n---\n" + content[fm_match.end():]
    
    if new_content != original:
        if not DRY_RUN:
            write_file(filepath, new_content)
        issues.append("FILE_WRITTEN")
        return (filepath, issues, None)
    
    return (filepath, issues, None)

def main():
    files = sorted(glob.glob(os.path.join(PROMPTS_DIR, "*.prompt.md")))
    total = len(files)
    
    changed = 0
    for filepath in files:
        path, issues, error = fix_file(filepath)
        basename = os.path.basename(path)
        if error:
            print(f"  ✗ {basename}: ERROR - {error}")
        elif issues:
            print(f"  ✓ {basename}: {', '.join(issues)}")
            changed += 1
        else:
            pass  # No issues
    
    if DRY_RUN:
        print(f"\n[DRY RUN] {changed} files would be modified.")
    else:
        print(f"\nDone. {changed} files modified.")
    print(f"Total scanned: {total}")

if __name__ == "__main__":
    main()
