# Stub Detection & Uninstall Patterns

## Detecting Auto-Generated `-script` Stubs

Hermes auto-generates placeholder skills for every Python script in `~/AppData/Local/hermes/scripts/`. These skills:
- End in `-script` suffix (e.g., `fix-frontmatter-script`, `audit-prompts-script`)
- Have placeholder descriptions: "Placeholder skill for the foo.py script"
- Have a corresponding non-script equivalent already installed in a categorized subdirectory (e.g., `development/fix-frontmatter`, `development/audit-prompts`)
- Carry no standalone value as skills — the actual script runs directly

The non-script equivalents are **always** in a category subdirectory under `~/AppData/Local/hermes/skills/<category>/<name>/`, while stubs sit at the root: `~/AppData/Local/hermes/skills/<name>-script/`.

## Detection Workflow

```bash
# List all -script stubs
hermes skills list --source local | grep "\-script"

# Verify each has a non-script equivalent
python3 -c "
import os
root = os.path.expanduser('~/AppData/Local/hermes/skills')
all_skills = {d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and os.path.exists(os.path.join(root, d, 'SKILL.md'))}
script_skills = [s for s in all_skills if s.endswith('-script')]
for ss in sorted(script_skills):
    base = ss.replace('-script', '')
    equiv = '✅ HAS EQUIV' if base in all_skills else '⬜ NO EQUIV — UNIQUE SKILL'
    print(f'{equiv}: {ss} → {base}')
print(f'Total: {len(script_skills)}')
"
```

## Removal Process

### Step 1: Uninstall from registry

```bash
echo "y" | hermes skills uninstall "<name>-script"
```

### Step 2: Delete on-disk directory

**Critical:** `hermes skills uninstall` removes the skill from the internal registry only — it does NOT delete the directory. Files remain on disk and the skill will re-appear on the next `hermes skills list` unless you also remove the directory.

```bash
rm -rf ~/AppData/Local/hermes/skills/<name>-script
```

Verify:
```bash
find ~/AppData/Local/hermes/skills -maxdepth 1 -type d -name "*-script" | wc -l
# Should be 0
```

### Batch removal

```bash
for skill in $(find ~/AppData/Local/hermes/skills -maxdepth 1 -type d -name "*-script"); do
  name=$(basename "$skill")
  echo "y" | hermes skills uninstall "$name"
  rm -rf "$skill"
  echo "  Removed $name"
done
```

## Pitfalls

- **Uninstall does not delete files**: Always run `rm -rf` after uninstall. Without it, the on-disk copy survives and the skill re-appears.
- **Non-script equivalents must exist first**: Before removing a `-script` stub, confirm the non-script version exists. Use the detection script above.
- **Category subdirectory stubs**: Some `-script` stubs may live inside category dirs too (e.g., `development/batch-skill-judge-script/`). These should also be removed — the non-script `batch-skill-judge` in the same category replaces them.
- **Security scanner blocks agent config file references**: Community skills (skills-sh) referencing agent configuration or profile files trigger a DANGEROUS verdict. No `--force` override exists. Use trusted-source (official, OpenAI, NVIDIA) install for those.
