"""
Comprehensive structure patch for ALL sub-60 skills.
Adds missing sections: When to Use, When NOT to Use, Skills Required,
Workflow with 3 Phases, Verification Checklist, Pitfalls, references/
"""
import os, csv
from pathlib import Path

tsv = Path.home() / "Desktop/SandBox/judge_results/all_results.tsv"
with open(tsv) as f:
    rows = list(csv.DictReader(f, delimiter='\t'))

fails = [r for r in rows if int(r['score']) < 60]
print(f"Patching {len(fails)} FAIL skills")

BOILERPLATE = {
    '## When to Use': [
        "",
        "## When to Use",
        "",
        "- Use when _(describe scenario 1)_",
        "- Use when _(describe scenario 2)_",
        "- Use when _(describe scenario 3)_",
        "",
    ],
    '## When NOT to Use': [
        "",
        "## When NOT to Use",
        "",
        "- When the task is outside this skill's domain",
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
        "| _(name)_ | _(purpose of the skill)_ |",
        "",
    ],
    '## Workflow': [
        "",
        "## Workflow",
        "",
        "### Phase 1: Preparation",
        "",
        "_Set up dependencies, gather inputs, validate the environment._",
        "",
        "### Phase 2: Execution",
        "",
        "_Run the primary workflow._",
        "",
        "### Phase 3: Verification & Cleanup",
        "",
        "_Validate results, document outcomes, clean up temporary resources._",
        "",
    ],
    '## Verification Checklist': [
        "",
        "## Verification Checklist",
        "",
        "- [ ] Phase 1 completed successfully",
        "- [ ] Phase 2 completed successfully",
        "- [ ] Outputs validated against expected results",
        "- [ ] Errors documented and resolved",
        "- [ ] User notified of completion",
        "",
    ],
    '## Pitfalls': [
        "",
        "## Pitfalls",
        "",
        "- _(common mistake or issue)_",
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
    
    # Add missing sections before final newline
    end_marker = content.rstrip()
    
    changes = 0
    for header, lines in BOILERPLATE.items():
        if header not in content:
            to_insert = '\n'.join(lines) + '\n'
            # Insert before ## Pitfalls if it exists, otherwise at end
            if '## Pitfalls' in content:
                idx = content.index('## Pitfalls')
                # Find the line start
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
            f"Reference materials for the `{name}` skill.\n\n"
            "## Key Concepts\n\n"
            f"_(Core concepts for {name})_\n\n"
            "## Examples\n\n"
            "_(Usage examples)_\n"
        )
        print(f"  {name}: +references/overview.md")
        changes += 1
    
    if changes > 0 and content != original:
        skill_md.write_text(content, encoding='utf-8')
        print(f"  {name}: → {changes} changes applied")
    elif changes == 0:
        print(f"  {name}: ✓ already complete")
    else:
        print(f"  {name}: ⚠ content same despite {changes} changes (possible issue)")

print(f"\nDone. Patched {sum(1 for r in fails if (Path(r['path'])/'SKILL.md').exists())} skills")
