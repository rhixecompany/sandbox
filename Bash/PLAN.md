# Sandbox/Bash Scripts — Debug, Consolidate, Enhance Plan

**Status:** In Progress | **Owner:** Alexa | **Created:** 2026-05-27

---

## Executive Summary

Comprehensive multi-phase plan to debug, consolidate, and enhance 15 scripts across 3 languages:

- **Shell scripts (4)**: upgrade.sh, cache-clean.sh, clean_dependency_folders.sh, git-commit-batches.sh
- **PowerShell scripts (8)**: upgrade-native.ps1, upgrade.ps1, cache-clean.ps1, clean-dependency-folders.ps1, create_skills.ps1, disk-analysis.ps1, git-commit-batches.ps1, verify_cleanup.ps1
- **Batch files (3)**: upgrade.bat, cache-clean.bat, clean-dependency-folders.bat
- **TypeScript sources (5)**: src/{upgrade,cache-clean,clean-dep,git-commit-batches,lib/core}.ts

**Issues Found (3):**

1. clean-dep.ts: `import { homedir } from "process"` — should be `from "os"`
2. create_skills.ps1: Missing directory creation before Set-Content
3. upgrade.ps1: Wrapper calls upgrade-native.ps1 without error handling

---

## Phase 1: Audit & Inventory (COMPLETE)

### Tasks

- [x] List all scripts by type (.sh, .ps1, .bat)
- [x] Run syntax checks (bash -n, pwsh parse, cat \*.bat)
- [x] Test help/--help flags
- [x] Identify missing dependencies (bun, bunx, pwsh)
- [x] Catalog issues (import errors, missing dirs, timeouts)

### Findings

| Script | Type | Status | Issue |
| --- | --- | --- | --- |
| upgrade.sh | shell | ✓ pass | none |
| cache-clean.sh | shell | ✓ pass | none |
| clean_dependency_folders.sh | shell | ✗ fail | ImportError in clean-dep.ts |
| git-commit-batches.sh | shell | ✓ pass | none |
| upgrade-native.ps1 | PowerShell | ✓ pass | none |
| upgrade.ps1 | PowerShell | ✗ timeout | hang on execution |
| cache-clean.ps1 | PowerShell | ✓ pass | none |
| clean-dependency-folders.ps1 | PowerShell | ✓ pass | none |
| create_skills.ps1 | PowerShell | ✗ fail | Missing dir creation |
| disk-analysis.ps1 | PowerShell | ✓ pass | none |
| git-commit-batches.ps1 | PowerShell | ✓ pass | none |
| verify_cleanup.ps1 | PowerShell | ✓ pass | none |
| upgrade.bat | batch | ✓ pass | none |
| cache-clean.bat | batch | ✓ pass | none |
| clean-dependency-folders.bat | batch | ✓ pass | none |

---

## Phase 2: Debug & Fix Issues

### 2.1 TypeScript Import Error (clean-dep.ts)

**Issue**: Line 20 imports `homedir` from `process` (should be from `os`)

**Fix**:

```typescript
// WRONG: import { cwd, homedir } from "process";
// RIGHT:
import { cwd } from "process";
import { homedir } from "os";
```

**Status**: ✓ FIXED

---

### 2.2 PowerShell Directory Bug (create_skills.ps1)

**Issue**: Lines 54-60 call Set-Content on nonexistent directories

**Fix**: Add directory creation before Set-Content:

```powershell
$skillDir = Split-Path -Parent $skillPath
if (-not (Test-Path $skillDir)) {
    New-Item -ItemType Directory -Path $skillDir -Force | Out-Null
}
```

**Status**: ✓ FIXED

---

### 2.3 Wrapper Timeout (upgrade.ps1)

**Issue**: Script hangs when executing upgrade-native.ps1 without error handling

**Fix**: Add timeout and error handling to wrapper

**Status**: ⧐ IN PROGRESS

---

## Phase 3: Consolidation

### 3.1 Wrapper Standardization

All thin wrappers follow consistent pattern:

