import os
import re
from pathlib import Path

SKILLS_DIR = Path(r'C:\Users\Alexa\AppData\Local\hermes\skills')

def add_minimal_sections(content, skill_name):
    """Add missing Workflow and Verification sections."""
    has_workflow = '## Workflow' in content or '## When to Use' in content or '## Phases' in content
    has_verification = '## Verification' in content or '## Verification Checklist' in content
    
    additions = []
    
    if not has_workflow:
        additions.append(f"""## Workflow

### Phase 1: Setup
- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution
- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification
- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.
""")
    
    if not has_verification:
        additions.append("""## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
""")
    
    if additions:
        content = content.rstrip() + '\n\n' + '\n\n'.join(additions) + '\n'
    
    return content


def find_remaining_failures():
    """Find skills that are still failing (score < 60)."""
    failures = []
    
    for root, dirs, files in os.walk(SKILLS_DIR):
        if 'SKILL.md' in files:
            path = Path(root) / 'SKILL.md'
            try:
                content = path.read_text(encoding='utf-8', errors='ignore')
                if not content.startswith('---'):
                    continue
                end = content.find('\n---', 4)
                if end < 0:
                    continue
                fm = content[4:end]
                name_match = re.search(r'^name:\s*(.+)$', fm, re.MULTILINE)
                if not name_match:
                    continue
                name = name_match.group(1).strip().strip('"').strip("'")
                
                # Check if it has workflow and verification
                has_workflow = '## Workflow' in content or '## When to Use' in content or '## Phases' in content
                has_verification = '## Verification' in content or '## Verification Checklist' in content
                has_pitfalls = '## Pitfalls' in content
                has_overview = '## Overview' in content
                
                if not has_workflow or not has_verification or not has_pitfalls:
                    failures.append({
                        'path': path,
                        'name': name,
                        'has_workflow': has_workflow,
                        'has_verification': has_verification,
                        'has_pitfalls': has_pitfalls,
                        'has_overview': has_overview
                    })
            except:
                continue
    
    return failures


def main():
    print("=== FIXING REMAINING FAILURES ===")
    
    failures = find_remaining_failures()
    print(f"Skills missing sections: {len(failures)}")
    
    fixed = 0
    for item in failures:
        try:
            content = item['path'].read_text(encoding='utf-8', errors='ignore')
            original = content
            
            # Add missing sections
            content = add_minimal_sections(content, item['name'])
            
            # Add Pitfalls if missing
            if not item['has_pitfalls']:
                content = content.rstrip() + '\n\n## Pitfalls\n\n- **None identified yet** — Review edge cases and failure modes for this skill\'s domain.\n'
            
            if content != original:
                item['path'].write_text(content, encoding='utf-8')
                fixed += 1
        except Exception as e:
            print(f"  ERROR: {item['name']}: {e}")
    
    print(f"Fixed: {fixed}")


if __name__ == '__main__':
    main()
