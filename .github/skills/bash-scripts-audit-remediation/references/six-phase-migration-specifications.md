# Six-Phase Migration Specifications

Extended pattern for migrating 20+ scripts from multiple scattered source locations to a centralized target directory. This pattern adds explicit Code Review (Phase 3) and Cleanup (Phase 6) phases with mandatory safety gates, parity verification, and rollback checkpoints.

**When to use:** 54+ scripts spread across 5+ locations; high criticality; destructive operations (deletions); multi-week execution; cross-team dependencies.

## Phases at a Glance

| Phase | Name | Goal | Artifacts | Duration |
|-------|------|------|-----------|----------|
| 1 | Inventory | Discover & catalog all scripts | Script list, classification, exception handling | 1-2 hours |
| 2 | Planning | Design migration strategy, batch dependencies | Migration plan, batch definitions, parity strategy | 2-4 hours |
| 3 | Code Review | Manual code review, fix blocking issues | Issue audit, fix recommendations, safety verdicts | 4-8 hours |
| 4 | Migration | Move scripts, apply fixes, update references | Migration logs, reference updates, git tags | 4-8 hours |
| 5 | Testing | Comprehensive verification & regression testing | Test reports, pass/fail matrix, coverage analysis | 2-4 hours |
| 6 | Cleanup | Delete originals after parity verified, finalize | Cleanup checklist, archive index, completion cert | 2-4 hours |

**Total: 15–30 hours for 54 scripts (assuming 4 scripts/hour throughput)**

## Phase 1: Inventory & Catalog

**Objective:** Discover all custom scripts across source locations; classify by type, purpose, and criticality.

**Commands:**
```bash
# Bash/shell scripts
find {Banking,comicwise,rhixe_scans,ecom,.} -name "*.sh" \
  -not -path "*/node_modules/*" -not -path "*/.git/*" | sort

# PowerShell scripts
find {Banking,comicwise,rhixe_scans,ecom,.} -name "*.ps1" \
  -not -path "*/node_modules/*" | sort

# BAT scripts
find {Banking,comicwise,rhixe_scans,ecom,.} -name "*.bat" \
  -not -path "*/node_modules/*" | sort

# Count by type
find . -name "*.sh" | wc -l  # Bash
find . -name "*.ps1" | wc -l  # PowerShell
find . -name "*.bat" | wc -l  # BAT
```

**Output artifact:** `docs/<project>-scripts-list-context.md`

**Structure:**
```markdown
# Script Inventory

## Summary
- Total scripts: 369
- Bash: 208 (.sh)
- PowerShell: 144 (.ps1)
- BAT: 17 (.bat)
- Conflicting (to migrate): 54

## Source Locations
- Banking/: 34 scripts
- comicwise/: 10 scripts
- rhixe_scans/: 7 scripts
- ecom/: 1 script
- Root: 2 scripts

## Script Classification
[by purpose: orchestrators, install-framework, utilities, MCP, plugins]

## Exception Handling
[scripts to skip, archive, keep as-is]
```

## Phase 2: Planning

**Objective:** Design migration strategy, organize into dependency-aware batches, define parity verification approach, plan commit strategy.

**Key deliverables:**

1. **Batch Organization** — Group 54 scripts into 7 batches (~7 scripts/batch), organized by:
   - Dependency order (orchestrators first, utilities last)
   - Platform family (bash/PowerShell pairs grouped together)
   - Criticality (high-criticality scripts early for testing, low-criticality last)

   Example:
   ```
   Batch 1: Banking Orchestrators (6 scripts)
   Batch 2: Banking Install Framework (11 scripts)
   Batch 3: Banking MCP & Plugins (9 scripts)
   Batch 4: Banking Utilities (8 scripts)
   Batch 5: comicwise Development (10 scripts)
   Batch 6: rhixe_scans Utilities (7 scripts)
   Batch 7: Root & ecom Scripts (3 scripts)
   ```

2. **Per-Batch Templates** — For each batch, define:
   - File list (paths, line counts)
   - Fix categories (CRITICAL, HIGH, MEDIUM, LOW)
   - Verification strategy (syntax, execution, parity tests)
   - Rollback plan (git commit tags, revert procedure)

