# Template Migration Plan

Generated: 2026-08-31 19:14 UTC
Prompts dir: `.github\prompts`

**Summary:** 0 prompts missing template dirs, 2 orphan template files, 235/235 passing

## 2. Migrate Orphan Template Files

These files live outside any prompt's `templates/{trigger}/` directory.

### Category: `orphan-dir:Initial` (1 files)

- **Source:** `.github\prompts\templates\Initial\README.md`
  **Parent dir:** `templates/Initial/`
  **Action:** Move to correct `templates/{trigger}/` directory
  **Suggested target:** `templates/MANUAL/`

### Category: `orphan-dir:optimize-agentsMd` (1 files)

- **Source:** `.github\prompts\templates\optimize-agentsMd\README.md`
  **Parent dir:** `templates/optimize-agentsMd/`
  **Action:** Move to correct `templates/{trigger}/` directory
  **Suggested target:** `templates/MANUAL/`

## 3. Update Cross-References in Prompts

After migrating files, update all prompt files that reference old paths:

| Old pattern | New pattern |
|---|---|
| `templates/_shared/...` | `templates/{prompt-trigger}/...` (if prompt-specific) or keep shared |
| `templates/root-*` | `templates/{prompt-trigger}/*` |
| `templates/profiles/*` | `templates/profile-templates/*` (if profile-templates.prompt.md exists) |
| `templates/Developement/*` | `templates/development/*` (typo fix) |
| top-level `.md` files | `templates/{prompt-trigger}/` |

