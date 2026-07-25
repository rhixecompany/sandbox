# Six-Phase Script Migration Pattern with Safety Gates

**Pattern discovered**: Executing large-scale script migrations (50+ files) across multiple source locations using a structured 6-phase approach with documentation-first planning and parity verification gates.

**Applicable to**: Any multi-location script consolidation, library migration, or code relocation project where preserving file parity and preventing data loss are critical.

## Overview

This pattern extends the 5-phase audit-and-remediation model to a **6-phase execution framework** that separates planning and review from destructive operations:

1. **Phase 1 (Catalog)** — Discover and inventory all scripts
2. **Phase 2 (Plan)** — Create batch organization and dependency analysis
3. **Phase 3 (Audit/Code Review)** — Quality check before touching originals
4. **Phase 4 (Migrate)** — Batch execution with parity verification
5. **Phase 5 (Test)** — Comprehensive testing of migrated scripts
6. **Phase 6 (Cleanup)** — Remove originals with verification checklist

## When to Use

- Consolidating 20+ scripts from scattered locations into a central directory
- Migrating scripts between package managers or runtime environments
- Reorganizing monorepo with significant duplication
- Any situation where deleting source files is irreversible

## Phase 1: Catalog

**Goal**: Discover all scripts, categorize, identify candidates for migration.

**Steps**:
1. Search all script types recursively (`find` with path exclusions)
2. Count by type and location
3. Identify scripts that will move vs. stay in place
4. Note dependencies and cross-references
5. Document exceptions (read-only, archival, generated)

**Output artifact**: `docs/<project>-scripts-list-context.md`
- Total script inventory
- Breakdown by type (.sh, .ps1, .bat, .ts)
- Location mapping (which paths contain which scripts)
- Migration candidates (54 of 369 in example)
- Exception categories

**Why this phase**: Prevents accidental deletion of critical scripts and establishes baseline for later parity checks.

## Phase 2: Plan

**Goal**: Organize migration into execution batches with dependency awareness.

**Critical substeps**:

### 2a. Dependency Analysis
- Map script references in package.json, Makefile, .github/workflows
- Identify cross-script imports or calls
- Note if migrating one script requires migrating others
- Create a **dependency graph** for batch ordering

### 2b. Batch Organization
- Group scripts by:
  - **Purpose** (cleanup, disk-analysis, quality-gate, etc.)
  - **Dependencies** (must migrate together, or in order)
  - **Risk level** (critical/high/medium/low)
