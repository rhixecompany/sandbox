# Batch Skill Dependency Injection

> Adding a new skill reference to both `dependencies:` and `skills:` across many prompt/plan files. Companion to Phase 4 of `prompt-management`.

## When to Use

- A new skill was created and all prompt files should reference it
- Migrating from inline execution to subagent-driven-development
- Adding `using-superpowers` or another foundational skill across the library
- Standardizing skill dependency declarations

## Challenge

Each prompt file has a different frontmatter structure:
- Some have BOTH `dependencies:` AND `skills:` sections
- Some have `dependencies:` but NO `skills:` section
- Some have neither (must add both)
- Insertion points vary — `metadata:` blocks with indented items look like list items to naive scanners

## Injection Rules

```
For each prompt file:
  1. Add `- skill:<name>` to `dependencies:` after the last dep item
  2. Add `- <name>` to `skills:` after the last skill item  
  3. If `skills:` doesn't exist, create it right after `dependencies:` block ends
  4. If neither exists, create both before the closing `---`
  5. Verify with `yaml.safe_load` after every batch
  6. Check no duplicate entries
```

## Pitfalls

### 1. Backtick Escaping in Terminal Heredocs
When using `python3 << 'PYEOF'` in bash, backticks inside the Python string are NOT escaped by single-quoted heredoc markers — but they CAN be consumed by earlier shell interpretation if the heredoc marker isn't properly single-quoted. Always use `<< 'PYEOF'` (with quotes) to prevent variable expansion AND backtick command substitution.

**Wrong** (backticks get interpreted by bash):
```bash
python3 << PYEOF
ref = 'Use the `skill-name` skill'
PYEOF
```

**Right** (single-quoted delimiter passes everything literally):
```bash
python3 << 'PYEOF'
ref = 'Use the `skill-name` skill'
PYEOF
```

### 2. read_file Format Breaks Direct Parsing
`read_file` returns content with line-number prefixes (`1|content`), NOT raw file content. You CANNOT parse this as YAML. Use one of:
- `terminal` to run Python that opens the file directly with `open(path)`
- `execute_code` (which reads raw files)
- Direct `cat` piped to `python3 -c`

### 3. Insertion Point Detection Is Fragile
Simple "find last `- ` item" logic fails when:
- `metadata:` contains indented `- ` items (look like list continuations)
- `related_skills:` within `metadata:` has `- ` items
- Blank lines between list items break line-based tracking

**Robust approach:** Track a state machine with `in_deps`, `in_skills`, `in_metadata` flags. Only count `- ` lines when inside the target section. Stop counting when you hit a non-indented non-list line.

### 4. YAML Validation Must Be After Every Batch
Run `yaml.safe_load` on the frontmatter after each batch to catch:
- Entries landing in `toolsets:` or `metadata:` instead of `skills:`
- Duplicate frontmatter keys  
- Broken YAML from misplaced items

### 5. Non-target Files Get Accidentally Modified
If your script iterates ALL `.prompt.md` files but some already have the reference, you may still touch them (inserting blank lines, changing YAML formatting). Use a pre-filter: skip files where `'skill-name' in content`.

### 6. Toolsets Contamination
When adding `- skill-name` to frontmatter, the script may put it in `toolsets:` instead of `skills:` if both sections exist and the scanner loses track of which section it's in. Always verify `toolsets` YAML doesn't contain the new entry.

## Recommended Script Pattern

```python
import yaml, os, glob

def inject_skill(prompt_path: str, skill_name: str, skill_ref: str = None):
    """
    Add a skill reference to both dependencies: and skills: sections.
    - skill_ref: entry in dependencies (default: f'skill:{skill_name}')
    """
    if skill_ref is None:
        skill_ref = f'skill:{skill_name}'
    
    with open(prompt_path) as f:
        content = f.read()
    
    if skill_name in content:
        return  # already present
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return  # no frontmatter
    
    fm_lines = parts[1].split('\n')
    
    # Track state with section awareness
    in_deps = False
    in_skills = False
    in_metadata = False
    in_related = False
    last_dep_idx = None
    last_skill_idx = None
    has_skills_section = False
    
    for i, line in enumerate(fm_lines):
        stripped = line.strip()
        
        # Track section state
        if stripped == 'dependencies:':
            in_deps = True; in_skills = False; continue
        if stripped == 'skills:':
            in_deps = False; in_skills = True; has_skills_section = True; continue
        if stripped in ('metadata:', 'toolsets:', 'tags:', 'tools:'):
            in_deps = False; in_skills = False
            if stripped == 'metadata:': in_metadata = True
            continue
        
        # Record last item in each section
        if in_deps and stripped.startswith('- '):
            last_dep_idx = i
        if in_skills and stripped.startswith('- '):
            last_skill_idx = i
    
    # Apply changes bottom-up to preserve indices
    changes = []
    
    if has_skills_section and last_skill_idx is not None:
        indent = ' ' * (len(fm_lines[last_skill_idx]) - len(fm_lines[last_skill_idx].lstrip()))
        changes.append((last_skill_idx + 1, f'{indent}- {skill_name}'))
    elif not has_skills_section and last_dep_idx is not None:
        indent = ' ' * (len(fm_lines[last_dep_idx]) - len(fm_lines[last_dep_idx].lstrip()))
        # Add skills: section after deps end
        changes.append((last_dep_idx + 1, ''))
        changes.append((last_dep_idx + 2, 'skills:'))
        changes.append((last_dep_idx + 3, f'{indent}- {skill_name}'))
    
    if last_dep_idx is not None:
        indent = ' ' * (len(fm_lines[last_dep_idx]) - len(fm_lines[last_dep_idx].lstrip()))
        changes.append((last_dep_idx + 1, f'{indent}- {skill_ref}'))
    
    # Sort by index descending to insert bottom-up
    changes.sort(key=lambda x: x[0], reverse=True)
    for idx, new_line in changes:
        fm_lines.insert(idx, new_line)
    
    new_frontmatter = '\n'.join(fm_lines)
    new_content = content.replace(parts[1], new_frontmatter, 1)
    
    # Verify
    try:
        yaml.safe_load(new_content.split('---', 2)[1])
    except Exception as e:
        raise ValueError(f'YAML broken after injection: {e}')
    
    with open(prompt_path, 'w') as f:
        f.write(new_content)
```

## Verification

After injection, run this check on all modified files:

```bash
python3 -c "
import yaml, glob
errors = []
for f in glob.glob('prompts/*.prompt.md') + glob.glob('.hermes/plans/*.md'):
    with open(f) as fh:
        parts = fh.read().split('---', 2)
    if len(parts) < 3: continue
    try:
        fm = yaml.safe_load(parts[1])
        s = fm.get('skills', []) or []
        d = fm.get('dependencies', []) or []
        t = fm.get('toolsets', []) or []
        name = fm.get('name', f)
        if '<skill>' in s: errors.append(f'{name}: in skills')
        if 'skill:<skill>' in str(d): errors.append(f'{name}: in deps')
        if '<skill>' in t: errors.append(f'{name}: STILL IN TOOLSETS!')
    except Exception as e:
        errors.append(f'{f}: YAML error: {e}')
if errors:
    for e in errors: print(f'FAIL: {e}')
else:
    print('All clean')
"
```

## Related
- `prompt-management` → Phase 4 (Batch Audit & Enhance)
- `prompt-management/references/prompt-batch-audit-pattern.md` — fixing broken frontmatter (complementary)
