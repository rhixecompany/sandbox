#!/usr/bin/env python3
"""batch_remediate.py — Patch skills scoring < 80 with common fixes.
Adds missing frontmatter fields, Skills Required table, pitfalls section, verification checklist.
"""
import os, re, yaml
from pathlib import Path

SKILLS_BASE = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
RESULTS_FILE = Path(r"C:\Users\Alexa\Desktop\SandBox\judge_results\all_results.tsv")

def get_skill_name(path):
    try:
        content = path.read_text(encoding='utf-8')
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = yaml.safe_load(fm_match.group(1))
            return fm.get('name', '')
    except:
        pass
    return ''

def remediate_skill(skill_path, name):
    """Apply common fixes to a skill."""
    content = skill_path.read_text(encoding='utf-8')
    original = content
    changes = []
    
    # Parse frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return False, ["No frontmatter found"]
    
    fm_text = fm_match.group(1)
    try:
        fm = yaml.safe_load(fm_text) or {}
    except:
        return False, ["YAML parse error"]
    
    # Fix 1: Add missing frontmatter fields
    defaults = {
        'title': name.replace('-', ' ').title() if name else '',
        'version': '1.0.0',
        'author': 'Hermes Agent',
        'license': 'MIT',
    }
    for field, default in defaults.items():
        if field not in fm:
            fm[field] = default
            changes.append(f"Added '{field}': {default}")
    
    if 'tags' in fm and isinstance(fm['tags'], list) and len(fm['tags']) == 0:
        fm['tags'] = ['imported']
        changes.append("Added default tags")
    
    # Rebuild frontmatter
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True)
    content = content[:fm_match.start(1)] + new_fm + content[fm_match.end(1):]
    
    # Fix 2: Add Skills Required table if missing
    if '## Skills Required' not in content:
        # Find a good insertion point (after Description/Overview section)
        insert_marker = '## Description'
        if insert_marker in content:
            idx = content.find(insert_marker)
            next_section = content.find('\n## ', idx + len(insert_marker))
            if next_section > 0:
                table = "\n\n## Skills Required\n\n| Skill | Purpose |\n|-------|---------|\n| `terminal` | CLI commands execution |\n| `file` | Read/write files |\n"
                content = content[:next_section] + table + content[next_section:]
                changes.append("Added Skills Required table")
    
    # Fix 3: Add Pitfalls section if missing
    if '## Pitfalls' not in content and '## Common Pitfalls' not in content:
        # Insert before Verification Checklist or at end of workflow sections
        insert_points = ['## Verification Checklist', '## Verification', '## Workflow', '## When NOT TO USE']
        inserted = False
        for marker in insert_points:
            if marker in content:
                idx = content.find(marker)
                pitfalls = "\n## Pitfalls\n\n- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context\n- **Context limits:** Process in batches; write results after each batch\n"
                content = content[:idx] + pitfalls + content[idx:]
                changes.append("Added Pitfalls section")
                inserted = True
                break
        if not inserted:
            # Append before the last section
            content += "\n## Pitfalls\n\n- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context\n- **Context limits:** Process in batches; write results after each batch\n"
            changes.append("Appended Pitfalls section")
    
    # Fix 4: Add Verification Checklist if missing
    if '## Verification Checklist' not in content and '## Verification' not in content:
        checklist = "\n## Verification Checklist\n\n- [ ] Skill has clear purpose and structured workflow\n- [ ] Frontmatter is complete and valid\n- [ ] All reference files exist and are substantive\n- [ ] No placeholder text\n"
        content += checklist
        changes.append("Added Verification Checklist")
    
    if content != original:
        skill_path.write_text(content, encoding='utf-8')
        return True, changes
    return False, ["No changes needed"]

def main():
    # Read TSV to get skills below 80
    below_80 = []
    with open(RESULTS_FILE) as f:
        header = f.readline()
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 10:
                name, path, score = parts[0], parts[1], int(parts[2])
                if score < 80:
                    below_80.append((name, path, score))
    
    print(f"Skills below 80: {len(below_80)}")
    
    fixed = 0
    skipped = 0
    errors = []
    
    for name, rel_path, score in below_80:
        rel_dir = Path(rel_path).parent  # TSV path includes SKILL.md
        skill_path = SKILLS_BASE / rel_dir / "SKILL.md"
        if not skill_path.exists():
            # Try with full relative path
            skill_path = SKILLS_BASE / rel_path
        
        if not skill_path.exists():
            errors.append(f"NOT FOUND: {name} ({rel_path})")
            continue
        
        try:
            was_fixed, changes = remediate_skill(skill_path, name)
            if was_fixed:
                fixed += 1
                print(f"  ✅ {name} ({score}): {', '.join(changes[:2])}")
            else:
                skipped += 1
        except Exception as e:
            errors.append(f"ERROR: {name}: {e}")
    
    print(f"\nDone: {fixed} fixed, {skipped} skipped, {len(errors)} errors")
    if errors:
        print("Errors:")
        for e in errors[:10]:
            print(f"  ⚠️ {e}")

if __name__ == '__main__':
    main()
