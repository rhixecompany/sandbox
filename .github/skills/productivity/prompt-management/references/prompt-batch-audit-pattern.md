# Prompt Batch Audit & Enhance Pattern

> Companion to Phase 4 of `prompt-management`. Captures the exact workflow used to audit and fix 249 prompt files in a single session.

## When to Use This Pattern

- A prompt directory has 10+ files with inconsistent frontmatter
- Migrating from Copilot-style (`agent:`, `model:`, `tools:`) to Hermes-standard frontmatter
- Adding missing metadata fields (`name:`, `title:`, `version:`, `author:`, `license:`) across a library
- Stripping redundant `## Legacy Prompt Details` sections
- Standardizing `tags:` format from Python-list `[a, b]` to proper YAML arrays
- Standardizing dependency prefixes (`command:/tool:` → `skill:`)

## Workflow Overview

```
Inventory → Aggregate scan → Write fix script → Dry-run → Apply → Verify
```

## Common Frontmatter Issues Detected

| Issue | Detection | Fix |
|-------|-----------|-----|
| Missing YAML frontmatter | `head -1` not `---` | Add full block with all required fields |
| Missing `name:` | `grep "^name:"` absent | Derive from filename (strip `.prompt.md`) |
| Missing `title:` | `grep "^title:"` absent | Derive from H1 heading or filename |
| Missing `version:` | `grep "^version:"` absent | Default to `1.0.0` |
| Missing `author:`/`license:` | `grep` absent | Default to `Hermes Agent` / `MIT` |
| Python-list `tags: [a, b]` | `tags:` line contains `[` | Convert to YAML list: `tags:\n  - a\n  - b` |
| Empty `tags:` (no value) | `^tags:\s*$` and next line not `  -` | Emit `tags: []` |
| Legacy section (`##`/`###`) | `grep "Legacy Prompt Details"` | Strip section with regex |
| `command:`/`tool:` prefix in deps | `dependencies:` has `command:` or `tool:` | Rewrite to `skill:` prefix |

## Fix Script Structure

The reusable script at `~/AppData/Local/hermes/scripts/fix_prompts.py` follows this shape:

```python
# 1. Parse frontmatter: split into fm_lines, body_lines
# 2. For each required field (name, title, version, author, license):
#    if missing: insert at position 0
# 3. fix_tags_format(): convert `tags: [...]` to YAML list; fix empty tags
# 4. standardize_dep_prefixes(): command:/tool: → skill:
# 5. remove_legacy_section(): regex strip `##`/`### Legacy Prompt Details`
# 6. Rebuild frontmatter + body, write file
# 7. Support --dry-run (preview only) and --batch=N (process subset)
```

## Critical Edge Cases

- **`### Legacy Prompt Details`** (H3 heading, not H2) — regex must use `#{2,3}` not just `##`
- **Files with `tags:` in valid YAML list format** — don't convert to inline `[]`. Check next line starts with `  - <item>`.
- **`.txt` files** in prompts dir — skip entirely; they are raw source references, not prompts
- **`plan-batchFixAllErrorsWarningsAndDeprecations.prompt.md`** — rename to a sane short name
- **`Developement.prompt.md`** — rename to `development.prompt.md`
- **`tags: []` followed by `  - hermes`** — don't leave `tags: []` above list items; merge to `tags: [hermes, ...]` or remove `[]`

## Performance Notes

- 249 files × 12 grep checks via `for f in *.prompt.md` loops = timeout risk
- Prefer bulk `grep -rl` / `grep -l` for aggregate scans
- For fix operations, one Python script processing all files in memory is faster than 249 individual `patch` calls
- Use `execute_code` for bulk analysis; use `terminal` for running the fix script
