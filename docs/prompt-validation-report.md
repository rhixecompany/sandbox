# Prompt Validation Report

> Generated: 2026-06-28 | 251 prompts checked

## Summary

| Metric | Count |
|--------|-------|
| Total prompts | 251 |
| With valid frontmatter (name, title, description, version, tags) | 251 ✅ |
| With actual tags (non-empty YAML list) | 101 |
| With empty tags (`tags: []`) | 150 ⚠️ |
| Duplicate names | 0 ✅ |
| Duplicate titles | 0 ✅ |
| Duplicate content (exact MD5) | 0 ✅ |
| Referencing shared templates | 6 ⚠️ |

## Frontmatter

- **Required fields:** All 251 prompts have `name:`, `title:`, `description:`, `version:`, `tags:` present ✅
- **Tags format:** 101 use proper YAML list, 150 use `tags: []` (empty — need meaningful tags)
- **No bare-string tags** (all use YAML array or list format)

## Duplicates

- **Names:** 0 duplicates found (the `name: CI` match is inside a `system:` YAML block, not a frontmatter entry)
- **MD5:** All 251 files have unique content checksums ✅

## Template Usage

- **Shared templates:** 13 files in `prompts/templates/_shared/`
- **Prompts using them:** 6 (agents-fix, bash-scripts-fix, general, prompt-management, prompts-fix, workspace-consolidate)
- **Prompts NOT using them:** 245 — major DRY opportunity

## Dependencies

*Not re-checked — previous script was too aggressive (marked prose words as missing refs)*

## Recommendations

| Priority | Action | Affects |
|----------|--------|---------|
| Low | Add meaningful `tags:` to 150 prompts with `tags: []` | 150 prompts |
| Medium | Wire remaining 245 prompts to use `templates/_shared/` | 245 prompts |
| Low | Clean up per-prompt template dirs in `templates/<name>/` | 130+ dirs |

---