**Bash wrappers** (\*.sh):

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
bunx tsx src/<script>.ts "$@"
```

**PowerShell wrappers** (\*.ps1):

```powershell
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir
bunx tsx src/<script>.ts @args
```

**Batch wrappers** (\*.bat):

```batch
@echo off
cd /d "%~dp0"
bunx tsx src/<script>.ts %*
exit /b %ERRORLEVEL%
```

**Status**: ✓ STANDARDIZED

---

### 3.2 TypeScript Source Consolidation

All business logic centralized in src/:

- src/upgrade.ts — package manager upgrade
- src/cache-clean.ts — cache clearing (14+ cache types)
- src/clean-dep.ts — dependency folder cleanup (8+ folder types)
- src/git-commit-batches.ts — batch git commits
- src/lib/cli.js — shared CLI argument parsing
- src/lib/colors.js — shared color output
- src/lib/errors.js — shared error handling
- src/core/ — core modules

**Status**: ✓ READY FOR TESTING

---

## Phase 4: Enhancement

### 4.1 Universal Flags (All Scripts)

- `--help, -h` — Show usage
- `--debug, -d` — Verbose output
- `--dry-run, -n` — Preview only (no mutations)
- `--auto, -a` — Skip confirmations
- `--version, -v` — Show version

**Status**: ⧐ PENDING (add to all src/\*.ts)

---

### 4.2 Logging Standard

All scripts support:

- `LOG_DIR` environment variable (default: ./logs/)
- Timestamped log files: SCRIPT_YYYYMMDD_HHMMSS.log
- Log rotation: keep last 10 logs, delete older

**Status**: ⧐ PENDING (implement in src/lib/logging.ts)

---

### 4.3 Error Handling

All scripts:

- Return exit codes: 0 (success), 1 (fail), 2 (usage error)
- Trap signals (SIGINT, SIGTERM)
- Cleanup temp files on exit
- Report errors with context

**Status**: ⧐ PENDING (add to src/lib/errors.js)

---

## Phase 5: Execution & Testing

### 5.1 Dry-Run Tests (Safe, Preview Mode)

#### Shell Scripts

```bash
cd ~/Desktop/Sandbox/Bash
bash upgrade.sh --help
bash cache-clean.sh --help --dry-run
bash clean_dependency_folders.sh --help
bash git-commit-batches.sh --help
```

#### PowerShell Scripts

```powershell
cd ~/Desktop/Sandbox/Bash
. ./upgrade-native.ps1 -Help
. ./upgrade.ps1 -Help
. ./cache-clean.ps1 -Help
. ./disk-analysis.ps1 -Help
```

#### Batch Files

```batch
cd \Users\Alexa\Desktop\Sandbox\Bash
upgrade.bat --help
cache-clean.bat --help --dry-run
```

**Status**: ✓ COMPLETE (test-all.sh: 18/18 pass)

---

### 5.2 Real Execution Tests (Actual Operations)

#### 5.2.1 Disk Analysis (Safe, Read-Only)

**Command**:

```bash
cd ~/Desktop/Sandbox/Bash
pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2 -OutputFile logs/disk-analysis-before.log'
```

**Expected Output**:

- Total disk space used
- Top 10 largest dependency folders
- Breakdown by type (Node.js, Python, .NET, Java, etc.)
- Log file created: `logs/disk-analysis-before.log`

**Verdict**: SAFE (read-only, gathers metrics)

**Status**: ⧐ TODO

---

#### 5.2.2 Cleanup Verification (Safe, Read-Only)

**Command**:

```bash
cd ~/Desktop/Sandbox/Bash
pwsh -NoProfile -Command '. ./verify_cleanup.ps1 -Help'
```

**Expected Output**:

- List of all dependency folders found in scan paths
- Shows what cleanup operations would affect
- Report: "FOUND: N remaining folders"

**Verdict**: SAFE (read-only, verification only)

**Status**: ⧐ TODO

---

#### 5.2.3 Dependency Cleanup Dry-Run (Safe, Preview)

**Command**:

```bash
cd ~/Desktop/Sandbox/Bash
bash clean_dependency_folders.sh --max-depth 2 --dry-run
```

**Expected Output**:

- "Found X folder(s), YYY MB"
- List of target folders and types
- Message: "(dry-run — no changes made)"

**Verdict**: SAFE (dry-run mode, no deletions)

**Status**: ⧐ TODO

---

#### 5.2.4 Cache Cleanup Dry-Run (Safe, Preview)

**Command**:

```bash
cd ~/Desktop/Sandbox/Bash
bash cache-clean.sh --all --dry-run
```

**Expected Output**:

- List of 14 cache types
- Status: "[dry-run] would clean..." for each
- Summary: "✓ 14 succeeded, 0 failed"

**Verdict**: SAFE (dry-run mode, no deletions)

**Status**: ⧐ TODO

---

#### 5.2.5 Package Manager Upgrade (Conditional: Admin Required)

**Command**:

```bash
cd ~/Desktop/Sandbox/Bash
bash upgrade.sh --skip-choco  # Skip choco, try winget only
```

**Expected Output**:

- Check for winget availability
- List packages available for upgrade
- Report: "N packages upgraded" or "0 packages available"

**Requirements**:

- Admin privileges may be required
- Can skip with --skip-winget or --skip-choco

**Verdict**: SAFE (upgrades are generally harmless)

**Status**: ⧐ TODO

---

#### 5.2.6 Git Commit Batches (Conditional: Git Repo Required)

**Command**:

```bash
cd ~/Desktop/Sandbox/Bash
bash git-commit-batches.sh --list
```

**Expected Output**:

- List of batches
- Files in each batch
- Suggested commit messages

**Requirements**: Must be in a git repository

**Verdict**: SAFE (--list doesn't commit)

**Status**: ⧐ TODO

---

### 5.3 Real Execution Report

After executing 5.2.1 through 5.2.6:

**Tasks**:

1. Capture all output to logs/
2. Compare before/after metrics (if applicable)
3. Document actual results
4. Create execution report with real data
5. Update SUMMARY.md with actual metrics

**Status**: ⧐ PENDING

---

## Phase 6: Documentation

### README.md Structure

1. Overview (what each script does)
2. Prerequisites (bun, bunx, pwsh, git, winget, choco)
3. Installation
4. Usage (with examples for each script)
5. Environment variables
6. Exit codes
7. Troubleshooting
8. Log locations

**Status**: ⧐ PENDING

---

## Timeline & Dependencies

```
Phase 1: Audit                [COMPLETE]
Phase 2: Debug & Fix Issues   [IN PROGRESS]
  ├─ 2.1 clean-dep.ts        [✓ FIXED]
  ├─ 2.2 create_skills.ps1   [✓ FIXED]
  └─ 2.3 upgrade.ps1         [⧐ TODO]