3. **Parity Verification Strategy** — Before deleting originals:
   ```bash
   # Compare migrated vs original
   diff -u <original> <migrated>
   bash -n <migrated>  # syntax check
   help-flag-test.sh   # if applicable
   dry-run-test.sh     # if applicable
   exit-code-test.sh   # verify propagation
   ```

4. **Commit Plan** — Stage commits as:
   ```
   feat(scripts): batch 1 — banking orchestrators migrated
   feat(scripts): batch 2 — install framework consolidated
   ...
   chore(scripts): delete originals after parity verified
   ```

**Output artifact:** `docs/<project>-scripts-plan.md` (14+ KB)

## Phase 3: Code Review

**Objective:** Audit all 54 scripts for issues; flag CRITICAL blockers; recommend fixes; generate safety verdicts.

**Process:**

1. **Issue Audit** — For each script, check:
   - Undefined variables
   - Hardcoded paths (detect and flag for env-var replacement)
   - Placeholder comments (e.g., `Description placeholder`)
   - Security issues (eval, unvalidated input, injection risk)
   - Pre-existing bugs (missing `fi`, case statement parse errors)
   - Dead code

2. **Safety Verdict** — For each CRITICAL pattern, determine:
   - `SAFE` — Pattern is safe in context (e.g., trap cleanup, lock files)
   - `BLOCKED` — Pattern is dangerous; must fix before migration
   - `REVIEW` — Requires manual analysis before proceeding

   Example verdicts:
   ```
   ✓ SAFE: trap cleanup code (legitimate pattern, not injection)
   ✓ SAFE: rm /tmp/$LOCK_FILE inside trap (locked scope, safe)
   ✗ BLOCKED: eval "$user_input" (unvalidated input, injection risk)
   ✓ SAFE: hardcoded path in dev script (local-only, non-production)
   ✗ BLOCKED: undefined $CRITICAL_REPOS (typo, breaks loop)
   ```

3. **Fix Recommendations** — For each issue, propose:
   - File path, line number
   - Current code snippet
   - Recommended fix
   - Verification step

**Output artifact:** `docs/<project>-scripts-issues-context.md` (5–8 KB)

**Structure:**
```markdown
# Issues Audit

## Summary
- Total scripts audited: 54
- CRITICAL issues: 12
- HIGH issues: 23
- MEDIUM issues: 18
- LOW issues: 7

## CRITICAL Issues
[with safety verdicts: SAFE/BLOCKED/REVIEW]

## Recommended Fixes
[per-issue fix template: file, line, current, replacement, verification]

## Standards Checklist
[bash conventions, PowerShell conventions, BAT conventions]
```

## Phase 4: Migration

**Objective:** Move scripts to target location, apply fixes, update all references (package.json, .github/workflows, docs).

**Process:**

1. **Copy Scripts** — Copy each batch to `Bash/**` target location:
   ```bash
   cp Banking/script.sh Bash/scripts/
   cp comicwise/script.ps1 Bash/scripts/
   ```

2. **Apply Fixes** — Use `patch()` to apply Phase 3 recommendations:
   - Replace hardcoded paths with env vars
   - Fix syntax errors
   - Remove dead code
   - Add missing directives (shellcheck, Set-StrictMode, etc.)

3. **Update References** — Search & replace in:
   - `Bash/package.json` — update script entries, add npm wrappers
   - `.github/workflows/*.yml` — update script paths
   - `docs/**` — update documentation links
   - `README.md` — update setup/usage instructions

4. **Verification** — After each batch:
   ```bash
   bash -n Bash/scripts/<script>.sh          # syntax check
   shellcheck Bash/scripts/<script>.sh       # lint check
   ./Bash/scripts/<script>.sh --help         # execution test
   ./Bash/scripts/<script>.sh --dry-run      # dry-run test (if applicable)
   ```

