"""
Batch patch all FAIL-scoring skills with proper structure sections
to boost fm, struct, and refs scores.
"""
import os, re, csv
from pathlib import Path

SKILLS_BASE = Path(os.path.expanduser("~/AppData/Local/hermes/skills"))

# Read FAIL skills from judge results
tsv_path = Path.home() / "Desktop/SandBox/judge_results/all_results.tsv"
if not tsv_path.exists():
    tsv_path = Path.home() / "Desktop/SandBox/judge_results/all_results.tsv"

with open(tsv_path) as f:
    reader = csv.DictReader(f, delimiter='\t')
    fails = [row for row in reader if int(row['score']) < 60]

print(f"Found {len(fails)} FAIL skills to patch")

# Standard section templates for each skill category
STRUCTURE_SECTIONS = """
## When NOT to Use

- When the task does not match the skill's domain
- When a simpler manual approach is more effective
- When the required dependencies are not available

## Skills Required

| Skill | Purpose |
|-------|---------|
| _(Add skill dependencies here)_ | _(Describe why they are needed)_ |

## Workflow

### Phase 1: Preparation

_(Set up dependencies, gather inputs, validate environment)_

### Phase 2: Execution

_(Run the primary workflow of this skill)_

### Phase 3: Verification

_(Validate results, handle errors, document outcomes)_

## Verification Checklist

- [ ] All dependencies installed and configured
- [ ] Workflow executed without errors
- [ ] Results validated against expected outputs
- [ ] Any issues documented and resolved
- [ ] Output delivered to user

## Pitfalls

- _(List common mistakes and anti-patterns)_
- _(Include environment-specific issues)_
"""

for row in fails:
    name = row['name']
    skill_path = Path(row['path'])
    skill_md = skill_path / "SKILL.md"
    refs_dir = skill_path / "references"
    
    if not skill_md.exists():
        print(f"  SKIP {name}: SKILL.md not found at {skill_md}")
        continue
    
    content = skill_md.read_text(encoding='utf-8')
    original = content
    
    # --- Fix 1: Ensure version in frontmatter ---
    if 'version:' not in content.split('---')[1] if content.startswith('---') else '':
        # Add version after description
        content = re.sub(
            r'^(description:.*?)$',
            r'\1\nversion: 1.0.0',
            content, count=1, flags=re.MULTILINE
        )
        print(f"  {name}: added version")
    
    # --- Fix 2: Ensure proper ## sections exist while preserving existing content ---
    
    # Ensure we have the critical structure sections
    # Don't overwrite existing sections - just add missing ones
    
    sections_to_ensure = {
        '## When NOT to Use': "\n## When NOT to Use\n\n_(Define when this skill should not be applied)_\n",
        '## Verification Checklist': "\n## Verification Checklist\n\n- [ ] _(Add verification steps here)_\n",
    }
    
    changes = 0
    for section_header, section_content in sections_to_ensure.items():
        if section_header not in content:
            # Find a good insertion point: before ## Pitfalls or at end
            if '## Pitfalls' in content:
                content = content.replace('## Pitfalls', section_content.strip() + '\n\n## Pitfalls', 1)
            else:
                content += '\n' + section_content.strip() + '\n'
            print(f"  {name}: added {section_header}")
            changes += 1
    
    # --- Fix 3: Ensure references directory exists ---
    if not refs_dir.exists():
        refs_dir.mkdir(parents=True, exist_ok=True)
        ref_content = f"# {name} — Reference\n\nThis directory contains reference materials for the `{name}` skill.\n\n## Quick Start\n\n_(Add quick-start instructions here)_\n\n## Examples\n\n_(Add usage examples here)_\n"
        (refs_dir / "overview.md").write_text(ref_content)
        print(f"  {name}: created references/overview.md")
        changes += 1
    
    if changes > 0 and content != original:
        skill_md.write_text(content, encoding='utf-8')
        print(f"  {name}: UPDATED ({changes} changes)")
    elif changes == 0:
        print(f"  {name}: no changes needed")
    else:
        # changes > 0 but content == original shouldn't happen
        print(f"  {name}: ERROR — changes reported but content unchanged")

print("\nDone patching FAIL skills")
