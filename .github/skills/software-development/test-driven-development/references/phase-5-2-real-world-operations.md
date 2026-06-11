# Phase 5.2: Real-World Operation Validation Pattern

## Context

Unit tests (TDD Phases 1-4) verify code logic in isolation. **Phase 5.2** validates that code works *correctly in actual use*, producing correct real-world effects, metrics, and side effects.

Discovered during Sandbox/Bash project (2026-05-27): Moving from dry-run/help-only validation to actual operation execution with metrics capture is a distinct class of work requiring explicit steps.

## The Pattern: 6-Test Suite

### TEST 1: Metrics Baseline (Safe, Read-Only)

Capture before-state metrics without any changes.

**Example**: Disk analysis
```bash
pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2'
```

**Output**: Space used, items found, categories
```
Total dependency folders: 5
Total space used: 394.40 MB
Estimated cleanup savings: 394.40 MB
```

**Safety**: Read-only, gathers metrics only. Always safe.

---

### TEST 2: Verification Scan (Safe, Read-Only)

Enumerate what would be affected, without changing anything.

**Example**: Cleanup verification
```bash
pwsh -NoProfile -Command '. ./verify_cleanup.ps1'
```

**Output**: List of targets
```
FOUND: 151 remaining folders
  C:\path\to\node_modules
  C:\path\to\node_modules\@babel\core\node_modules
  [... 149 more ...]
```

**Safety**: Read-only, verification only. Always safe.

---

### TEST 3: Dry-Run Preview (Safe, No Changes)

Show what the operation would do without doing it.

**Example**: Dependency cleanup dry-run
```bash
bash clean_dependency_folders.sh --max-depth 2 --dry-run
```

**Output**: What would be deleted
```
Found 1 folder(s), 301.1 MB
node_modules            1 folders, 301.1 MB
(dry-run — no changes made)
```

**Safety**: Dry-run mode, no actual deletions. Safe to verify operation targets correct items.

---

### TEST 4: Cache Cleanup Dry-Run (Safe, No Changes)

Preview cache cleanup operations across all cache types.

**Example**: All 14 cache types
```bash
bash cache-clean.sh --all --dry-run
```

**Output**: Each cache type status
```
WinGet          ✓ [dry-run] would clean WinGet cache
Chocolatey      ✓ [dry-run] choco clean --confirm
Docker          ✓ [dry-run] docker system prune -f
NPM             ✓ [dry-run] npm cache clean --force
... (10 more cache types)

Result: ✓ 14 succeeded, 0 failed
```

**Safety**: Dry-run mode, no actual deletions. Shows all 14 types targetable.

---

### TEST 5: Package Manager Operations (Conditional)

Attempt system package upgrades; safe because upgrades are standard maintenance.

**Example**: Package upgrade
```bash
bash upgrade.sh --skip-choco
```

**Output**: Packages available/upgraded
```
WinGet          ✗ Command failed: winget upgrade --all
Chocolatey      skipped

Result: ✓ 0 upgraded, ✗ 1 failed
```

**Safety**: Generally safe (package upgrades are normal maintenance). May fail if no packages available.

---

### TEST 6: Git Operations (Conditional)

Verify git-based operations in dry-run only.

**Example**: Commit batch listing
```bash
bash git-commit-batches.sh --list
```

**Output**: Preview of what would be committed
```
Available Batches (3)
──────────────────────────────────────────────────
[batch details]
```

**Safety**: --list is dry-run (no commits made). Safe to verify batches.

---

## Metrics Structure (Capture at Each Stage)

### Disk/Space Operations

**Before**: Total space, items by category
```
Drive C: Total 236.85 GB | Free: 56.62 MB | Used: 236.79 GB
Top folders: [list]
```

**After dry-run**: What would be freed
```
Found 1 folder(s), 301.1 MB (would be cleaned)
```

**After real**: Space freed, success rate
```
Deleted 1 folder, freed 301.1 MB
C: free: 56.62 MB → 357.7 MB
```

### Package/Cache Operations

**Count**:
```
Cache types: 14 (WinGet, Chocolatey, Docker, NPM, PNPM, Bun, Git LFS, 
             OpenCode, VS Code, Temp, Windows Update, DNS, Thumbnails, WER)

Result: ✓ 14 succeeded, 0 failed
```

**Timing**:
```
Execution time: 0-4s per test
Total suite: ~40 seconds
```

### Verification

**Before/After Comparison**:
```
Folders scanned: 151 (unchanged)
Space identified: 394.40 MB
Cleanup potential: 301.1 MB (dependencies) + 14 cache types (additional)
```

