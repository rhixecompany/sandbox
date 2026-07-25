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
python3 $LOCALAPPDATA/hermes/scripts/fix_prompts.py
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

### Phase 5: Tag Inference

**Use when:** 50+ prompts have `tags: []` and need meaningful categorisation from their existing content rather than hand-curation.

1. **Build keyword→tag map** for your domain (languages, frameworks, tools, concerns — see reference file)
2. **Infer from source text** — concatenate `title + name + description + first 500 chars of body`, match each regex pattern
3. **Apply name-pattern heuristics** — `plan-*` → planning, `*-mcp-*` → mcp, `*-audit` → audit
4. **Write back** — replace `tags: []` with `tags: [inferred, tags]`
5. **Verify** — confirm 0 empty tags remain, no tags overwritten where they already existed

**Reference:** `references/tag-inference.md` (full keyword map + Python script template)

## Pitfalls
- **CRLF on Windows**: Python `read_file`/`write_file` tools handle this fine, but direct `open()` needs `'rb'`/`'wb'` modes. **CRITICAL**: `has_yaml_frontmatter()` must check for BOTH `---\n` AND `---\r\n` — Copilot-imported files use CRLF and will be misdetected as having no frontmatter, causing duplicate frontmatter blocks to be added.
- **Copilot-style frontmatter**: Files imported from Copilot/GitHub may have non-standard first fields (e.g. starting with `toolsets:` instead of `name:`). These need merging, not replacement. See `references/copilot-frontmatter-merge.md`.
- **Duplicate frontmatter after fix**: If the fix script runs on CRLF files, it adds a second `---` block. Always run a post-fix dedup pass. See `references/copilot-frontmatter-merge.md` for the 3-script cascade pattern.
- **git revert first**: If a fix damages files, revert with `git checkout -- *.prompt.md` before re-running
- **Bulk corruption detection pattern**: When 170+ prompt files show the same garbled YAML (e.g. inline list items like `tags: - foo - bar` instead of proper YAML arrays, or `promptmetadata` string artifacts from corrupted metadata blocks), the corruption may already be committed. Investigate the corruption pattern first:
  1. `git diff HEAD -- prompts/*.prompt.md | grep "^+" | head -30` — check if the corruption is in working tree OR committed
  2. `git show HEAD:prompts/sample-file.prompt.md | grep -c "promptmetadata"` — check if corrupt commit exists
  3. If committed: `git log --all --format="%H" | while read c; do has=$(git show $c:prompts/sample-file.prompt.md 2>/dev/null | grep -c "promptmetadata"); [ "$has" = "0" ] && echo "CLEAN: $c" && break; done` — find the last clean commit
  4. `git checkout <clean-commit> -- prompts/` — restore from clean commit. Then verify with `grep -rl "promptmetadata" prompts/*.prompt.md | wc -l` — should be 0
  5. Commit the fix: `git add prompts/ && git commit -m "fix: restore prompt files from clean commit (YAML metadata corruption)"`
- **Symmetry check**: After bulk restore, verify both the corruption signature AND basic YAML structure. `grep -c "promptmetadata"` catches the corruption, but also check tags indentation by spot-checking a few files. Verify `git diff --stat HEAD -- prompts/ | tail -3` to confirm the diff volume matches expected corruption extent.
- **Bulk corruption detection pattern**: When 170+ prompt files show the same garbled YAML (e.g. inline list items like `tags: - foo - bar` instead of proper YAML arrays, or `promptmetadata` string artifacts from corrupted metadata blocks), the corruption may already be committed. Investigate the corruption pattern first:
  1. `git diff HEAD -- prompts/*.prompt.md | grep "^+" | head -30` — check if the corruption is in working tree OR committed
  2. `git show HEAD:prompts/sample-file.prompt.md | grep -c "promptmetadata"` — check if corrupt commit exists
  3. If committed: `git log --all --format="%H" | while read c; do has=$(git show $c:prompts/sample-file.prompt.md 2>/dev/null | grep -c "promptmetadata"); [ "$has" = "0" ] && echo "CLEAN: $c" && break; done` — find the last clean commit
  4. `git checkout <clean-commit> -- prompts/` — restore from clean commit. Then verify with `grep -rl "promptmetadata" prompts/*.prompt.md | wc -l` — should be 0
  5. Commit the fix: `git add prompts/ && git commit -m "fix: restore prompt files from clean commit (YAML metadata corruption)"`
- **Symmetry check**: After bulk restore, verify both the corruption signature AND basic YAML structure. `grep -c "promptmetadata"` catches the corruption, but also check tags indentation by spot-checking a few files. Verify `git diff --stat HEAD -- prompts/ | tail -3` to confirm the diff volume matches expected corruption extent.
- **.txt files**: These are raw source references — skip them for YAML frontmatter additions
- **False positives**: `tags:` followed by YAML list items (`  - item`) is VALID — don't replace with `tags: []`
- **Duplicate tags**: Running `fix_tags_format` then `update_field` for tags can create duplicates — check for this
- **`generator-orchestrator.prompt.md` edge case**: Use `###` level heading for Legacy section detection too
- **Large frontmatter gap**: Copilot files can have 60+ lines of `toolsets:` entries. Don't assume `dashes[1] - dashes[0] > 60` means no duplicate — check if the second block contains `name:` field.

## Script Location
Scripts go in: `~/AppData/Local/hermes/scripts/fix_*.py`

## References
- `references/tag-inference.md` — keyword-to-tag mapping for auto-inferring tags from prompt content
- `references/copilot-frontmatter-merge.md` — handling CRLF + Copilot-style frontmatter (3-script cascade pattern for mixed-format libraries)

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