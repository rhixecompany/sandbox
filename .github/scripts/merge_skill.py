#!/usr/bin/env python3
"""
merge_skill.py — Merge a thin skill into an umbrella skill.
Copies references from absorbed skill to umbrella, updates umbrella's
"Absorbed Skills" section, then archives the absorbed skill.
Phase 3/6 of audit-skills-judge-fix pipeline.

Usage: python merge_skill.py <absorbed_skill_name> <umbrella_skill_name>
"""
import os
import sys
import shutil
import re
from pathlib import Path

SKILLS_ROOT = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")

def find_skill_path(skill_name):
    """Find the canonical path for a skill by name."""
    for root, dirs, files in os.walk(SKILLS_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if os.path.basename(root).lower() == skill_name.lower() and 'SKILL.md' in files:
            return Path(root)
    return None

def read_file(path):
    try:
        return Path(path).read_text(encoding='utf-8')
    except:
        return None

def write_file(path, content):
    Path(path).write_text(content, encoding='utf-8')

def copy_references(absorbed_path, umbrella_path):
    """Copy unique reference files from absorbed skill to umbrella."""
    copied = []
    for ref_type in ['references', 'templates', 'scripts']:
        src_dir = absorbed_path / ref_type
        if not src_dir.exists():
            continue
        dst_dir = umbrella_path / ref_type
        dst_dir.mkdir(exist_ok=True)
        
        for src_file in src_dir.iterdir():
            if src_file.is_file():
                dst_file = dst_dir / src_file.name
                if not dst_file.exists():
                    shutil.copy2(src_file, dst_file)
                    copied.append(f"{ref_type}/{src_file.name}")
                else:
                    # Merge content if file exists
                    existing = read_file(dst_file)
                    new_content = read_file(src_file)
                    if new_content and new_content not in existing:
                        merged = existing + "\n\n---\n\n" + new_content
                        write_file(dst_file, merged)
                        copied.append(f"{ref_type}/{src_file.name} (merged)")
    return copied

def update_umbrella_absorbed_section(umbrella_path, absorbed_name, absorbed_desc):
    """Add absorbed skill to umbrella's 'Recently Absorbed Skills' section."""
    skill_md = umbrella_path / "SKILL.md"
    content = read_file(skill_md)
    if not content:
        return False
    
    absorbed_entry = f"| {absorbed_name} | {absorbed_desc} |"
    
    # Check if section exists
    if re.search(r'##\s*Recently\s*Absorbed\s*Skills', content, re.IGNORECASE):
        # Append to existing section
        lines = content.splitlines()
        in_section = False
        inserted = False
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if re.match(r'##\s*Recently\s*Absorbed\s*Skills', line, re.IGNORECASE):
                in_section = True
                continue
            if in_section and not inserted and line.strip().startswith('|'):
                # Check if already listed
                if absorbed_name in line:
                    inserted = True
                    break
            if in_section and not inserted and (line.strip() == '' or line.startswith('##')):
                # End of table, insert before
                new_lines.insert(-1, absorbed_entry)
                inserted = True
        if not inserted:
            # Add at end of section
            for i, line in enumerate(new_lines):
                if re.match(r'##\s*Recently\s*Absorbed\s*Skills', line, re.IGNORECASE):
                    # Find end of table
                    for j in range(i + 1, len(new_lines)):
                        if new_lines[j].startswith('##') or (new_lines[j].strip() == '' and j > i + 2):
                            new_lines.insert(j, absorbed_entry)
                            break
                    break
        content = '\n'.join(new_lines)
    else:
        # Create new section at end
        section = f"\n\n## Recently Absorbed Skills\n\n| Skill | Description |\n|-------|-------------|\n{absorbed_entry}\n"
        content = content.rstrip() + section
    
    write_file(skill_md, content)
    return True

def main():
    if len(sys.argv) != 3:
        print("Usage: python merge_skill.py <absorbed_skill_name> <umbrella_skill_name>")
        print("Example: python merge_skill.py huggingface-accelerate accelerate")
        sys.exit(1)
    
    absorbed_name = sys.argv[1]
    umbrella_name = sys.argv[2]
    
    print(f"Merging '{absorbed_name}' into '{umbrella_name}'...")
    
    # Find paths
    absorbed_path = find_skill_path(absorbed_name)
    umbrella_path = find_skill_path(umbrella_name)
    
    if not absorbed_path:
        print(f"ERROR: Absorbed skill '{absorbed_name}' not found")
        sys.exit(1)
    if not umbrella_path:
        print(f"ERROR: Umbrella skill '{umbrella_name}' not found")
        sys.exit(1)
    
    print(f"  Absorbed: {absorbed_path}")
    print(f"  Umbrella: {umbrella_path}")
    
    # Get absorbed skill description
    absorbed_fm = {}
    absorbed_content = read_file(absorbed_path / "SKILL.md")
    if absorbed_content:
        fm_match = re.match(r'^---\s*\n(.*?)\n---', absorbed_content, re.DOTALL)
        if fm_match:
            for line in fm_match.group(1).split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    absorbed_fm[k.strip()] = v.strip().strip('"\'')
    
    absorbed_desc = absorbed_fm.get('description', 'No description')
    
    # Copy references
    copied = copy_references(absorbed_path, umbrella_path)
    print(f"  Copied {len(copied)} reference files:")
    for c in copied:
        print(f"    - {c}")
    
    # Update umbrella
    updated = update_umbrella_absorbed_section(umbrella_path, absorbed_name, absorbed_desc)
    if updated:
        print(f"  Updated umbrella SKILL.md with absorbed skill entry")
    
    print(f"\nNext step: Run skill_manage to archive '{absorbed_name}'")
    print(f"  skill_manage(action='delete', name='{absorbed_name}', absorbed_into='{umbrella_name}')")

if __name__ == '__main__':
    main()