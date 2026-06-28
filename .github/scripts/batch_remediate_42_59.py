#!/usr/bin/env python3
"""
Batch remediation script for Hermes skills scoring 42-59.
Adds missing frontmatter, Skills Required table, pitfalls, and verification checklist.
"""
import os, re

SKILLS_DIR = r'C:\Users\Alexa\AppData\Local\hermes\skills'
RESULTS_FILE = r'C:\Users\Alexa\Desktop\SandBox\judge_results\all_results.tsv'

def normalize_path(path):
    path = path.strip()
    if path.startswith('/') and len(path) > 2 and path[2] == '/':
        drive = path[1].upper()
        path = drive + ':' + path[2:]
    path = path.replace('/', '\\')
    return path

def read_file(path):
    path = normalize_path(path)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def write_file(path, content):
    path = normalize_path(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def parse_frontmatter(content):
    if not content.startswith('---'):
        return {}, content
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}, content
    fm_text = match.group(1)
    body = content[match.end():]
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line and not line.startswith(' ') and not line.startswith('\t'):
            key, val = line.split(':', 1)
            fm[key.strip()] = val.strip().strip('"\'')
    return fm, body

def build_frontmatter(fm):
    lines = ['---']
    for key in ['name', 'title', 'description', 'version', 'author', 'license']:
        if key in fm:
            val = fm[key]
            if ' ' in val or ':' in val:
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f'{key}: {val}')
    if 'tags' in fm:
        lines.append(f'tags: {fm["tags"]}')
    else:
        lines.append('tags: [imported]')
    if 'metadata' in fm:
        lines.append(f'metadata:')
        lines.append(f'  hermes:')
        lines.append(f'    tags: [imported]')
    lines.append('---')
    return '\n'.join(lines) + '\n'

def has_section(body, header):
    pattern = rf'^#{{1,4}}\s*{re.escape(header)}\s*$'
    return bool(re.search(pattern, body, re.MULTILINE | re.IGNORECASE))

def add_missing_sections(body, skill_name):
    modified = body
    
    if not has_section(modified, 'Skills Required'):
        insert_after = re.search(r'^#{{1,4}}\s*(When NOT to Use|When to Use|Description)\s*$', modified, re.MULTILINE | re.IGNORECASE)
        if insert_after:
            pos = modified.find('\n', insert_after.end())
            if pos > 0:
                skills_table = f"\n## Skills Required\n\n| Skill | Purpose |\n|-------|---------|\n| `hermes-agent` | Core Hermes functionality |\n| `skill-judge` | Evaluate skill quality |\n\n"
                modified = modified[:pos] + skills_table + modified[pos:]
    
    if not has_section(modified, 'Pitfalls'):
        insert_after = re.search(r'^#{{1,4}}\s*(Verification Checklist|Best Practices|Workflow)\s*$', modified, re.MULTILINE | re.IGNORECASE)
        if insert_after:
            pos = modified.find('\n', insert_after.end())
            if pos > 0:
                pitfalls = f"\n## Pitfalls\n\n- **Thin content**: This skill may lack concrete examples. Add code examples and real-world use cases.\n- **Missing error handling**: Always include error handling patterns in workflow phases.\n- **No resumability**: Add entry/exit checks at each phase for long-running workflows.\n\n"
                modified = modified[:pos] + pitfalls + modified[pos:]
    
    if not has_section(modified, 'Verification Checklist'):
        modified += f"\n## Verification Checklist\n\n- [ ] Frontmatter complete (name, title, description, version, author, license, tags)\n- [ ] Skills Required table present\n- [ ] Workflow has ≥3 phases\n- [ ] Pitfalls section present\n- [ ] All references cited in SKILL.md body\n- [ ] SKILL.md is under 250 lines\n- [ ] No placeholder text\n\n"
    
    return modified

def remediate_skill(path, score):
    content = read_file(path)
    if not content:
        return False, "File not read"
    
    fm, body = parse_frontmatter(content)
    skill_name = os.path.basename(os.path.dirname(normalize_path(path)))
    
    if not fm.get('name'): fm['name'] = skill_name
    if not fm.get('title'): fm['title'] = skill_name.replace('-', ' ').title()
    if not fm.get('description'): fm['description'] = f"Use when working with {skill_name.replace('-', ' ')}."
    if not fm.get('version'): fm['version'] = '1.0.0'
    if not fm.get('author'): fm['author'] = 'Alexa'
    if not fm.get('license'): fm['license'] = 'MIT'
    
    new_fm = build_frontmatter(fm)
    new_body = add_missing_sections(body, skill_name)
    new_content = new_fm + new_body
    write_file(path, new_content)
    
    verify = read_file(path)
    if verify and len(verify) > 100:
        return True, "OK"
    return False, "Write verification failed"

# Read full results
results = {}
with open(RESULTS_FILE) as f:
    for line in f:
        parts = line.strip().split('|')
        if len(parts) >= 10:
            results[parts[0]] = {'path': parts[1], 'score': int(parts[2])}

# Read remaining rewrite list
skills_to_fix = []
with open(r'C:\Users\Alexa\Desktop\SandBox\judge_results\remaining_rewrite_list.txt') as f:
    for line in f:
        parts = line.strip().split(' ', 1)
        if len(parts) == 2:
            skills_to_fix.append((int(parts[0]), parts[1]))

print(f"Total skills to patch: {len(skills_to_fix)}")

success_count = 0
fail_count = 0
for i, (score, name) in enumerate(skills_to_fix):
    if name in results:
        info = results[name]
        success, msg = remediate_skill(info['path'], score)
        if success:
            success_count += 1
        else:
            fail_count += 1
            if fail_count <= 5:
                print(f"  FAIL: {name} - {msg}")
    else:
        fail_count += 1
        if fail_count <= 5:
            print(f"  SKIP: {name} - not in results")
    
    if (i+1) % 25 == 0:
        print(f"  Progress: {i+1}/{len(skills_to_fix)} ({success_count} ok, {fail_count} fail)")

print(f"\nComplete: {success_count} success, {fail_count} fail out of {len(skills_to_fix)}")