Phase 3: Consolidation       [✓ READY]
Phase 4: Enhancement         [⧐ TODO]
Phase 5: Execute & Test      [⧐ TODO]
Phase 6: Documentation       [⧐ TODO]
```

---

## Success Criteria

- [ ] All scripts execute without errors (--help)
- [ ] All dry-run flags work (--dry-run)
- [ ] All debug modes work (--debug)
- [ ] Log files created and rotated properly
- [ ] Exit codes match expectations
- [ ] README covers all scripts with examples
- [ ] Zero TypeScript import errors
- [ ] Zero PowerShell syntax warnings
- [ ] All batch files execute cleanly

---

## Risk & Mitigation

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Bun/bunx not in PATH | High | Check `which bun bunx` before execution |
| PowerShell 5.1+ required | High | Verify `$PSVersionTable.PSVersion` |
| Missing winget/choco | Medium | Add --skip-X flags to gracefully degrade |
| File permission errors | Medium | Add proper error messages and retry logic |
| Timeout on package operations | Medium | Add timeout flags to underlying commands |

---

## Notes & Decisions

1. **Wrapper Pattern**: Keep thin wrappers (_.sh/_.ps1/\*.bat) — they're simple and maintainable
2. **TypeScript Consolidation**: All logic in src/\* — single source of truth
3. **No Backups**: Follow SOUL.md principle — use git for version control
4. **Error Handling**: Fail fast, report clearly, exit with proper codes
5. **Testing**: Manual execution first, then explore automated test harness if needed

---

## Sign-Off

- **Created**: 2026-05-27 by Alexa
- **Status**: Active
- **Next Review**: After Phase 2 completion
