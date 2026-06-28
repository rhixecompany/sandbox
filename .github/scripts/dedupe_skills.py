#!/usr/bin/env python3
"""
dedupe_skills.py — Find duplicate SKILL.md files across skill directories.
Identifies skills with the same name in multiple locations.
Phase 3 of audit-skills-judge-fix pipeline.
"""
import os
import json
from pathlib import Path
from collections import defaultdict

SKILLS_ROOT = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
OUTPUT_FILE = Path(r"C:\Users\Alexa\Desktop\SandBox\docs\dedupe-report.md")

def find_all_skills():
    """Find all SKILL.md files and group by skill name."""
    skills = defaultdict(list)
    for root, dirs, files in os.walk(SKILLS_ROOT):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if 'SKILL.md' in files:
            skill_name = os.path.basename(root)
            skill_path = os.path.join(root, 'SKILL.md')
            try:
                with open(skill_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                lines = len(content.splitlines())
                size = len(content)
            except:
                lines = 0
                size = 0
            rel_path = os.path.relpath(root, SKILLS_ROOT)
            skills[skill_name].append({
                'path': root,
                'rel_path': rel_path,
                'lines': lines,
                'size': size,
                'in_category': '\\' in rel_path or '/' in rel_path
            })
    return skills

def main():
    print("Scanning for duplicate skills...")
    all_skills = find_all_skills()
    
    # Find duplicates (same name, multiple paths)
    duplicates = {name: paths for name, paths in all_skills.items() if len(paths) > 1}
    
    # Find potential overlaps (similar names)
    name_groups = defaultdict(list)
    for name in all_skills:
        # Group by base name (remove -cli, -skill, -generator suffixes)
        base = name.replace('-cli', '').replace('-skill', '').replace('-generator', '').replace('-search', '')
        name_groups[base].append(name)
    
    overlaps = {base: names for base, names in name_groups.items() if len(names) > 1}
    
    # Generate report
    report = []
    report.append("# Deduplication Report\n")
    report.append(f"**Total unique skill names:** {len(all_skills)}\n")
    report.append(f"**Skills with duplicate paths:** {len(duplicates)}\n")
    report.append(f"**Potential overlaps (similar names):** {len(overlaps)}\n\n")
    
    report.append("## Duplicate Paths (Same Name, Multiple Locations)\n")
    report.append("| Skill | Paths | Lines | Canonical? |\n")
    report.append("|-------|-------|-------|------------|\n")
    for name, paths in sorted(duplicates.items()):
        for p in paths:
            canonical = "✅" if p['in_category'] else "❌"
            report.append(f"| {name} | {p['rel_path']} | {p['lines']} | {canonical} |\n")
    
    report.append("\n## Potential Overlaps (Similar Names)\n")
    report.append("| Base Name | Variants | Action |\n")
    report.append("|-----------|----------|--------|\n")
    for base, names in sorted(overlaps.items()):
        if len(names) > 1:
            report.append(f"| {base} | {', '.join(sorted(names))} | Review |\n")
    
    report.append("\n## Recommended Actions\n")
    report.append("1. For duplicate paths: Keep the version in the category subdirectory (✅)\n")
    report.append("2. For overlaps: Merge thin skills into the fuller version\n")
    report.append("3. Use `skill_manage(action='delete', absorbed_into='<umbrella>')` for merges\n")
    report.append("4. Use `rm -rf` for true duplicates with identical content\n")
    
    report_text = ''.join(report)
    OUTPUT_FILE.write_text(report_text, encoding='utf-8')
    
    print(f"\nReport written to {OUTPUT_FILE}")
    print(f"Duplicate paths: {len(duplicates)}")
    print(f"Potential overlaps: {len(overlaps)}")
    
    # Print summary
    print("\n=== Duplicate Paths ===")
    for name, paths in sorted(duplicates.items()):
        print(f"\n  {name}:")
        for p in paths:
            print(f"    {p['rel_path']} ({p['lines']} lines)")
    
    print("\n=== Potential Overlaps ===")
    for base, names in sorted(overlaps.items()):
        if len(names) > 1:
            print(f"  {base}: {', '.join(sorted(names))}")

if __name__ == '__main__':
    main()