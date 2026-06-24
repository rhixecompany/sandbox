---
title: "Bash Scripts Plan"
source: "docs/bash-scripts-plan.md"
---

# Bash Scripts Fix - Implementation Plan

**Generated:** 2026-05-29  
**Phase:** 2 (Implementation Planning)  
**Based on:** docs/bash-scripts-list-context.md  

---

## Goal

Design and plan a comprehensive migration strategy to:
1. Move 54 conflicting scripts from projects/ and root to Bash/**
2. Consolidate functionality into TypeScript with AST-safe operations
3. Maintain dry-run support and behavior parity
4. Eliminate dead code
5. Update all references (package.json, CI configs)

---

## Executive Summary

### Scope

| Item | Count | Details |
|------|-------|---------|
| **Total scripts to migrate** | 54 | Banking (34), comicwise (10), rhixe_scans (7), ecom (1), root (2) |
| **Scripts to keep in place** | 315+ | Bash/ content, archives, infrastructure, seeds |
| **Total scripts in workspace** | 369 | Fully inventoried in Phase 1 |

### Architecture

Target state after migration:

```
Bash/
├── src/
│   ├── orchestrator.ts          (main entry point)
│   ├── lib/
│   │   ├── colors.ts
│   │   ├── logging.ts
│   │   ├── errors.ts
│   │   ├── cli.ts
│   │   └── [consolidation utilities]
│   └── [migrated implementations]
├── Banking/
│   ├── scripts/
│   │   ├── orchestrator.{sh,ps1,bat}
│   │   ├── opencode-mcp.{sh,ps1,bat}
│   │   ├── plan-ensure.{sh,ps1,bat}
│   │   └── [other migrated scripts]
│   └── install/
│       └── lib/
│           ├── 00-config.sh through 08-install.sh
│           └── install.sh (orchestrator)
├── comicwise/
│   ├── dev.{sh,ps1,bat}
│   ├── cleanup.{sh,ps1,bat}
│   ├── quality-gate.{sh,ps1,bat}
│   ├── setup-dev.{sh,ps1,bat}
│   └── install-vscode-extensions.{sh,ps1,bat}
├── rhixe_scans/
│   ├── docker-clean.sh
│   ├── git-setup.sh
│   ├── install_chrome.sh
│   ├── install_firefox.sh
│   ├── prod-dev.sh
│   ├── prod.sh
│   └── setup.sh
├── ecom/
│   └── install.sh
├── [root-level migrated scripts]
├── package.json (updated with new npm scripts)
├── [wrappers and orchestrators]
├── docs/
│   └── NAMING_CONVENTION.md
├── logs/
└── archive/
    └── [kept as-is: skills-commit-batch-*, etc.]
```

---

## Migration Strategy

### Phase 2a: Analysis & Planning

| Task | Details |
|------|---------|
| **Script grouping** | Group by functionality (installers, orchestrators, validators, utilities) |
| **Dependency mapping** | Document interdependencies, cross-project calls, shared logic |
| **TypeScript consolidation** | Identify duplicated logic for shared libraries (colors, logging, CLI) |
| **Dry-run audit** | Catalog which scripts already have dry-run, which need it |
| **Path reference audit** | Find hard-coded paths that will need updating post-migration |

### Phase 2b: Fix Planning

Issues to identify and fix during Phase 3 (Code Review):

| Category | Examples | Action |
|----------|----------|--------|
| **Bash syntax** | Missing `set -euo pipefail`, missing `shellcheck` directives, unbound vars | Fix in Phase 3 |
| **PowerShell** | Missing `Set-StrictMode`, deprecated `PSIsContainer`, hardcoded paths | Fix in Phase 3 |
| **Batch files** | Label ordering issues, ANSI artifacts, thin delegator pattern | Fix in Phase 3 |
| **Hard-coded paths** | `C:\\Users\\Alexa\\Desktop\\SandBox` references | Fix after migration |
| **Placeholder comments** | `@author Adminbot`, `Description placeholder` | Fix in Phase 3 |
| **Dead code** | One-shot artifacts, test scripts | Archive or delete |

### Phase 2c: Execution Planning

**Batches for Phase 4 (Execution):**

#### Batch 1: Banking Orchestrators (4 scripts)
- `orchestrator.{sh,ps1,bat}` — Master orchestrator
- `plan-ensure.{sh,ps1,bat}`
- **Output:** TypeScript implementation + thin wrappers
- **Verification:** Both original and migrated output identical

#### Batch 2: Banking Install Framework (11 scripts)
- `install.sh`, `install-agents.sh`
- `install/lib/00-config.sh` through `08-install.sh` (9 modules)
- **Output:** Consolidated install framework with shared lib
- **Verification:** Can run install process successfully

#### Batch 3: Banking MCP & Plugin Scripts (9 scripts)
- `opencode-mcp.{sh,ps1,bat}`
- `opencode-plugin-repair.{sh,ps1,bat}`
- `opencode-plugin-verify.{sh,ps1,bat}`
- **Output:** Consolidated MCP/plugin runners
- **Verification:** All three variants produce identical results

#### Batch 4: Banking Utilities & Verification (10 scripts)
- `aggressive-capture.ps1`
- `branch-compare.sh`
- `delete-gone-branches.sh`
- `diagnose-and-fix-git.{sh,ps1}`
- `run-verify-and-validate.ps1`
- `verify-agents.{sh,ps1}`
- **Output:** Consolidated utility set
- **Verification:** All scripts runnable post-migration

#### Batch 5: comicwise Development Workflows (10 scripts)
- `cleanup.{sh,ps1}`
- `dev.{sh,ps1}`
- `install-vscode-extensions.{sh,ps1}`
- `quality-gate.{sh,ps1}`
- `setup-dev.{sh,ps1}`
- **Output:** Consolidated dev environment setup
- **Verification:** Full dev environment initializes correctly

#### Batch 6: rhixe_scans Utilities (7 scripts)
- `docker-clean.sh`
- `git-setup.sh`
- `install_chrome.sh`, `install_firefox.sh`
- `prod-dev.sh`, `prod.sh`
- `setup.sh`
- **Output:** Consolidated tooling set
- **Verification:** Docker/git/browser tools initialize correctly

#### Batch 7: Root & ecom Scripts (3 scripts)
- `analyze-scripts.sh` → `Bash/analyze-scripts.sh`
- `docs/sandbox-runtime-commands.ps1` → `Bash/sandbox-runtime-commands.ps1`
- `projects/ecom/install.sh` → `Bash/ecom/install.sh`
- **Output:** Root-level scripts integrated
- **Verification:** Scripts execute from new location

---

## Phase 3 Dependency: Code Review Issues to Fix

Before migration (Phase 4), Phase 3 will audit and document issues.

### Critical Issues to Audit

- [ ] Missing `set -euo pipefail` in bash scripts
- [ ] Missing `shellcheck shell=bash` directives
- [ ] Hard-coded paths needing updates
- [ ] Placeholder comments (`Adminbot`, `Description placeholder`)
- [ ] Missing `Set-StrictMode` in PowerShell scripts
- [ ] Deprecated `PSIsContainer` patterns
- [ ] BAT label ordering and delegator patterns
- [ ] Dry-run function consistency across variants
- [ ] Exit code propagation in wrappers

### Blocker Detection

- Script syntax errors (bash -n, powershell parse)
- Missing dependencies
- Circular dependencies between scripts
- Hardcoded user/system paths not parameterizable

---

## Phase 4: Migration Execution

### Per-Batch Execution Pattern

```bash
# For each batch:

Step 1: Copy scripts to Bash/** with directory structure preserved
  mkdir -p Bash/Banking/scripts
  cp projects/Banking/scripts/orchestrator.* Bash/Banking/scripts/

Step 2: Fix hard-coded paths to reflect new Bash/** location
  sed -i "s|/projects/Banking|/Bash/Banking|g" Bash/Banking/scripts/*

Step 3: Verify parity (original vs migrated)
  bash projects/Banking/scripts/orchestrator.sh --help > original.txt
  bash Bash/Banking/scripts/orchestrator.sh --help > migrated.txt
  diff original.txt migrated.txt

Step 4: Update all references in callers
  package.json scripts section
  .github/workflows/*.yml
  Makefile / orchestrator scripts
  README and documentation

Step 5: Delete original after parity verified
  git rm projects/Banking/scripts/orchestrator.*
```

### Commit Strategy

**Per-project commits:**

```bash
git commit -m "feat: migrate Banking scripts to Bash/

- Move 34 Banking scripts to Bash/Banking/**
- Update package.json script references
- Fix hard-coded paths post-migration
- All parity checks passed"
```

---

## Phase 5: Testing & Verification

### Test Coverage

For each migrated script:

1. **Syntax validation**
   ```bash
   bash -n script.sh
   powershell -NoProfile -File script.ps1
   ```

2. **Behavior parity**
   ```bash
   # Original vs migrated output identical
   diff <(original-script args) <(migrated-script args)
   ```

3. **Dry-run fidelity**
   ```bash
   original-script --dry-run > original-dryrun.log
   migrated-script --dry-run > migrated-dryrun.log
   diff original-dryrun.log migrated-dryrun.log
   ```

4. **Exit code propagation**
   ```bash
   original-script --invalid-arg; echo $?
   migrated-script --invalid-arg; echo $?
   ```

### Regression Testing

- All npm scripts in package.json execute without error
- CI workflows pass with new script locations
- Dry-run batches execute successfully
- No orphaned references remain

---

## Phase 6: Cleanup & Finalization

### Cleanup Checklist

- [ ] All 54 conflicting scripts copied to Bash/**
- [ ] All 54 originals deleted via git rm
- [ ] No stale references in package.json, workflows, docs
- [ ] git status shows clean state
- [ ] No broken symlinks or orphaned paths
- [ ] Tag release: BASH-SCRIPTS-MIGRATION-2026-05-29

### Documentation Updates

- Update README.md with new script locations
- Update NAMING_CONVENTION.md in Bash/docs/
- Create MIGRATION_GUIDE.md documenting path changes
- Update CI workflow documentation

---

## Deliverables Summary

**Phase 2 Outputs:**

1. ✅ `docs/bash-scripts-list-context.md` (Phase 1) — 7.0 KB
2. → `docs/bash-scripts-plan.md` (Phase 2) — Implementation plan
3. → `docs/bash-scripts-issues-context.md` (Phase 3) — Audit findings
4. → `.github/prompts/bash-scripts-fix-prompt.md` (Phase 3) — Execution spec
5. → Migrated scripts in Bash/** (Phase 4-5)
6. → BASH_SCRIPTS_MIGRATION_REPORT.md (Phase 6) — Final report

---

## Success Criteria

- [ ] All 54 scripts copied to Bash/** with correct structure
- [ ] All 54 originals deleted from projects/ and root
- [ ] 100% parity tests pass (original vs migrated)
- [ ] All dry-run variants execute without error
- [ ] No regression in script functionality
- [ ] No broken references in package.json or CI configs
- [ ] Clean git status with migration commits
- [ ] Documentation updated

---

## Timeline Estimate

| Phase | Duration | Status |
|-------|----------|--------|
| Phase 1 (Catalog) | ~15 min | ✅ Complete |
| Phase 2 (Plan) | ~30 min | → In progress |
| Phase 3 (Code Review) | ~45 min | Pending Phase 2 |
| Phase 4 (Migration) | ~60 min | Pending Phase 3 |
| Phase 5 (Test) | ~30 min | Pending Phase 4 |
| Phase 6 (Cleanup) | ~15 min | Pending Phase 5 |
| **Total** | **~195 min (3.25 hours)** | — |

---

## Status

✅ **Phase 2 In Progress**

Next: Complete Phase 3 (Code Review & Issue Audit)

---

**Project:** Bash Scripts Modernization (bash-scripts-fix)  
**Version:** 2.0  
**Last Updated:** 2026-05-29
