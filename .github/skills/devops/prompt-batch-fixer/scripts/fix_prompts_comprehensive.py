#!/usr/bin/env python3
"""
Comprehensive prompt fix script — Phase 4 Batch Audit & Enhance.
Fixes: empty tags (inference), Python-list tags, missing name/version fields,
Copilot-style fields, dep prefix standardization, legacy sections.

Usage: python3 fix_prompts_comprehensive.py [--dry-run] [--batch N]
  --dry-run: preview changes without writing
  --batch N: process files in batch N (1-indexed, all if omitted)

REQUIRES: prompts/ directory at ~/Desktop/SandBox/prompts/
See skill: prompt-batch-fixer (devops/prompt-batch-fixer)
"""

import os
import re
import sys
import glob
from pathlib import Path

PROMPTS_DIR = os.path.expanduser("~/Desktop/SandBox/prompts")
DRY_RUN = "--dry-run" in sys.argv
SPECIFIC_BATCH = None
for arg in sys.argv:
    if arg.startswith("--batch="):
        SPECIFIC_BATCH = int(arg.split("=")[1])

BATCH_SIZE = 25
AUTHOR = "Hermes Agent"
LICENSE = "MIT"

# ─── Tag Inference Map ───────────────────────────────────────────────────────
KEYWORD_TAGS = {
    r'python': ['python'],
    r'typescript|tsx?': ['typescript'],
    r'javascript|node': ['javascript'],
    r'csharp|\.net|dotnet': ['csharp', 'dotnet'],
    r'java(?!script)': ['java'],
    r'ruby': ['ruby'],
    r'rust': ['rust'],
    r'go(?:lang)?\b': ['go'],
    r'sql|postgres|mysql|database|query': ['database', 'sql'],
    r'react': ['react'],
    r'next\.?js': ['nextjs'],
    r'django': ['django'],
    r'express': ['express'],
    r'spring': ['spring'],
    r'docker|container': ['docker'],
    r'kubernetes|k8s': ['kubernetes'],
    r'azure|bicep': ['azure'],
    r'aws': ['aws'],
    r'gcp|google-cloud': ['gcp'],
    r'ci.?cd': ['ci-cd'],
    r'terraform': ['terraform'],
    r'mcp': ['mcp'],
    r'playwright': ['playwright'],
    r'jest|pytest': ['testing'],
    r'eslint|lint': ['linting'],
    r'security|safety|injection|bias': ['security'],
    r'performance|optimi[sz]e': ['performance'],
    r'debug|triage': ['debugging'],
    r'refactor': ['refactoring'],
    r'migrate|upgrade': ['migration'],
    r'documentation|readme|mkdocs': ['documentation'],
    r'markdown': ['markdown'],
    r'architect|blueprint|design|adr': ['architecture'],
    r'specification|spec|feature': ['specification'],
    r'agent|acp|acpx': ['agents'],
    r'copilot|hermes|opencode': ['ai-assistant'],
    r'api': ['api'],
    r'git|github': ['git'],
    r'linux': ['linux'],
    r'windows': ['windows'],
    r'agile|scrum|kanban': ['agile'],
    r'workflow|orchestrat': ['workflow'],
    r'planning|roadmap': ['planning'],
    r'audit|review': ['audit'],
    r'generator|generate|create-': ['generator'],
    r'fix|repair|remediat': ['fix'],
    r'data': ['data'],
    r'machine.?learn|ml|ai': ['ml'],
    r'frontend|ui|ux|css|html': ['frontend'],
    r'backend|server': ['backend'],
    r'test': ['testing'],
    r'deploy': ['deployment'],
    r'config': ['configuration'],
    r'prompt': ['prompts'],
    r'skill': ['skills'],
}

NAME_PATTERN_TAGS = {
    r'^plan-': ['planning'],
    r'^execute-': ['execution'],
    r'^create-': ['generator'],
    r'^fix-': ['fix'],
    r'^update-': ['maintenance'],
    r'^migrate-': ['migration'],
    r'^audit-': ['audit'],
    r'^generate-': ['generator'],
    r'^convert-': ['conversion'],
    r'^validate-': ['validation'],
    r'^debug-': ['debugging'],
    r'^setup-': ['setup'],
    r'^refactor-': ['refactoring'],
    r'-mcp-': ['mcp'],
    r'-blueprint-': ['architecture'],
    r'-audit-': ['audit'],
    r'-review$': ['review'],
    r'-fix$': ['fix'],
    r'-generator$': ['generator'],
}


def slugify(name):
    s = name.replace(".prompt.md", "").replace(".prompt.txt", "").replace(".md", "")
    s = re.sub(r'[^a-zA-Z0-9_-]', '-', s)
    return s.lower().strip('-')


