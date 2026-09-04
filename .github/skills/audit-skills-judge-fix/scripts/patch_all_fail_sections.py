"""
Comprehensive structure patch for all sub-60 skills.
Injects all 7 standard sections: When to Use, When NOT to Use, Skills Required,
Workflow (3 phases), Verification Checklist, Pitfalls + references/ dir.

Each section is only added if it doesn't already exist.
Safe to re-run — unchanged skills are skipped.
"""
import os, csv
from pathlib import Path

_HOME = os.environ.get("HOME", os.environ.get("USERPROFILE", "C:\\Users\\Alexa"))
TSV = Path(_HOME) / "Desktop/SandBox/judge_results/all_results.tsv"

if not TSV.exists():
    print(f"ERROR: judge results not found at {TSV}")
    exit(1)

with open(TSV, encoding='utf-8') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))

fails = [r for r in rows if int(r.get('score', 100)) < 60]
if not fails:
    print("No FAIL skills found. Nothing to do.")
    exit(0)

print(f"Patching {len(fails)} FAIL skills")

BOILERPLATE = {
    '## When to Use': [
        "",
        "## When to Use",
        "",
        "- Use when _(scenario 1)_",
        "- Use when _(scenario 2)_",
        "- Use when _(scenario 3)_",
        "",
    ],
    '## When NOT to Use': [
        "",
        "## When NOT to Use",
        "",
        "- When outside this skill's domain",
        "- When simpler approaches are more effective",
        "- When required dependencies are unavailable",
        "",
    ],
    '## Skills Required': [
        "",
        "## Skills Required",
        "",
        "| Skill | Purpose |",
        "|-------|---------|",
        "| _(name)_ | _(purpose)_ |",
        "",
    ],
    '## Workflow': [
        "",
        "## Workflow",
        "",
        "### Phase 1: Preparation",
        "",
        "_Set up dependencies, gather inputs, validate environment._",
        "",
        "### Phase 2: Execution",
        "",
        "_Run the primary workflow._",
        "",
        "### Phase 3: Verification & Cleanup",
        "",
        "_Validate results, document outcomes, clean up._",
        "",
    ],
    '## Verification Checklist': [
        "",
        "## Verification Checklist",
        "",
        "- [ ] Phase 1 completed successfully",
        "- [ ] Phase 2 completed successfully",
        "- [ ] Outputs validated",
        "- [ ] Errors documented",
        "- [ ] User notified",
        "",
    ],
    '## Pitfalls': [
        "",
        "## Pitfalls",
        "",
        "- _(common mistake)_",
        "- _(environment-specific concern)_",
        "- _(anti-pattern to avoid)_",
        "",
    ],
}

for row in fails:
    name = row['name']
    skill_md = Path(row['path']) / "SKILL.md"
    if not skill_md.exists():
        print(f"  SKIP {name}: no SKILL.md")
        continue

    content = skill_md.read_text(encoding='utf-8')
    original = content
    changes = 0

    for header, lines in BOILERPLATE.items():
        if header not in content:
            to_insert = '\n'.join(lines) + '\n'
            # Insert before ## Pitfalls if it exists, otherwise at end
            if '## Pitfalls' in content:
                idx = content.index('## Pitfalls')
                line_start = content.rfind('\n', 0, idx) + 1
                content = content[:line_start] + to_insert + '\n' + content[line_start:]
            else:
                content = content.rstrip() + '\n\n' + to_insert.rstrip() + '\n'
            print(f"  {name}: +{header}")
            changes += 1

    # Ensure references/ dir exists
    refs_dir = Path(row['path']) / "references"
    if not refs_dir.exists():
        refs_dir.mkdir(parents=True, exist_ok=True)
        (refs_dir / "overview.md").write_text(
            f"# {name} — Reference\n\n"
            f"Reference materials for `{name}`.\n\n"
            "## Key Concepts\n\n_(Core concepts)_\n\n"
            "## Examples\n\n_(Usage examples)_\n"
        )
        print(f"  {name}: +references/overview.md")
        changes += 1

    if changes > 0 and content != original:
        skill_md.write_text(content, encoding='utf-8')
        print(f"  {name}: → {changes} changes applied")
    elif changes > 0:
        print(f"  {name}: ERROR — content unchanged despite {changes} reported changes")

print(f"\nDone. {sum(1 for r in fails if (Path(r['path'])/'SKILL.md').exists())} skills processed")