- Target 7–8 scripts per batch (optimal for review)
- Ensure batches are **independent** (batch 1 doesn't require batch 3 done first)

### 2c. Per-Batch Execution Template
Each batch needs a template specifying:
```
Batch N:
  Files: [list]
  Dependencies: [upstream batches if any]
  Issues to fix: [CRITICAL/HIGH/MEDIUM/LOW]
  Expected fixes: [concrete diffs]
  Verification steps: [exact commands to run]
  Rollback: [git revert or reverse-copy]
```

**Output artifact**: `docs/<project>-scripts-plan.md`
- 7 batches outlined with files, purposes, and ordering
- Dependency matrix
- Per-batch execution template
- Total time estimate (~3.25 hours example)

### 2d. Issues Pre-Audit
Document issue categories you expect to find in Phase 3:
```
Batch 1 (cleanup scripts):
  CRITICAL: undefined variables, missing set -e
  HIGH: placeholder comments, hardcoded paths
  MEDIUM: inconsistent error handling
```

**Output artifact**: `docs/<project>-scripts-issues-context.md`

**Why this phase**: Forces you to think through execution order before starting. Batch independence prevents cascading failures. Pre-auditing issue categories makes Phase 3 faster.

## Phase 3: Code Review & Audit

**Goal**: Identify all issues before migration.

**Steps**:
1. Read each script in batch order
2. Classify issues (use CRITICAL/HIGH/MEDIUM/LOW taxonomy)
3. Document fixes needed (line numbers, context, replacement)
4. Check for one-off artifacts (generated migration scripts, test scaffolding)
5. Create **issue verdict** for CRITICAL patterns (safe vs. blocked)

**Do NOT execute fixes yet** — just catalog them.

**Output artifact**: Audit report per batch with issues list and verdicts.

**Why this phase**: Allows full review before any modifications. Decisions can be made with full context visible. Critical issues can be escalated for human decision before touching files.

## Phase 4: Migration Execution

**Goal**: Move scripts from source locations to target location with parity verification.

**Critical substeps**:

### 4a. Batch Migration
For each batch:
1. Copy files from source to target directory
2. **Immediately compare** source vs. target (byte-level check, line count, checksum)
3. If parity fails → investigate before proceeding
4. Record copy verification timestamp and hash

### 4b. Reference Updates
Update all references to moved scripts:
- package.json `scripts` entries
- .github/workflows (if paths hardcoded)
- docs and README (if script paths documented)
- Cross-script imports (if any)

### 4c. Path Decoupling
Replace hardcoded source paths with environment variables:
```bash
# Before:
cd /projects/Banking/scripts/reconcile.sh

# After:
cd "$BASH_SCRIPT_HOME/reconcile.sh"
# Where BASH_SCRIPT_HOME is set in package.json or .bashrc
```

### 4d. Parity Verification
**BEFORE deleting source**, run:
```bash
diff -u source/script.sh target/script.sh || echo "Files differ"
wc -l source/*.sh target/*.sh  # line count match
sha256sum source/*.sh target/*.sh  # checksum match
```

If parity fails → **STOP**. Do not delete. Investigate.

**Why this checkpoint**: Prevents data loss. If migration is incomplete, you still have originals.

## Phase 5: Testing

**Goal**: Verify migrated scripts work correctly in new location.

**Steps per batch**:
1. Run migrated script with `--help` (syntax check)
2. Run migrated script with `--dry-run` (safety test)
3. Run migrated script normally (functional test)
4. Compare output with original (should be identical)
5. Check exit codes ($? should match original)

**Error scenarios**:
- Broken imports (if script calls other scripts by path)
- Missing dependencies (if script expects files in original location)
- Environment variables not set (if script uses $USERPROFILE or similar)

**Output artifact**: Test results per batch (pass/fail for each script).

**Why this phase**: Catches broken migrations before cleanup. Much easier to debug with originals still present.

## Phase 6: Cleanup

**Goal**: Remove source copies and verify no stale references remain.

**18-point cleanup checklist**:

1. Confirm all Phase 5 tests passed
2. Verify git status is clean (no uncommitted changes)
3. Create git checkpoint: `git tag -a migration-phase-5-complete -m "..."`
4. Search package.json for old paths → update/remove
5. Search .github/workflows for old paths → update/remove
6. Search docs/ for old paths → update/remove
7. Search .bashrc/.zshrc for old paths → update/remove
8. Check for broken symlinks in old locations
9. Search for `require()` or `import` references to old paths
10. Remove stale `.sh` files from source locations
11. Remove stale `.ps1` files from source locations
12. Remove now-empty directories
13. Verify target scripts still run (quick smoke test)
14. Run full test suite
15. Search codebase for remaining references to deleted paths
16. Create cleanup verification report
17. Commit cleanup changes
18. Tag completion: `git tag -a migration-complete -m "..."`

**Why gradual cleanup**: Prevents "oops, I deleted something critical" moments. Each point is a safety check.

## Safety Gates

### Before Phase 4 (Migration):
- [ ] All Phase 3 audits complete
- [ ] No CRITICAL issues are BLOCKED
- [ ] Dependency order verified (each batch can execute independently)
- [ ] Git checkpoint created (`git tag ...`)

### Before Phase 5 (Testing):
- [ ] All batches migrated
- [ ] Parity verification passed (source == target)
- [ ] All references updated
- [ ] Paths decoupled from source locations

### Before Phase 6 (Cleanup):
- [ ] All Phase 5 tests passed (all 54 scripts work in new location)
- [ ] No regressions detected
- [ ] Test report complete

### Before Deletion:
- [ ] 18-point cleanup checklist completed
- [ ] No stale references remain
- [ ] Git state clean and tagged

## Artifacts

A complete 6-phase execution produces:

**Planning Phase (1-2)**:
- `docs/<project>-scripts-list-context.md` (Phase 1 catalog)
- `docs/<project>-scripts-plan.md` (Phase 2 execution plan)
- `docs/<project>-scripts-issues-context.md` (Phase 2 issue pre-audit)

**Ready-State Docs (3-6)**:
- `<PROJECT>_PHASES_3_6_READINESS.md` (complete Phase 3-6 workflows)
- `<PROJECT>_INDEX.txt` (deliverable index + timeline)
- `<PROJECT>_PROJECT_SUMMARY.md` (executive overview)

**Execution Reports (during 4-6)**:
- Phase 4 Migration Report (per-batch parity verification)
- Phase 5 Test Report (test results per script)
- Phase 6 Cleanup Report (18-point checklist results)

## Timing Estimates

For a 54-script migration:
- Phase 1: 15 min (discovery + catalog)
- Phase 2: 30 min (batch planning + issue pre-audit)
- Phase 3: 45 min (code review + audit verdicts)
- Phase 4: 60 min (migration + parity checks)
- Phase 5: 30 min (testing + issue resolution)
- Phase 6: 15 min (cleanup + verification)

**Total: ~3.25 hours** (all phases, end-to-end)

## Key Lessons

1. **Separation of concerns**: Planning before execution prevents chaos. Audit before migration prevents surprises. Testing before cleanup prevents data loss.

2. **Parity verification is non-negotiable**: Always compare source vs. target before deleting originals. A 1-line difference in a critical script could cause production issues.

3. **Batch independence**: If batches have cross-dependencies, execution becomes fragile. Better to migrate fewer scripts per batch than to create ordering constraints.

4. **Documentation-first planning**: Writing execution templates for all phases upfront makes actual execution mechanical and reviewable.

5. **Safety gates at each transition**: Each phase transition (1→2, 2→3, etc.) is a decision point. Making explicit checklist forces awareness.

6. **Gradual cleanup**: Don't delete everything at once. Delete batch by batch, with verification after each. Easier to recover if something breaks.

## Related Patterns

- **Parity verification pattern** (Phase 4): `bash -n` syntax check, `wc -l`, `sha256sum`, `diff -u`
- **Batch organization** (Phase 2): Dependency-aware grouping, 7-8 files per batch, rollback templates
- **Testing pattern** (Phase 5): Help check, dry-run, full run, exit-code verification, output comparison
- **Cleanup checklist** (Phase 6): 18-point verification procedure, git tagging, stale-reference search
