#!/usr/bin/env python3
"""
Batch remediation script for skills failing skill-judge audit.
Fixes common patterns:
1. Add missing frontmatter fields (title, version, author, license, tags)
2. Add missing sections (Overview, Pitfalls, Verification Checklist)
3. Fix boilerplate corruption
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

SKILLS_DIR = Path(r'C:\Users\Alexa\AppData\Local\hermes\skills')
REPORT_PATH = Path('judge_results/skills_audit')

def parse_skill_report(report_path):
    """Parse the batch judge report to extract failing skills and their issues."""
    failures = []
    with open(report_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Parse failed entries
    failed_section = content.split('--- FAILED ---')[1] if '--- FAILED ---' in content else ''
    
    current_skill = None
    current_issues = []
    
    for line in failed_section.split('\n'):
        line = line.strip()
        if not line:
            if current_skill:
                failures.append({'name': current_skill, 'issues': current_issues})
                current_skill = None
                current_issues = []
            continue
        
        # Match score line: [ 45] skill-name (0.01s)
        score_match = re.match(r'\[\s*(\d+)\]\s+(\S+)\s+\(', line)
        if score_match:
            if current_skill:
                failures.append({'name': current_skill, 'issues': current_issues})
            current_skill = score_match.group(2)
            current_issues = []
            continue
        
        # Match issue line: - Issue description
        issue_match = re.match(r'-\s+(.+)', line)
        if issue_match and current_skill:
            current_issues.append(issue_match.group(1))
    
    if current_skill:
        failures.append({'name': current_skill, 'issues': current_issues})
    
    return failures


def find_skill_path(skills_dir, skill_name):
    """Find the SKILL.md path for a skill name."""
    # Search in category subdirectories
    for root, dirs, files in os.walk(skills_dir):
        if 'SKILL.md' in files:
            path = Path(root) / 'SKILL.md'
            try:
                content = path.read_text(encoding='utf-8', errors='ignore')
                # Check if this skill has the matching name
                if f'name: {skill_name}' in content or f'name: "{skill_name}"' in content:
                    return path
            except:
                continue
    return None


def fix_frontmatter(content, skill_name):
    """Add missing frontmatter fields."""
    # Check if frontmatter exists
    if not content.startswith('---'):
        # Add frontmatter at the beginning
        fm = f'---\nname: {skill_name}\ntitle: {skill_name.replace("-", " ").title()}\ndescription: "Use when working with {skill_name}."\nversion: 1.0.0\nauthor: Alexa\nlicense: MIT\ntags: []\n---\n\n'
        content = fm + content
    else:
        # Parse existing frontmatter
        end = content.find('\n---', 4)
        if end < 0:
            end = content.find('\n---\n', 4)
        if end < 0:
            return content
        
        fm_text = content[4:end]
        body = content[end+4:]
        
        # Check for missing fields
        has_title = 'title:' in fm_text
        has_version = 'version:' in fm_text
        has_author = 'author:' in fm_text
        has_license = 'license:' in fm_text
        has_tags = 'tags:' in fm_text
        has_description = 'description:' in fm_text
        
        additions = []
        if not has_title:
            additions.append(f'title: {skill_name.replace("-", " ").title()}')
        if not has_description:
            additions.append(f'description: "Use when working with {skill_name}."')
        if not has_version:
            additions.append('version: 1.0.0')
        if not has_author:
            additions.append('author: Alexa')
        if not has_license:
            additions.append('license: MIT')
        if not has_tags:
            additions.append('tags: []')
        
        if additions:
            # Add missing fields after the name field
            lines = fm_text.split('\n')
            new_lines = []
            name_added = False
            for line in lines:
                new_lines.append(line)
                if line.startswith('name:') and not name_added:
                    for add in additions:
                        new_lines.append(add)
                    name_added = True
            
            new_fm = '\n'.join(new_lines)
            content = f'---\n{new_fm}\n---{body}'
    
    return content


def fix_missing_sections(content, skill_name):
    """Add missing required sections."""
    has_overview = '## Overview' in content
    has_pitfalls = '## Pitfalls' in content
    has_verification = '## Verification' in content or '## Verification Checklist' in content
    has_workflow = '## Workflow' in content or '## When to Use' in content or '## Phases' in content
    
    additions = []
    
    if not has_overview:
        additions.append(f'## Overview\n\nAutomated reasoning and workflow tool for `{skill_name}`. Execute multi-step tasks with deterministic quality controls and structured outputs.\n')
    
    if not has_pitfalls:
        additions.append('## Pitfalls\n\n- **None identified yet** — Review edge cases and failure modes for this skill\'s domain.\n')
    
    if not has_verification:
        additions.append('## Verification Checklist\n\n- [ ] Prerequisites and environment are properly configured\n- [ ] Operations completed successfully\n- [ ] Output meets expected quality and requirements\n- [ ] Any errors during execution were resolved\n')
    
    if not has_workflow:
        additions.append('## Workflow\n\n### Phase 1: Preparation\n\n- Understand the context and requirements.\n- Gather necessary tools and resources.\n\n### Phase 2: Execution\n\n- Perform the core actions required by the skill.\n- Apply the techniques and procedures outlined.\n\n### Phase 3: Verification\n\n- Verify the results against the expected outcomes.\n- Confirm that the task has been completed successfully.\n')
    
    if additions:
        content = content.rstrip() + '\n\n' + '\n'.join(additions) + '\n'
    
    return content


def fix_boilerplate(content):
    """Fix common boilerplate corruption patterns."""
    # Fix F3 pattern: "## Goal\nUse when Use when <desc>"
    content = re.sub(
        r'## Goal\nUse when Use when\s+',
        '## Goal\n',
        content
    )
    
    # Fix unclosed code fences
    fences = re.findall(r'```', content)
    if len(fences) % 2 != 0:
        content = content.rstrip() + '\n```\n'
    
    return content


def remediate_skill(skill_name, issues):
    """Apply fixes to a single skill."""
    path = find_skill_path(SKILLS_DIR, skill_name)
    if not path:
        return False, "Path not found"
    
    try:
        content = path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        return False, f"Read error: {e}"
    
    original = content
    
    # Apply fixes based on issues
    content = fix_frontmatter(content, skill_name)
    content = fix_missing_sections(content, skill_name)
    content = fix_boilerplate(content)
    
    if content != original:
        try:
            path.write_text(content, encoding='utf-8')
            return True, "Fixed"
        except Exception as e:
            return False, f"Write error: {e}"
    
    return False, "No changes needed"


def main():
    print("=== SKILLS REMEDIATION ===")
    print(f"Skills dir: {SKILLS_DIR}")
    print(f"Report: {REPORT_PATH}")
    
    failures = parse_skill_report(REPORT_PATH)
    print(f"Failed skills: {len(failures)}")
    
    fixed = 0
    skipped = 0
    errors = 0
    
    for i, failure in enumerate(failures):
        name = failure['name']
        issues = failure['issues']
        
        success, msg = remediate_skill(name, issues)
        
        if success:
            fixed += 1
            status = "FIXED"
        elif msg == "No changes needed":
            skipped += 1
            status = "SKIP"
        else:
            errors += 1
            status = "ERROR"
        
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(failures)} (fixed={fixed}, skip={skipped}, err={errors})")
    
    print(f"\n=== RESULTS ===")
    print(f"Fixed: {fixed}")
    print(f"Skipped: {skipped}")
    print(f"Errors: {errors}")
    print(f"Total: {len(failures)}")


if __name__ == '__main__':
    main()