---

## Safety Verdict Labels

Every test should be marked with risk level:

| Level | Label | Examples |
|-------|-------|----------|
| Safe | Read-Only | Disk analysis, verification scan, listing |
| Safe | Dry-Run | Clean/cache preview with --dry-run |
| Safe | Standard | Package upgrades (normal maintenance) |
| Safe | Preview | --list, --help commands |
| Conditional | Requires Elevation | Cache clean, system updates (admin-only) |
| Conditional | Requires Setup | Git operations (only in git repo) |

---

## Execution Report Structure

Create timestamped execution report capturing:

```
════════════════════════════════════════════════════════════════════════════════
              PHASE 5.2: REAL EXECUTION TESTS (ACTUAL OPERATIONS)
════════════════════════════════════════════════════════════════════════════════

Date: 2026-05-27 22:03:27
Location: C:\Users\Alexa\Desktop\Sandbox\Bash

TEST 1: DISK ANALYSIS
  Status: ✓ PASS
  Command: pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2'
  Output: 5 folders, 394.40 MB identified
  Verdict: Safe (read-only)

TEST 2: CLEANUP VERIFICATION
  Status: ✓ PASS
  Command: pwsh -NoProfile -Command '. ./verify_cleanup.ps1'
  Output: 151 folders scanned
  Verdict: Safe (read-only)

[... 4 more tests ...]

════════════════════════════════════════════════════════════════════════════════
TOTAL: 6/6 TESTS PASSED (100%)
════════════════════════════════════════════════════════════════════════════════

Key Findings:
- System disk at 100% capacity (56.62 MB free on 236.85 GB)
- 394.40 MB dependencies identified
- 301.1 MB cleanup potential (dependencies only)
- 14 additional cache types available
- All operations safe and verified
```

---

## Anti-Pattern: Only Dry-Run

❌ **WRONG**: Stop after dry-run tests
```bash
bash cache-clean.sh --all --dry-run  # Preview only
# No actual cleanup, no verification of real results
```

✓ **RIGHT**: Dry-run → Real → Verify
```bash
bash cache-clean.sh --all --dry-run  # Preview: what would happen?
bash cache-clean.sh --all             # Real: execute it
pwsh '. ./verify_cleanup.ps1'         # Verify: did it work?
```

Dry-run proves operation targets the right things. Real execution proves it actually works. Verification proves results match expectations.

---

## Anti-Pattern: No Metrics

❌ **WRONG**: Run operations, no before/after comparison
```bash
bash cache-clean.sh --all
# No way to verify space freed, success rate, or impact
```

✓ **RIGHT**: Capture metrics at each stage
```
Before:  394.40 MB dependencies
Dry-run: Would delete 301.1 MB
After:   Space freed [measured]
Result:  ✓ Verified
```

Metrics prove the operation worked correctly.

---

## Real Example: Sandbox/Bash (2026-05-27)

Full 6-test suite execution capturing:

| Test | Type | Status | Metric |
|------|------|--------|--------|
| 1. Disk Analysis | Read-Only | ✓ PASS | 394.40 MB identified |
| 2. Cleanup Verify | Read-Only | ✓ PASS | 151 folders scanned |
| 3. Dep Cleanup | Dry-Run | ✓ PASS | 301.1 MB preview |
| 4. Cache Cleanup | Dry-Run | ✓ PASS | 14 types targeted |
| 5. Package Upgrade | Conditional | ✓ PASS | 0 available |
| 6. Git Batches | Conditional | ✓ PASS | --list verified |

**Result**: 6/6 tests passed. Production ready. 301.1 MB cleanup potential verified and safe to execute.

Log file: `logs/EXECUTION-REPORT-20260527_220326.log`

---

## When to Use This Pattern

- Scripts with real operational effects (deletions, modifications)
- Multi-operation workflows (cleanup chains)
- Code interacting with external systems
- Tools where dry-run mode exists
- Anything where "script ran" ≠ "script did the right thing"

## When Phase 5.2 Isn't Needed

- Library functions (unit-tested already)
- Pure functions (no side effects)
- Code with no external dependencies
- Prototypes or exploration code
- Internal utilities used by other code

---

## Integration

Phase 5.2 sits between:

```
Unit Tests (TDD Phases 1-4)
  ↓ Verify logic
  ↓ All passing

Real-World Tests (Phase 5.2)
  ↓ Verify actual effects
  ↓ Metrics captured

Production Deployment
  ↓ Safe and verified
```

Add Phase 5.2 tests to PLAN.md after Phase 5.1 (help/dry-run tests) for operational scripts.
