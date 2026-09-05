# Template Migration Plan

Generated: 2026-09-05 02:21 UTC
Prompts dir: `.github\prompts`

**Summary:** 1 prompts missing template dirs, 0 orphan template files, 235/236 passing

## 1. Create Missing Template Directories

### `comprehensive-hermes-maintenance` (from `comprehensive-hermes-maintenance.prompt.md`)

Missing: `templates/comprehensive-hermes-maintenance/`

Steps:
1. `mkdir -p templates/comprehensive-hermes-maintenance`
2. Create `templates/comprehensive-hermes-maintenance/README.md` with prompt template content

## 3. Update Cross-References in Prompts

After migrating files, update all prompt files that reference old paths:

| Old pattern | New pattern |
|---|---|
| `templates/_shared/...` | `templates/{prompt-trigger}/...` (if prompt-specific) or keep shared |
| `templates/root-*` | `templates/{prompt-trigger}/*` |
| `templates/profiles/*` | `templates/profile-templates/*` (if profile-templates.prompt.md exists) |
| `templates/Developement/*` | `templates/development/*` (typo fix) |
| top-level `.md` files | `templates/{prompt-trigger}/` |