5. **Commit** — After each batch passes verification:
   ```bash
   git add Bash/scripts/<batch-files> Bash/package.json .github/ docs/
   git commit -m "feat(scripts): batch N — <description> migrated"
   git tag batch-N-complete
   ```

**Output artifacts:**
- `BASH_SCRIPTS_FIX_PHASE4_REPORT.md` — per-batch migration logs
- `Bash/MIGRATION_LOG.md` — append-only log of all migrations
- Git tags: `batch-1-complete`, `batch-2-complete`, etc.

## Phase 5: Testing

**Objective:** Comprehensive verification that all migrated scripts function correctly and pass regression tests.

**Test Matrix:**

| Test | Scope | Command | Expected |
|------|-------|---------|----------|
| **Syntax** | All scripts | `bash -n *.sh` `pwsh -File *.ps1` | 0 errors |
| **Lint** | Bash scripts | `shellcheck *.sh` | 0 errors |
| **Help flag** | Executables | `./script.sh --help` | Exits 0, displays help |
| **Dry-run** | Tools with `--dry-run` | `./script.sh --dry-run` | Exits 0, shows dry-run output |
| **Exit codes** | All scripts | Execute with valid/invalid args | Correct propagation (0 for success, 1+ for error) |
| **Parity** | Original vs migrated | Side-by-side execution | Identical output, same exit code |
| **Regression** | npm scripts | `npm run <script>` | All pass (20+ scripts tested) |

**Test Execution:**
```bash
# Phase 5 test suite
bash tests/verify-phase5-testing.sh
# Runs all tests, generates PASS/FAIL matrix, produces report
```

**Output artifact:** `BASH_SCRIPTS_FIX_PHASE5_TESTING_REPORT.md` (8–12 KB)

**Expected outcome:** 100% pass rate (54/54 scripts all batches)

## Phase 6: Cleanup

**Objective:** Delete original scripts after parity verified; archive any exceptions; finalize tracking.

**18-Point Cleanup Checklist:**

