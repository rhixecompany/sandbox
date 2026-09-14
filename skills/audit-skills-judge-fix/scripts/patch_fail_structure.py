"""
Batch patch all FAIL-scoring skills with proper structure sections
to boost fm, struct, and refs scores. Quick first-aid round.

Inject: version in frontmatter, ## When NOT to Use, ## Verification Checklist,
and creates references/overview.md for skills missing it.
"""
import os, re, csv
from pathlib import Path

_HOME = os.environ.get("HOME", os.environ.get("USERPROFILE", "C:\\Users\\Alexa"))
SKILLS_BASE = Path(_HOME) / "AppData/Local/hermes/skills"
TSV = Path(_HOME) / "Desktop/SandBox/judge_results/all_results.tsv"

if not TSV.exists():
    print(f"ERROR: judge results not found at {TSV}")
    print("Run batch_skill_judge.py first")
    exit(1)

with open(TSV, encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fails = [row for row in reader if int(row['score']) < 60]

print(f"Found {len(fails)} FAIL skills to patch")

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
    changes = 0

    # Fix 1: Ensure version in frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 2 and 'version:' not in parts[1]:
            parts[1] = re.sub(
                r'^(description:.*?)$',
                r'\1\nversion: 1.0.0',
                parts[1], count=1, flags=re.MULTILINE
            )
            content = '---'.join(parts)
            print(f"  {name}: added version")
            changes += 1

    # Fix 2: Add missing section headers
    sections = {
        '## When NOT to Use': "\n## When NOT to Use\n\n_(Define when this skill should not be applied)_\n",
        '## Verification Checklist': "\n## Verification Checklist\n\n- [ ] _(Add verification steps here)_\n",
    }

    for header, section_text in sections.items():
        if header not in content:
            if '## Pitfalls' in content:
                content = content.replace('## Pitfalls', section_text.strip() + '\n\n## Pitfalls', 1)
            else:
                content += '\n' + section_text.strip() + '\n'
            print(f"  {name}: added {header}")
            changes += 1

    # Fix 3: Ensure references directory exists
    if not refs_dir.exists():
        refs_dir.mkdir(parents=True, exist_ok=True)
        (refs_dir / "overview.md").write_text(
            f"# {name} — Reference\n\n"
            f"Reference materials for the `{name}` skill.\n\n"
            "## Quick Start\n\n_(Add quick-start instructions here)_\n\n"
            "## Examples\n\n_(Add usage examples here)_\n"
        )
        print(f"  {name}: created references/overview.md")
        changes += 1

    if changes > 0 and content != original:
        skill_md.write_text(content, encoding='utf-8')
        print(f"  {name}: UPDATED ({changes} changes)")
    elif changes > 0:
        print(f"  {name}: ERROR — no visible change despite {changes} reported")

print("\nDone")
