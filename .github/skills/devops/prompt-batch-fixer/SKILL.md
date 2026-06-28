---
author: Alexa
description: Use when batch-processing markdown prompt files — adding YAML frontmatter,
  fixing tags format, stripping legacy sections, standardizing dependency prefixes,
  renaming typo filenames, or re-verifying all prompts after fixes.
license: MIT
name: prompt-batch-fixer
tags:
- prompts
- batch
- fix
- yaml
- frontmatter
- verification
title: Prompt Batch Fixer
version: 1.0.0

---

# Prompt Batch Fixer

## When to Use
- Batch-processing 100+ prompt files that need YAML frontmatter standardization
- Adding name/title/version to prompt files missing required fields
- Converting Python-list tags (`tags: [a, b]`) to proper YAML arrays
- Stripping redundant `## Legacy Prompt Details` sections
- Standardizing dependency prefix formats (`command:`, `tool:` → `skill:`)
- Renaming typo/overly-long filenames
- Re-verifying post-fix state

## When NOT to Use
- Single-file edits (use patch instead)
- Raw .txt reference files (leave untouched)

## Workflow

### Phase 1: Audit
1. Get file count: `ls -1 *.prompt.md | wc -l`
2. Scan for common issues:
   ```
   # Missing YAML frontmatter
   grep -c "^---" *.prompt.md | grep ":0$"
   # Missing name/title/version fields
   for f in *.prompt.md; do head -20 "$f" | grep -q "^name:" || echo "$f"; done
   # Legacy sections
   grep -rl "Legacy Prompt Details" *.prompt.md
   # Tags in Python-list format
   grep -l "tags:" *.prompt.md | head -10
   # Typo filenames
   ls *[A-Z]*.prompt.md
   ```
3. Check template directories exist for referenced files

### Phase 2: Fix Script
1. Create Python fix script at `~/AppData/Local/hermes/scripts/fix_<target>.py`
2. Handle these common issues:
   - Missing YAML frontmatter: add complete `---` block with all required fields
   - Empty tags: `tags:` → `tags: []`
   - Python-list tags: `tags: [a, b]` → YAML array format
   - Legacy sections: strip `## Legacy Prompt Details` and any content until next `##`
   - Dep prefix standardization: `command:` / `tool:` → `skill:`
   - Add missing fields: `name:`, `title:`, `version: 1.0.0`, `author:`, `license: MIT`
3. Use `--batch N` flag for incremental processing
4. Handle CRLF line endings on Windows (use `'rb'`/`'wb'` modes)

### Phase 3: Execute
```
python3 ~/AppData/Local/hermes/scripts/fix_prompts.py
```
Run dry-run first: `--dry-run` flag

### Phase 4: Verify
```
# Verify all have name/version
for f in *.prompt.md; do head -5 "$f" | grep -q "^name:" || echo "MISSING: $f"; done
# Verify no legacy sections remain
grep -rl "Legacy Prompt" *.prompt.md
# Verify no empty tags
grep -rlP "^tags:\s*$" *.prompt.md
```

## Pitfalls
- **CRLF on Windows**: Python `read_file`/`write_file` tools handle this fine, but direct `open()` needs `'rb'`/`'wb'` modes
- **git revert first**: If a fix damages files, revert with `git checkout -- *.prompt.md` before re-running
- **.txt files**: These are raw source references — skip them for YAML frontmatter additions
- **False positives**: `tags:` followed by YAML list items (`  - item`) is VALID — don't replace with `tags: []`
- **Duplicate tags**: Running `fix_tags_format` then `update_field` for tags can create duplicates — check for this
- **`generator-orchestrator.prompt.md` edge case**: Use `###` level heading for Legacy section detection too

## Script Location
Scripts go in: `~/AppData/Local/hermes/scripts/fix_*.py`

## Recently Absorbed Skills
- `fix-yaml-frontmatter` (2026-06-25) — YAML frontmatter repair for skills with broken description quoting

## Verification Checklist
- [ ] All target files have valid YAML frontmatter
- [ ] name, title, version: 1.0.0, author, license fields present
- [ ] No `## Legacy Prompt Details` sections remaining
- [ ] Tags use valid YAML format (not Python list `[...]`)
- [ ] Dependency prefixes standardized
- [ ] No empty `tags:` (use `tags: []` instead)
- [ ] .txt files left unmodified
- [ ] Script saved in ~/AppData/Local/hermes/scripts/
