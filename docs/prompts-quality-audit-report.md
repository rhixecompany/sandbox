# Prompts Quality Audit Report

**Date**: 2026-05-31  
**Scope**: `Prompts/*.prompts.md` (8 files)  
**Archive**: `Prompts/_archive/` (5 redundant `.txt` files)


## Summary

| Metric | Count |
|--------|-------|
| Total files | 8 |
| ✅ Optimal (≥80) | 8 |
| ⚠️ Needs work (60–79) | 0 |
| ❌ Rewrite (<60) | 0 |

## Per-File Scores

| File | Score | Status | Size | Frontmatter | Sections | Skills | Actions | Broken Refs | Issues |
|------|-------|--------|------|-------------|----------|--------|---------|-------------|--------|
| ✅ agents-fix.prompt | 100 | optimal | 5536 | ✓ | ✓ | ✓ | ✓ | 0 | none |
| ✅ bash-scripts-fix.prompt | 100 | optimal | 7054 | ✓ | ✓ | ✓ | ✓ | 0 | none |
| ✅ commands-fix.prompt | 100 | optimal | 5999 | ✓ | ✓ | ✓ | ✓ | 0 | none |
| ✅ dev-init.prompt | 90 | optimal | 15884 | ✓ | ✓ | ✓ | ✓ | 0 | hierarchy |
| ✅ general.prompt | 90 | optimal | 5339 | ✓ | ✓ | ✓ | ✗ | 0 | no tool refs |
| ✅ repo.prompt | 90 | optimal | 21536 | ✓ | ✓ | ✓ | ✓ | 0 | hierarchy |
| ✅ skills-fix.prompt | 100 | optimal | 5600 | ✓ | ✓ | ✓ | ✓ | 0 | none |
| ✅ workspace-consolidate.prompt | 100 | optimal | 21391 | ✓ | ✓ | ✓ | ✓ | 0 | none |

## Merge Actions Performed

| Source | Target | Action |
|--------|--------|--------|
| `skills-fix.prompts.txt` | archived | Redundant — `.md` is strict superset |
| `general.prompts.txt` | archived | Redundant — `.md` is strict superset |
| `commands-fix.prompts.txt` | archived | Redundant — `.md` is strict superset |
| `agents-fix.prompts.txt` | archived | Redundant — `.md` is strict superset |
| `dev-init.prompts.txt` | `dev-init.prompts.md` | Merged `/enhance-markdown` definition as reference |
| `repo.prompts.txt` | `repo.prompts.md` | Merged migration/branch normalization section |
| `bash-scripts-fix.prompts.txt` | `bash-scripts-fix.prompts.md` | Merged 7-phase implementation plan reference |

## Remaining Issues

- `dev-init.prompts.md`: heading hierarchy (H2→H4 skip in `/enhance-markdown` appendix — cosmetic)
- `general.prompts.md`: no tool references in Actions section (uses prose instead of tool calls)
- `repo.prompts.md`: heading hierarchy (phase sub-sections use H3 under H2 Phases — cosmetic)

All issues are cosmetic. No structural blockers remain.