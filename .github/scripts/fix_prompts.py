#!/usr/bin/env python3
"""
Batch fix script for prompt files in ~/Desktop/SandBox/prompts/
Applies 12 issue fixes across 249 files.

Usage: python3 fix_prompts.py [--dry-run] [--batch N]
  --dry-run: preview changes without writing
  --batch N: process files in batch N (1-indexed, all if omitted)
"""

import os
import re
import sys
import glob
import shutil
from pathlib import Path

PROMPTS_DIR = os.path.expanduser("~/Desktop/SandBox/prompts")
DRY_RUN = "--dry-run" in sys.argv
SPECIFIC_BATCH = None
for arg in sys.argv:
    if arg.startswith("--batch="):
        SPECIFIC_BATCH = int(arg.split("=")[1])

BATCH_SIZE = 7
AUTHOR = "Hermes Agent"
LICENSE = "MIT"

def slugify(name):
    """Convert filename to a clean name slug."""
    s = name.replace(".prompt.md", "").replace(".prompt.txt", "").replace(".md", "")
    s = re.sub(r'[^a-zA-Z0-9_-]', '-', s)
    return s.lower().strip('-')

def titleize(name):
    """Convert filename to a title."""
    s = slugify(name)
    return s.replace('-', ' ').replace('_', ' ').title()

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def has_yaml_frontmatter(content):
    return content.startswith('---\n') or content.startswith('---\r\n')

def parse_frontmatter(content):
    """Extract frontmatter block and body. Returns (fm_lines, body, has_fm)."""
    lines = content.split('\n')
    if not (lines[0].strip() == '---'):
        return [], lines, False
    
    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break
    
    if end_idx == -1:
        return [], lines, False
    
    return lines[1:end_idx], lines[end_idx+1:], True

def get_field(fm_lines, field):
    """Get value of a YAML field from frontmatter lines."""
    for line in fm_lines:
        if line.startswith(field + ':'):
            return line[len(field)+1:].strip()
        # Handle multiline (>- or |)
    return None

def update_field(fm_lines, field, value, add_if_missing=True):
    """Update a field in frontmatter lines. Returns updated lines."""
    new_lines = []
    found = False
    for line in fm_lines:
        if line.startswith(field + ':') or line.startswith(field + ': '):
            new_lines.append(f"{field}: {value}")
            found = True
        else:
            new_lines.append(line)
    if not found and add_if_missing:
        new_lines.insert(0, f"{field}: {value}")
    return new_lines

def remove_field(fm_lines, field):
    """Remove a field from frontmatter."""
    return [l for l in fm_lines if not (l.startswith(field + ':') or l.startswith(field + ': '))]

