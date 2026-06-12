# prompts-md — Fix Issues Context

Created: 2026-06-12
Target scope: `Prompts/*.md` (9 files)
Companion plan: `thoughts/plans/prompts-md-debug.md`

## Fix Track

| ID | Status | Notes |
| --- | --- | --- |
| 1 | Completed | Normalized malformed `skills:` bullets in Batch 1 files |
| 2 | Completed | Fixed truncated skill section in `prompts-fix.prompts.md` |
| 3 | Completed | Empty `## Phase 3` replaced with `## Phase 3: Plan audits and fixes` in `dev-init.prompts.md` |
| 4 | Completed | Clarified "three ecosystems" wording ambiguity reduced in `agents-fix.prompts.md` Goal block |
| 5 | Open | Stale body reference to `_archive/...bash-scripts-fix.prompts.txt` remains; verified context block |
| 6 | Completed | Corrected frontmatter copy duplication in `prompts-fix.prompts.md` |
| 7 | Open | `general.prompts.md` already has the core sections; no drift fix applied |

## Applied Changes

- `agents-fix.prompts.md`: normalized `skills:`, cleaned Goal wording
- `bash-scripts-fix.prompts.md`: normalized `skills:` and removed dependency-style bullets from skills section
- `dev-init.prompts.md`: removed empty `## Phase 3`, made section explicit
- `general.prompts.md`: unchanged
- `prompts-fix.prompts.md`: normalized `skills:`, fixed frontmatter description duplication, removed semicolons, fixed Goal wording

## Verification Gate

- Every modified file must still parse as valid frontmatter + markdown.
- No skill/tool references may be introduced as broken.
- Batch 1 must complete before Batch 2 begins.
