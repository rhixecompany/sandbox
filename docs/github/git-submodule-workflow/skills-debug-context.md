# Skill Audit: `git-submodule-workflow`

**Category:** github  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\github\git-submodule-workflow\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 1 minor  

---

## Frontmatter Check

```yaml
name: git-submodule-workflow
title: Git Submodule Configuration & Workflow
description: >
  Configure, initialize, and maintain multiple git repositories as submodules within a parent monorepo. Covers conversion of existing local directories, configuration via .gitmodules, branch management, and verification of submodule state.
trigger: /git-submodule-workflow
tags: [git, submodules, monorepo, multi-project, github]
dependencies:
  - tool:terminal (git commands)
  - tool:write_file (for .gitmodules editing)
  - tool:patch (for targeted .gitmodules edits)
  - skill:git-helper
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: backup_ritual: backup file reference |

## Sections Present

- • `## Goal`
- ✅ `## Workflow`
- • `## Phase 3: Commit & Cleanup`
- • `## Submodule Inventory`
- • `## Initialization (first clone)`
- • `## Updating Submodules`
- • `## Removing a Submodule`
- • `## Resolving "modified content" State`
- • `## Branch Tracking`
- • `## Phase 4: Verification`
- • `## Ongoing Operations`
- • `## Pitfalls & Troubleshooting`
- • `## References`
- • `## Actions Summary`
- ✅ `## When to Use`

## Recommendations

- Fix `C1`: Stale pattern: backup_ritual: backup file reference