def get_h1(content):
    """Extract first H1 heading text."""
    m = re.search(r'^# (.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else None

def remove_legacy_section(content):
    """Remove ## Legacy Prompt Details section and everything until next ## or end."""
    # Pattern: "## Legacy Prompt Details" or "### Legacy Prompt Details" followed by any content until next ## or end
    pattern = r'(?:\n|^)#{2,3} Legacy Prompt Details.*?(?=\n#+ |\Z)'
    result = re.sub(pattern, '', content, flags=re.DOTALL)
    return result

def fix_tags_format(fm_lines):
    """Convert Python-style tags: [...] to proper YAML list.
    Also fix 'tags:' with no value to 'tags: []'.
    Also fix multi-line 'tags: []\n[' format.
    """
    new_lines = []
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        # Fix multi-line format: tags: [] then next line(s) have [...]
        if line.startswith('tags:') and '[]' in line:
            # Check if next line starts with '[' (multi-line Python list)
            if i + 1 < len(fm_lines) and fm_lines[i + 1].strip().startswith('['):
                # Consume all lines until the ']' line
                bracket_lines = [fm_lines[i + 1]]
                j = i + 2
                while j < len(fm_lines) and ']' not in fm_lines[j]:
                    bracket_lines.append(fm_lines[j])
                    j += 1
                if j < len(fm_lines):
                    bracket_lines.append(fm_lines[j])
                # Combine the bracket block
                full = ' '.join(bl.strip() for bl in bracket_lines)
                m = re.match(r'\[([^\]]*)\]', full)
                if m:
                    items_str = m.group(1).strip()
                    items = [item.strip().strip('"').strip("'") for item in items_str.split(',')]
                    items = [it for it in items if it]
                    if items:
                        new_lines.append('tags:')
                        for item in items:
                            new_lines.append(f'  - {item}')
                    else:
                        new_lines.append('tags: []')
                else:
                    new_lines.append('tags: []')
                i = j + 1
                continue
        # Fix inline Python-list tags: [...]
        if line.startswith('tags:') and '[' in line:
            m = re.match(r'tags:\s*\[([^\]]*)\]', line)
            if m:
                items_str = m.group(1).strip()
                if not items_str:
                    # Empty list — keep [] format
                    new_lines.append('tags: []')
                    i += 1
                    continue
                items = [item.strip().strip('"').strip("'") for item in items_str.split(',')]
                new_lines.append('tags:')
                for item in items:
                    if item:
                        new_lines.append(f'  - {item}')
                i += 1
                continue
        # Fix 'tags:' with no value and not followed by - items
        if line.strip() == 'tags:' or line.strip() == 'tags:':
            # Check next line — if it doesn't exist or doesn't start with '  - ', it's empty
            if i + 1 >= len(fm_lines) or not fm_lines[i + 1].lstrip().startswith('- '):
                new_lines.append('tags: []')
                i += 1
                continue
        new_lines.append(line)
        i += 1
    return new_lines

def standardize_dep_prefixes(fm_lines):
    """Standardize dependency prefixes: command:/tool: -> skill:"""
    new_lines = []
    in_deps = False
    for line in fm_lines:
        if line.startswith('dependencies:'):
            in_deps = True
            new_lines.append(line)
            continue
        if in_deps:
            if line.startswith('  - ') or line.startswith('  -'):
                dep = line.strip().lstrip('- ')
                # Handle command: prefix
                if dep.startswith('command:'):
                    dep_name = dep.split(':', 1)[1].strip()
                    new_lines.append(f'  - skill:{dep_name}')
                # Handle tool: prefix  
                elif dep.startswith('tool:'):
                    dep_name = dep.split(':', 1)[1].strip()
                    new_lines.append(f'  - skill:{dep_name}')
                # Already skill: prefix
                elif dep.startswith('skill:'):
                    new_lines.append(line)
                else:
                    # Bare name - add skill: prefix
                    new_lines.append(f'  - skill:{dep}')
            else:
                in_deps = False
                new_lines.append(line)
        else:
            new_lines.append(line)
    return new_lines

def fix_file(filepath, batch_num, file_num):
    """Fix a single prompt file. Returns (filepath, issues_fixed, error)."""
    issues = []
    basename = os.path.basename(filepath)
    
    try:
        content = read_file(filepath)
        original = content
    except Exception as e:
        return (filepath, [], f"Cannot read: {e}")

    # Skip .txt files for YAML frontmatter fixes — they're raw references
    if basename.endswith('.prompt.txt') or basename.endswith('.txt'):
        return (filepath, [], None)
    
    has_fm = has_yaml_frontmatter(content)
    
    if not has_fm:
        # Add YAML frontmatter
        name = slugify(basename)
        title = titleize(basename).replace('.Prompt Md', '').replace('.Md', '')
        desc = title
        
        new_content = f"---\nname: {name}\ntitle: \"{title}\"\ndescription: \"{desc}\"\nversion: 1.0.0\nauthor: \"{AUTHOR}\"\nlicense: {LICENSE}\ntags: []\n---\n\n{content}"
        issues.append("ADD_YAML_FRONTMATTER")
        content = new_content
        has_fm = True

    # Now parse frontmatter and body
    fm_lines, body_lines, _ = parse_frontmatter(content)
    if not fm_lines and not has_fm:
        return (filepath, issues, "Could not parse frontmatter")
    
    body = '\n'.join(body_lines)
    changed = False
    
    # Store original fm for comparison
    original_fm = fm_lines.copy()
    
    # 1. Add name: field (derive from filename)
    if not get_field(fm_lines, 'name'):
        name = slugify(basename)
        fm_lines = update_field(fm_lines, 'name', name)
        issues.append("ADD_NAME")
        changed = True
    
    # 2. Add title: field (from H1 or filename)
    if not get_field(fm_lines, 'title'):
        h1 = get_h1(body)
        if h1:
            title = h1.strip('"')
        else:
            title = titleize(basename)
        fm_lines = update_field(fm_lines, 'title', title)
        issues.append("ADD_TITLE")
        changed = True
    
    # 3. Add version: field
    if not get_field(fm_lines, 'version'):
        fm_lines = update_field(fm_lines, 'version', '1.0.0')
        issues.append("ADD_VERSION")
        changed = True
    
    # 4. Add author: and license:
    if not get_field(fm_lines, 'author'):
        fm_lines = update_field(fm_lines, 'author', AUTHOR)
        issues.append("ADD_AUTHOR")
        changed = True
    if not get_field(fm_lines, 'license'):
        fm_lines = update_field(fm_lines, 'license', LICENSE)
        issues.append("ADD_LICENSE")
        changed = True
    
    # 5. Fix tags format (Python list -> YAML array)
    old_tags = [l for l in fm_lines if l.startswith('tags:')]
    new_fm = fix_tags_format(fm_lines)
    if new_fm != fm_lines:
        fm_lines = new_fm
        issues.append("FIX_TAGS_FORMAT")
        changed = True
    
    # 5b. Remove Copilot-style 'agent:' field (not used in Hermes)
    new_fm = remove_field(fm_lines, 'agent')
    if new_fm != fm_lines:
        fm_lines = new_fm
        issues.append("REMOVE_AGENT_FIELD")
        changed = True
    
    # 5c. Remove Copilot-style 'model:' field (not used in Hermes)
    new_fm = remove_field(fm_lines, 'model')
    if new_fm != fm_lines:
        fm_lines = new_fm
        issues.append("REMOVE_MODEL_FIELD")
        changed = True
    
    # 5d. Convert Copilot-style 'tools:' to Hermes-standard 'toolsets:'
    # Find 'tools:' field, rename to 'toolsets:', keep the value
    tools_line = get_field(fm_lines, 'tools')
    if tools_line is not None:
        fm_lines = remove_field(fm_lines, 'tools')
        # Insert toolsets: with same value
        fm_lines = update_field(fm_lines, 'toolsets', tools_line)
        issues.append("CONVERT_TOOLS_TO_TOOLSETS")
        changed = True
    
    # 6. Standardize dependency prefixes
    new_fm = standardize_dep_prefixes(fm_lines)
    if new_fm != fm_lines:
        fm_lines = new_fm
        issues.append("STANDARDIZE_DEPS")
        changed = True
    
    # 7. Remove ## Legacy Prompt Details section
    new_body = remove_legacy_section(body)
    if new_body != body:
        body = new_body
        issues.append("REMOVE_LEGACY_SECTION")
        changed = True
    
    # 8. Build new content and write
    if changed:
        fm_str = '\n'.join(fm_lines)
        new_content = f"---\n{fm_str}\n---\n\n{body.lstrip()}"
        
        if new_content != original:
            if not DRY_RUN:
                write_file(filepath, new_content)
            issues.append("FILE_WRITTEN")
    
    return (filepath, issues, None)


def main():
    # Get all .prompt.md files, sorted oldest first
    files = sorted(
        glob.glob(os.path.join(PROMPTS_DIR, "*.prompt.md")),
        key=os.path.getmtime
    )
    
    # Also handle debugger-prompt.md, pl.md, .txt files
    extra_files = sorted(glob.glob(os.path.join(PROMPTS_DIR, "*.md")))
    for f in extra_files:
        if f.endswith('.prompt.md'):
            continue
        if f not in files:
            files.append(f)
    
    txt_files = sorted(glob.glob(os.path.join(PROMPTS_DIR, "*.prompt.txt")))
    files.extend(txt_files)
    
    total = len(files)
    print(f"Total files to process: {total}")
    
    # Calculate batch ranges
    batches = [(i, min(i + BATCH_SIZE, total)) for i in range(0, total, BATCH_SIZE)]
    
    if SPECIFIC_BATCH is not None:
        if SPECIFIC_BATCH < 1 or SPECIFIC_BATCH > len(batches):
            print(f"Error: batch {SPECIFIC_BATCH} out of range (1-{len(batches)})")
            sys.exit(1)
        batches = [batches[SPECIFIC_BATCH - 1]]
        print(f"Processing batch {SPECIFIC_BATCH} only")
    
    for batch_num, (start, end) in enumerate(batches, 1):
        batch_files = files[start:end]
        print(f"\n=== Batch {batch_num}/{len(batches)} (files {start+1}-{end}) ===")
        
        for i, filepath in enumerate(batch_files):
            file_num = start + i + 1
            basename = os.path.basename(filepath)
            result = fix_file(filepath, batch_num, file_num)
            path, issues, error = result
            
            if error:
                print(f"  [{file_num}] ✗ {basename}: ERROR - {error}")
            elif issues:
                print(f"  [{file_num}] ✓ {basename}: {', '.join(issues)}")
            else:
                print(f"  [{file_num}] - {basename}: OK (no changes needed)")
    
    if DRY_RUN:
        print(f"\n[DRY RUN] No files were modified.")
    print(f"\nDone. {total} files processed.")

if __name__ == "__main__":
    main()