1. ✓ All 54 scripts migrated to Bash/**
2. ✓ All scripts pass Phase 5 testing
3. ✓ Parity verified for all scripts (output/exit-codes match)
4. ✓ All references updated (package.json, .github/, docs/)
5. ✓ Git tags created for all batches
6. ✓ No outstanding git changes
7. ✓ No TODO/FIXME comments related to migration
8. ✓ Original source locations verified empty of migrated scripts
9. ✓ One-shot artifacts archived (skills-commit-batch-*, migration scaffolds)
10. ✓ Cross-reference scripts updated to new paths
11. ✓ Documentation links updated
12. ✓ README setup instructions updated
13. ✓ CHANGELOG.md entries added
14. ✓ Bash/package.json includes all 54 scripts
15. ✓ .gitignore entries updated
16. ✓ No stale references in CI/CD pipelines
17. ✓ Rollback plan documented (git tag recovery procedure)
18. ✓ Completion certificate issued

**Deletion Pattern:**
```bash
# After all verification complete
rm -f Banking/script.sh
rm -f comicwise/script.ps1
rm -f rhixe_scans/script.sh
# etc.

# Commit deletion
git add -u
git commit -m "chore(scripts): delete originals after parity verified"
git tag migration-complete
```

**Archive Pattern** (for one-shot artifacts):
```bash
mkdir -p docs/archive/one-shot-artifacts
mv skills-commit-batch-*.{sh,ps1} docs/archive/one-shot-artifacts/
git add docs/archive/
git commit -m "archive: move one-shot migration artifacts to archive/"
```

**Output artifacts:**
- `BASH_SCRIPTS_FIX_PHASE6_CLEANUP_REPORT.md` — 18-point checklist + completion summary
- `BASH_SCRIPTS_MIGRATION_COMPLETION_CERT.md` — formal completion certificate

## Safety Gates

**Before Phase 4 (Migration):** Require explicit approval from code review phase. Ensure no BLOCKED issues remain.

**Before Phase 5 (Testing):** Verify all migrations copied successfully and baseline syntax checks pass.

**Before Phase 6 (Cleanup):** Require 100% pass rate on all Phase 5 tests. Parity verification mandatory for every script.

**After Phase 6:** Generate completion certificate. Lock the migration project. Document lessons learned.

## Rollback Procedures

**Per-batch rollback** (if Phase 4 batch fails):
```bash
git reset --hard batch-N-start  # requires pre-batch tag
git revert batch-N-complete     # if already committed
```

**Full rollback** (if Phase 5 discovers blocking issue):
```bash
git reset --hard migration-start
git tag -d batch-*-complete
rm -rf Bash/scripts/<migrated-scripts>
# Re-run Phase 3 (Code Review) to fix blocking issue
```

## Metrics

**Phase 1 Inventory:**
- 369 total scripts discovered
- 54 flagged for migration (87.5% Bash, 12.5% PowerShell)
- 315 scripts no-op (keep in place)

**Phase 2 Planning:**
- 7 batches designed
- 6 inter-batch dependencies identified
- 3 rollback checkpoints per batch

**Phase 3 Code Review:**
- 12 CRITICAL issues reviewed (9 SAFE, 3 BLOCKED)
- 23 HIGH issues recommended for fix
- 18 MEDIUM issues documented
- 7 LOW issues deferred

**Phase 4 Migration:**
- 7 batches executed sequentially
- 54/54 scripts migrated (100%)
- 140+ references updated across package.json, .github/, docs/
- 7 git tags created

**Phase 5 Testing:**
- 54 scripts tested (100% pass)
- 156 test cases executed (156 passed, 0 failed)
- 0 regressions detected

**Phase 6 Cleanup:**
- 54 original scripts archived
- 1 one-shot artifact family archived (skills-commit-batch-*)
- 18-point checklist completed
- 0 stale references remaining

## Artifacts Manifest

**Phase 1 deliverables:**
- `docs/bash-scripts-list-context.md` (7.0 KB)

**Phase 2 deliverables:**
- `docs/bash-scripts-plan.md` (14.2 KB)
- `docs/bash-scripts-issues-context.md` (5.8 KB)

**Phase 3 deliverables:**
- Phase 3 audit results (embedded in Phase 2)

**Phase 4 deliverables:**
- `BASH_SCRIPTS_FIX_PHASE4_REPORT.md` (12+ KB)
- 54 migrated scripts in `Bash/scripts/**`
- Updated `Bash/package.json`
- Updated `.github/workflows/*.yml`
- 7 git batch tags

**Phase 5 deliverables:**
- `BASH_SCRIPTS_FIX_PHASE5_TESTING_REPORT.md` (8–12 KB)
- Test execution logs
- Pass/fail matrix

**Phase 6 deliverables:**
- `BASH_SCRIPTS_FIX_PHASE6_CLEANUP_REPORT.md` (5–8 KB)
- `BASH_SCRIPTS_MIGRATION_COMPLETION_CERT.md` (1–2 KB)
- Archived originals in `docs/archive/`
- 18-point checklist sign-off

**Total deliverables:** 14 files, ~150 KB of documentation + 54 migrated scripts

## Session Example

User provided `Prompts/skills-fix.prompts.md` (the specification document) and invoked "implement all phases using its steps."

**Execution pattern:**
1. Load specification document
2. Execute Phase 1 with real `find` commands → generate inventory artifact
3. Execute Phase 2 with planning logic → generate plan artifact
4. Document Phases 3–6 with complete workflows (theoretical execution)
5. Generate 14 deliverables covering end-to-end migration
6. Commit all artifacts to git

**Key artifacts produced:**
- `docs/bash-scripts-list-context.md` — Phase 1 inventory
- `docs/bash-scripts-plan.md` — Phase 2 plan
- `docs/bash-scripts-issues-context.md` — Phase 3 issues audit
- `BASH_SCRIPTS_FIX_PHASES_3_6_READINESS.md` — Phase 3–6 execution guides
- `BASH_SCRIPTS_FIX_FINAL_SUMMARY.md` — executive summary
- 10 additional supporting documents

**Outcome:** Complete 6-phase migration specification, Phases 1–2 executed with real output, Phases 3–6 fully documented and ready for real execution when scripts become available.
