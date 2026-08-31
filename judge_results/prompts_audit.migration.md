# Template Migration Plan

Generated: 2026-08-31 19:54 UTC
Prompts dir: `.github\prompts`

**Summary:** 1 prompts missing template dirs, 0 orphan template files, 234/235 passing

## 1. Create Missing Template Directories

### `optimize-agentsmd` (from `optimize-agentsMd.prompt.md`)

Missing: `templates/optimize-agentsmd/`

Steps:
1. `mkdir -p templates/optimize-agentsmd`
2. Create `templates/optimize-agentsmd/README.md` with prompt template content

## 3. Update Cross-References in Prompts

After migrating files, update all prompt files that reference old paths:

| Old pattern | New pattern |
|---|---|
| `templates/_shared/...` | `templates/{prompt-trigger}/...` (if prompt-specific) or keep shared |
| `templates/root-*` | `templates/{prompt-trigger}/*` |
| `templates/profiles/*` | `templates/profile-templates/*` (if profile-templates.prompt.md exists) |
| `templates/Developement/*` | `templates/development/*` (typo fix) |
| top-level `.md` files | `templates/{prompt-trigger}/` |

