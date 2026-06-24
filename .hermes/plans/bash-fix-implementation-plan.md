---
title: "Bash Fix Implementation Plan"
source: "docs/bash-fix-implementation-plan.md"
---

# Bash Scripts Fix — Phase 2: Implementation Plan

**Generated**: 2026-05-27
**Based on**: `docs/bash-scripts-list-context.md` (Phase 1 catalog)

---

## Strategy

- **Copy** → **Fix paths** → **Verify parity** → **Delete originals** → **Update callers**
- Process in batches by project group
- Each batch is committed independently
- No functional changes — migration only (code review fixes are Phase 3)

## Target Structure in Bash/

```
Bash/
├── Banking/
│   ├── install.sh
│   ├── install-agents.sh
│   ├── install/lib/
│   │   ├── 00-config.sh ... 08-install.sh
│   └── scripts/
│       ├── aggressive-capture.ps1
│       ├── branch-compare.sh
│       ├── delete-gone-branches.sh
│       ├── diagnose-and-fix-git.ps1
│       ├── diagnose-and-fix-git.sh
│       ├── opencode-mcp.sh, .ps1, .bat
│       ├── opencode-plugin-repair.sh, .ps1, .bat
│       ├── opencode-plugin-verify.sh, .ps1, .bat
│       ├── orchestrator.sh, .ps1, .bat
│       ├── plan-ensure.sh, .ps1, .bat
│       ├── run-verify-and-validate.ps1
│       ├── verify-agents.sh, .ps1
├── comicwise/
│   ├── cleanup.sh, .ps1
│   ├── dev.sh, .ps1
│   ├── install-vscode-extensions.sh, .ps1
│   ├── quality-gate.sh, .ps1
│   ├── setup-dev.sh, .ps1
├── rhixe_scans/
│   ├── docker-clean.sh
│   ├── git-setup.sh
│   ├── install_chrome.sh
│   ├── install_firefox.sh
│   ├── prod-dev.sh
│   ├── prod.sh
│   ├── setup.sh
├── ecom/
│   └── install.sh
├── root/
│   ├── analyze-scripts.sh
│   └── sandbox-runtime-commands.ps1
```

## Batch Execution Plan

### Batch 1: Banking scripts/ — cross-platform wrappers (17 files)

**Files**: opencode-mcp.{sh,ps1,bat}, opencode-plugin-repair.{sh,ps1,bat}, opencode-plugin-verify.{sh,ps1,bat}, orchestrator.{sh,ps1,bat}, plan-ensure.{sh,ps1,bat}, branch-compare.sh

**Callers to update**:
- `projects/Banking/package.json` — scripts referencing these paths
- CI workflows in `.github/workflows/`

### Batch 2: Banking git/agent scripts (7 files)

**Files**: delete-gone-branches.sh, diagnose-and-fix-git.ps1, diagnose-and-fix-git.sh, aggressive-capture.ps1, run-verify-and-validate.ps1, verify-agents.sh, verify-agents.ps1

**Callers to update**:
- `projects/Banking/package.json`
- Any CI references

### Batch 3: Banking install/ module (11 files)

**Files**: install.sh, install-agents.sh, install/lib/00-config.sh through 08-install.sh

**Callers to update**:
- `projects/Banking/package.json` — scripts referencing install.sh
- README documentation referencing install paths

### Batch 4: comicwise (10 files)

**Files**: cleanup.{sh,ps1}, dev.{sh,ps1}, install-vscode-extensions.{sh,ps1}, quality-gate.{sh,ps1}, setup-dev.{sh,ps1}

**Callers to update**:
- `projects/comicwise/package.json` — dev, cleanup, quality-gate scripts
- CI workflows

### Batch 5: rhixe_scans (7 files)

**Files**: docker-clean.sh, git-setup.sh, install_chrome.sh, install_firefox.sh, prod-dev.sh, prod.sh, setup.sh

**Callers to update**:
- `projects/rhixe_scans/package.json` or Makefile
- CI workflows referencing bash/ paths

### Batch 6: ecom + root (3 files)

**Files**: projects/ecom/install.sh, analyze-scripts.sh, docs/sandbox-runtime-commands.ps1

**Callers to update**:
- Root-level scripts — check CI and documentation references

## Path Fix Strategy

For each migrated script, the main concern is paths that reference sibling or parent files relative to the original location. Key patterns to fix:

1. **Source/import paths** — `source ./lib/utils.sh` → needs to work from new Bash/ path
2. **Hard-coded project paths** — e.g., `../../node_modules` → adjust for new depth
3. **Callers that reference the old location** — package.json, Makefile, CI configs

### Internal Path Migration

When copying scripts to `Bash/<project>/`, internal references need updating:

| Old Reference | New Reference |
|---------------|---------------|
| `../../node_modules/` | `../../../projects/Banking/node_modules/` |
| `./lib/00-config.sh` | `./install/lib/00-config.sh` |
| `../scripts/` | `./scripts/` |

For Bash scripts that DO NOT reference sibling files (standalone scripts), no path changes needed — just update the `package.json` script entries.

## Verification Strategy

For each batch:
1. Copy script to `Bash/<project>/<path>`
2. Run syntax check: `bash -n script.sh` or `pwsh -n script.ps1`
3. If script has `--dry-run`, test it in destination
4. Confirm identical output between original and migrated copy
5. Update all callers
6. Delete original with `git rm`
7. Commit with message `feat: migrate <project> batch-N scripts to Bash/`

## Caller Update Patterns

### package.json (Banking)
```
OLD: "install": "bash install.sh"
NEW: "install": "bash ../Bash/Banking/install.sh"
```
Or better: use relative path from project root.

### package.json (comicwise)
```
OLD: "dev": "bash dev.sh"
NEW: "dev": "bash ../Bash/comicwise/dev.sh"
```

### CI workflows
```
OLD: run: |
        cd projects/comicwise
        bash dev.sh
NEW: run: |
        bash Bash/comicwise/dev.sh
```