def titleize(name):
    s = slugify(name)
    return s.replace('-', ' ').replace('_', ' ').title()


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


def has_yaml_frontmatter(content):
    # CRITICAL: Check both LF and CRLF
    return content.startswith('---\n') or content.startswith('---\r\n')


def parse_frontmatter(content):
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
    for line in fm_lines:
        if line.startswith(field + ':'):
            val = line[len(field)+1:].strip()
            if val:
                return val
    return None


def update_field(fm_lines, field, value, add_if_missing=True):
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
    return [l for l in fm_lines if not (l.startswith(field + ':') or l.startswith(field + ': '))]


def get_h1(content):
    m = re.search(r'^# (.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else None


def remove_legacy_section(content):
    pattern = r'(?:\n|^)#{2,3} Legacy Prompt Details.*?(?=\n#+ |\Z)'
    result = re.sub(pattern, '', content, flags=re.DOTALL)
    return result


def fix_tags_format(fm_lines):
    """Convert Python-style tags: [...] to proper YAML list."""
    new_lines = []
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        # Multi-line: tags: [] then next line(s) have [...]
        if line.startswith('tags:') and '[]' in line:
            if i + 1 < len(fm_lines) and fm_lines[i + 1].strip().startswith('['):
                bracket_lines = [fm_lines[i + 1]]
                j = i + 2
                while j < len(fm_lines) and ']' not in fm_lines[j]:
                    bracket_lines.append(fm_lines[j])
                    j += 1
                if j < len(fm_lines):
                    bracket_lines.append(fm_lines[j])
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
        # Inline Python-list tags: [...]
        if line.startswith('tags:') and '[' in line:
            m = re.match(r'tags:\s*\[([^\]]*)\]', line)
            if m:
                items_str = m.group(1).strip()
                if not items_str:
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
        # Bare tags: with no value
        if line.strip() == 'tags:' or line.strip() == 'tags:':
            if i + 1 >= len(fm_lines) or not fm_lines[i + 1].lstrip().startswith('- '):
                new_lines.append('tags: []')
                i += 1
                continue
        new_lines.append(line)
        i += 1
    return new_lines


def standardize_dep_prefixes(fm_lines):
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
                if dep.startswith('command:'):
                    dep_name = dep.split(':', 1)[1].strip()
                    new_lines.append(f'  - skill:{dep_name}')
                elif dep.startswith('tool:'):
                    dep_name = dep.split(':', 1)[1].strip()
                    new_lines.append(f'  - skill:{dep_name}')
                elif dep.startswith('skill:') or dep.startswith('prompt:'):
                    new_lines.append(line)
                else:
                    new_lines.append(f'  - skill:{dep}')
            else:
                in_deps = False
                new_lines.append(line)
        else:
            new_lines.append(line)
    return new_lines


def infer_tags_for_file(filepath, fm_lines, body):
    """Infer tags from filename, frontmatter, and body content."""
    basename = os.path.basename(filepath)
    name_val = get_field(fm_lines, 'name') or slugify(basename)
    title_val = get_field(fm_lines, 'title') or titleize(basename)
    desc_val = get_field(fm_lines, 'description') or ''
    
    source = f"{title_val} {name_val} {desc_val}\n"
    source += body[:500].lower()
    
    tags = set()
    for pattern, tag_list in KEYWORD_TAGS.items():
        if re.search(pattern, source, re.IGNORECASE):
            tags.update(tag_list)
    for pattern, tag_list in NAME_PATTERN_TAGS.items():
        if re.search(pattern, basename.lower()):
            tags.update(tag_list)
    tags.add('prompts')
    
    return sorted(tags)


def fix_file(filepath):
    """Fix a single prompt file. Returns (filepath, issues_fixed, error)."""
    issues = []
    basename = os.path.basename(filepath)
    
    try:
        with open(filepath, 'rb') as f:
            raw = f.read()
        content = raw.replace(b'\r\n', b'\n').decode('utf-8')
        original = content
    except Exception as e:
        return (filepath, [], f"Cannot read: {e}")

    if basename.endswith('.prompt.txt') or basename.endswith('.txt'):
        return (filepath, [], None)

    has_fm = has_yaml_frontmatter(content)
    
    if not has_fm:
        name = slugify(basename)
        title = titleize(basename)
        desc = title
        new_content = f"---\nname: {name}\ntitle: \"{title}\"\ndescription: \"{desc}\"\nversion: 1.0.0\nauthor: \"{AUTHOR}\"\nlicense: {LICENSE}\ntags: []\n---\n\n{content}"
        issues.append("ADD_YAML_FRONTMATTER")
        content = new_content
        has_fm = True

    fm_lines, body_lines, _ = parse_frontmatter(content)
    if not fm_lines and not has_fm:
        return (filepath, issues, "Could not parse frontmatter")

    body = '\n'.join(body_lines)
    changed = False

    if not get_field(fm_lines, 'name'):
        name = slugify(basename)
        fm_lines = update_field(fm_lines, 'name', name)
        issues.append("ADD_NAME")
        changed = True

    if not get_field(fm_lines, 'title'):
        h1 = get_h1(body)
        title = h1.strip('"') if h1 else titleize(basename)
        fm_lines = update_field(fm_lines, 'title', title)
        issues.append("ADD_TITLE")
        changed = True

    if not get_field(fm_lines, 'version'):
        fm_lines = update_field(fm_lines, 'version', '1.0.0')
        issues.append("ADD_VERSION")
        changed = True

    if not get_field(fm_lines, 'author'):
        fm_lines = update_field(fm_lines, 'author', AUTHOR)
        issues.append("ADD_AUTHOR")
        changed = True
    if not get_field(fm_lines, 'license'):
        fm_lines = update_field(fm_lines, 'license', LICENSE)
        issues.append("ADD_LICENSE")
        changed = True

    old_tags = [l for l in fm_lines if l.startswith('tags:')]
    new_fm = fix_tags_format(fm_lines)
    if new_fm != fm_lines:
        fm_lines = new_fm
        issues.append("FIX_TAGS_FORMAT")
        changed = True

    for field in ['agent', 'model', 'tools']:
        new_fm = remove_field(fm_lines, field)
        if new_fm != fm_lines:
            fm_lines = new_fm
            issues.append(f"REMOVE_{field.upper()}_FIELD")
            changed = True

    new_fm = standardize_dep_prefixes(fm_lines)
    if new_fm != fm_lines:
        fm_lines = new_fm
        issues.append("STANDARDIZE_DEPS")
        changed = True

    new_body = remove_legacy_section(body)
    if new_body != body:
        body = new_body
        issues.append("REMOVE_LEGACY_SECTION")
        changed = True

    # Tag inference for empty tags
    has_empty_tags = False
    for line in fm_lines:
        if line.strip() == 'tags: []' or line.strip() == 'tags:':
            has_empty_tags = True
            break
    
    if has_empty_tags:
        inferred = infer_tags_for_file(filepath, fm_lines, body)
        if inferred:
            new_fm = []
            for line in fm_lines:
                if line.strip() == 'tags: []' or line.strip() == 'tags:':
                    new_fm.append('tags:')
                    for tag in inferred:
                        new_fm.append(f'  - {tag}')
                else:
                    new_fm.append(line)
            fm_lines = new_fm
            issues.append(f"INFER_TAGS({','.join(inferred)})")
            changed = True

    if changed:
        fm_str = '\n'.join(fm_lines)
        new_content = f"---\n{fm_str}\n---\n\n{body.lstrip()}"
        if new_content != original:
            if not DRY_RUN:
                write_file(filepath, new_content)
            issues.append("FILE_WRITTEN")

    return (filepath, issues, None)


def main():
    files = sorted(
        glob.glob(os.path.join(PROMPTS_DIR, "*.prompt.md")),
        key=os.path.getmtime
    )

    total = len(files)
    print(f"Total files to process: {total}")

    batches = [(i, min(i + BATCH_SIZE, total)) for i in range(0, total, BATCH_SIZE)]

    if SPECIFIC_BATCH is not None:
        if SPECIFIC_BATCH < 1 or SPECIFIC_BATCH > len(batches):
            print(f"Error: batch {SPECIFIC_BATCH} out of range (1-{len(batches)})")
            sys.exit(1)
        batches = [batches[SPECIFIC_BATCH - 1]]
        print(f"Processing batch {SPECIFIC_BATCH} only")

    total_issues = 0
    total_errors = 0
    total_written = 0

    for batch_num, (start, end) in enumerate(batches, 1):
        batch_files = files[start:end]
        print(f"\n=== Batch {batch_num}/{len(batches)} (files {start+1}-{end}) ===")

        for i, filepath in enumerate(batch_files):
            file_num = start + i + 1
            basename = os.path.basename(filepath)
            result = fix_file(filepath)
            path, issues, error = result

            if error:
                print(f"  [{file_num}] ✗ {basename}: ERROR - {error}")
                total_errors += 1
            elif issues:
                print(f"  [{file_num}] ✓ {basename}: {', '.join(issues)}")
                total_issues += len(issues)
                if "FILE_WRITTEN" in issues:
                    total_written += 1
            else:
                print(f"  [{file_num}] - {basename}: OK")

    if DRY_RUN:
        print(f"\n[DRY RUN] No files were modified.")
    print(f"\nDone. {total} files processed, {total_written} written, {total_issues} issues fixed, {total_errors} errors.")


if __name__ == "__main__":
    main()
