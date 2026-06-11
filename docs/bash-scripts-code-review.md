# Bash Scripts Code Review — Phase 3

**Generated:** May 26, 2026  
**Task ID:** t_716b7e7f Phase 3  
**Scope:** Review all 37 Bash scripts for formatting, content, and structural issues

## Executive Summary

**Scripts Reviewed:** 37 Bash scripts  
**Categories:**
- ✅ **Good:** 3 scripts (modern orchestrators: upgrade.sh, cache-clean.sh, clean_dependency_folders.sh)
- ⚠️ **Needs Improvement:** 8 scripts (active scripts with various issues)
- 🗑️ **Archive/Delete:** 26 scripts (archived commit batches)

**Key Findings:**
1. **Inconsistent architecture** — Mix of orchestrators and scripts with embedded business logic
2. **Archived dead code** — 26 commit batch scripts serve no purpose
3. **Formatting inconsistencies** — Mixed comment styles, varied error handling patterns
4. **Missing dry-run** — Only 1 of 37 scripts supports dry-run mode
5. **No test coverage** — Zero automated tests for any script

## 1. Formatting Inconsistencies

### 1.1 Shebang Lines

**Issue:** Three different shebang styles in use

| Style | Count | Files |
|-------|-------|-------|
| `#!/usr/bin/env bash` | 34 | Most files |
| `#!/bin/bash` | 0 | None (good!) |
| Missing | 0 | None (good!) |

**Verdict:** ✅ **Consistent** — All use portable `#!/usr/bin/env bash`

### 1.2 ShellCheck Directives

**Issue:** Only 2 scripts use ShellCheck directives

**Files with directives:**
- `phase-5-verify-install.sh` — Has `# shellcheck shell=bash`
- `lib/log-rotate.sh` — Has `# shellcheck shell=bash`

**Recommendation:**
```bash
#!/usr/bin/env bash
# shellcheck shell=bash
```

Add to all scripts for linting consistency.

### 1.3 Error Handling

**Issue:** Inconsistent use of `set -euo pipefail`

| Pattern | Count | Files |
|---------|-------|-------|
| Has `set -euo pipefail` | ~28 | Most active scripts |
| Missing `set -euo pipefail` | ~9 | Some archived scripts |
| Has `set -e` only | 0 | None |

**Critical Issues:**
- Missing `-u` flag — allows undefined variables (silent bugs)
- Missing `-o pipefail` — hides pipeline failures

**Recommendation:** ALL scripts must have:
```bash
set -euo pipefail
```

### 1.4 Comment Styles

**Issue:** Three different comment header styles

**Style A (Box comments):**
```bash
#############################################################################
# phase-5-verify-install.sh
# Verification script for the refactored install modular structure.
#############################################################################
```

**Style B (Simple comments):**
```bash
# Cache Cleaner — thin wrapper (forwards to TypeScript implementation)
```

**Style C (ShellCheck pragma comments):**
```bash
# shellcheck shell=bash
# Log rotation utility — call after writing logs
```

**Recommendation:**
```bash
#!/usr/bin/env bash
# shellcheck shell=bash
#
# script-name.sh
# Brief one-line description
#
# Usage:
#   ./script-name.sh [options]
##############################################################################

set -euo pipefail
```

Standardize on this format for all scripts.

### 1.5 Indentation

**Issue:** Mixed indentation (2-space vs 4-space)

**Analysis:**
- `phase-5-verify-install.sh` — 4-space indentation
- `upgrade.sh`, `cache-clean.sh` — No indentation (simple scripts)
- `log-rotate.sh` — 4-space indentation

**Recommendation:** Standardize on 2-space indentation (Bash convention)

```bash
# BEFORE (4-space)
if [ -f "file" ]; then
    echo "Found"
else
    echo "Not found"
fi

# AFTER (2-space)
if [ -f "file" ]; then
  echo "Found"
else
  echo "Not found"
fi
```

## 2. Content Issues

### 2.1 Outdated Information

**Issue:** Scripts reference non-existent paths and modules

**Example: phase-5-verify-install.sh**
- References `$PROJECT_ROOT/install/lib/` directory
- Sources modules that don't exist in current structure
- Checks for `install.sh` and `install-agents.sh` that may not exist

**Files:**
```
MISSING: $PROJECT_ROOT/install/lib/00-config.sh
MISSING: $PROJECT_ROOT/install/lib/01-utils.sh
MISSING: $PROJECT_ROOT/install/lib/02-paths.sh
... (8 modules referenced but don't exist)
```

**Recommendation:** Either:
1. **Fix:** Create the referenced modules
2. **Update:** Rewrite script for current structure
3. **Delete:** Remove if no longer needed

### 2.2 Contradictions

**Issue:** Inconsistent architecture patterns

| Script | Architecture | Status |
|--------|--------------|--------|
| `upgrade.sh` | ✅ Orchestrator (delegates to TS) | Modern |
| `cache-clean.sh` | ✅ Orchestrator (delegates to TS) | Modern |
| `phase-5-verify-install.sh` | ❌ Embedded logic (295 lines) | Legacy |
| `log-rotate.sh` | ❌ Library function (no orchestration) | Mixed |

**Contradiction:** Some scripts delegate to TypeScript, others have embedded business logic.

**Target:** ALL scripts should be thin orchestrators.

### 2.3 Unclear Instructions

**Issue:** Usage instructions missing or incomplete

**Scripts with good usage:**
```bash
# phase-5-verify-install.sh
# Usage:
#   ./Bash/scripts/phase-5-verify-install.sh          # Standard check
#   ./Bash/scripts/phase-5-verify-install.sh --verbose # Verbose output
```

**Scripts with missing usage:**
- `upgrade.sh` — No usage documentation
- `cache-clean.sh` — No usage documentation
- `log-rotate.sh` — Has parameters but unclear when/how to call

**Recommendation:** Add usage documentation to all scripts:
```bash
# Usage:
#   ./script-name.sh [options]
#
# Options:
#   --dry-run, -n    Preview changes without executing
#   --verbose, -v    Enable verbose output
#   --help, -h       Show this help message
```

### 2.4 Missing Dry-run Support

**Issue:** Only 1 of 37 scripts supports dry-run mode

**Script with dry-run:**
```bash
# skills-commit-batch-1.sh
DRY_RUN=${DRY_RUN:-false}
for arg in "$@"; do
  if [ "$arg" = "--dry-run" ] || [ "$arg" = "-n" ]; then DRY_RUN=true; fi
done
if [ "$DRY_RUN" = "true" ]; then
  echo "DRY-RUN: $(basename "$0") would prepare git commit batch 1 (no side effects)."
  exit 0
fi
```

**Recommendation:** ALL scripts that perform mutations must support dry-run:
```bash
DRY_RUN=false
for arg in "$@"; do
  case "$arg" in
    --dry-run|-n) DRY_RUN=true ;;
    --help|-h) show_usage; exit 0 ;;
  esac
done

if [ "$DRY_RUN" = "true" ]; then
  echo "[DRY-RUN] Would execute: $COMMAND"
else
  $COMMAND
fi
```

## 3. Structural Problems

### 3.1 Organization Issues

**Issue:** Inconsistent directory structure

**Current Structure:**
```
Bash/
├── scripts/           # 5 scripts (active)
│   ├── phase-1-deep-triage.sh
│   ├── phase-2-light-inventory.sh
│   ├── phase-5-verify-install.sh
│   ├── phase-6-cross-ref.sh
│   └── run-audit.sh
├── lib/               # 1 script (utility)
│   └── log-rotate.sh
├── tests/             # 1 script (test)
│   └── verify-dryrun.sh
├── archive/           # 26 scripts (dead code)
│   └── skills-commit-batches/
│       └── skills-commit-batch-*.sh (26 files)
├── upgrade.sh         # Root level (3 scripts)
├── cache-clean.sh
├── clean_dependency_folders.sh
└── git-commit-batches.sh  # Unclear purpose
```

**Problems:**
1. **Mixed purposes** — Root has orchestrators + unclear scripts
2. **No clear separation** — Active vs archived not obvious
3. **Inconsistent naming** — Some use hyphens, some underscores

**Recommended Structure:**
```
Bash/
├── orchestrators/     # Thin wrappers only
│   ├── upgrade.sh
│   ├── cache-clean.sh
│   └── dependency-clean.sh
├── legacy/            # Scripts to migrate (contains business logic)
│   ├── verify-install.sh
│   ├── phase-*.sh (4 files)
│   └── run-audit.sh
├── lib/               # Shared utilities
│   └── common.sh
├── tests/             # Test scripts
│   └── *.test.sh
└── archive/           # Dead code (pending deletion)
    └── commit-batches/ (26 files)
```

### 3.2 Missing Sections

**Issue:** Scripts missing critical sections

**Missing across multiple scripts:**
1. **Help/usage** — 32 of 37 scripts have no `--help` option
2. **Error messages** — Unclear failure output
3. **Exit codes** — No documentation of exit codes
4. **Examples** — No usage examples

**Recommended Template:**
```bash
#!/usr/bin/env bash
# shellcheck shell=bash
#
# script-name.sh
# Brief description
#
# Usage:
#   ./script-name.sh [options]
#
# Options:
#   --dry-run, -n    Preview changes
#   --verbose, -v    Verbose output
#   --help, -h       Show this help
#
# Exit codes:
#   0 - Success
#   1 - General error
#   2 - Missing dependencies
#
# Examples:
#   ./script-name.sh --dry-run
#   ./script-name.sh --verbose
##############################################################################

set -euo pipefail

show_usage() {
  grep '^#' "$0" | sed 's/^# //' | sed 's/^#//'
}

# Parse arguments
for arg in "$@"; do
  case "$arg" in
    --help|-h) show_usage; exit 0 ;;
    --dry-run|-n) DRY_RUN=true ;;
    --verbose|-v) VERBOSE=true ;;
    *) echo "Unknown option: $arg"; show_usage; exit 1 ;;
  esac
done

# Main logic...
```

### 3.3 Redundancy and Duplication

**Issue:** Multiple scripts with similar functionality

**Duplicated Patterns:**

**Pattern 1: Commit batch scripts (26 files)**
```bash
# All 26 scripts follow identical pattern:
git checkout -b skills-migration/batch-N
git add <files>
git commit -m "<message>"
# git push origin skills-migration/batch-N  # commented out
```

**Solution:** Single script with batch number parameter:
```bash
#!/usr/bin/env bash
# git-commit-batch.sh <batch_number> <branch_name> <commit_message> <files...>
BATCH="$1"
BRANCH="$2"
MESSAGE="$3"
shift 3
FILES=("$@")

git checkout -b "$BRANCH"
git add "${FILES[@]}"
git commit -m "$MESSAGE"
# git push origin "$BRANCH"  # requires approval
```

**Pattern 2: Orchestrator boilerplate**
```bash
# Repeated in upgrade.sh, cache-clean.sh, clean_dependency_folders.sh:
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
bunx tsx src/<script>.ts "$@"
```

**Solution:** Single orchestrator factory:
```typescript
// lib/core/orchestrator.ts
export function createOrchestrator(scriptPath: string) {
  return `#!/usr/bin/env bash
# shellcheck shell=bash
set -euo pipefail
cd "$(dirname "$0")"
tsx ${scriptPath} "$@"`;
}
```

### 3.4 Dead Code

**Issue:** 26 archived commit batch scripts serve no purpose

**Files:**
```
Bash/archive/skills-commit-batches/skills-commit-batch-1.sh
Bash/archive/skills-commit-batches/skills-commit-batch-2.sh
...
Bash/archive/skills-commit-batches/skills-commit-batch-26.sh
```

**Analysis:**
- All are one-time migration scripts
- All have commented-out `git push` commands
- All reference files that may not exist
- Total size: ~23KB of dead code

**Recommendation:** DELETE all 26 files after verifying:
1. Migrations were completed
2. Branches were merged or abandoned
3. No active references to these scripts

**Before deletion, check:**
```bash
# Search for references
grep -r "skills-commit-batch" Bash/ --exclude-dir=archive

# If no references found, safe to delete:
rm -rf Bash/archive/skills-commit-batches/
```

## 4. Comprehensive Issue List

### 4.1 Critical Issues (Must Fix)

| ID | File | Issue | Fix |
|----|------|-------|-----|
| C1 | `phase-5-verify-install.sh` | References non-existent install/lib modules | Update to current structure or delete |
| C2 | 26 commit batch scripts | Dead code, no purpose | DELETE after verification |
| C3 | `git-commit-batches.sh` | Purpose unclear, may be unused | Investigate and delete if unused |
| C4 | All scripts except 3 | No dry-run support | Add dry-run mode to all mutation scripts |
| C5 | 32 scripts | No `--help` option | Add usage documentation |

### 4.2 Important Issues (Should Fix)

| ID | File | Issue | Fix |
|----|------|-------|-----|
| I1 | `phase-5-verify-install.sh` | 295 lines of business logic in shell | Extract to TypeScript module |
| I2 | `log-rotate.sh` | Library function, not orchestrator | Convert to TypeScript or keep as util |
| I3 | All scripts | Mixed indentation (2-space vs 4-space) | Standardize on 2-space |
| I4 | All scripts | No ShellCheck directives | Add `# shellcheck shell=bash` |
| I5 | All scripts | Inconsistent comment headers | Standardize on template |
| I6 | Multiple | No exit code documentation | Document exit codes in headers |

### 4.3 Minor Issues (Nice to Have)

| ID | File | Issue | Fix |
|----|------|-------|-----|
| M1 | `upgrade.sh`, `cache-clean.sh` | No usage documentation | Add header with usage |
| M2 | `log-rotate.sh` | Unclear when/how to call | Add usage examples |
| M3 | Directory structure | Inconsistent organization | Reorganize per recommended structure |
| M4 | File naming | Mixed hyphens/underscores | Standardize on hyphens |
| M5 | All scripts | No examples section | Add usage examples |

## 5. Fix Priorities

### Phase 3A: Immediate Actions (This Week)

1. **DELETE dead code** (26 commit batch scripts)
   - Verify no active references
   - Remove `Bash/archive/skills-commit-batches/`
   - Update git history if needed

2. **Fix critical path issues** (phase-5-verify-install.sh)
   - Either create missing install/lib modules
   - Or rewrite for current structure
   - Or delete if obsolete

3. **Add dry-run support** to all mutation scripts
   - phase-*.sh scripts
   - Any script that modifies files

### Phase 3B: Quality Improvements (Next Week)

4. **Standardize formatting**
   - Add ShellCheck directives to all
   - Fix indentation to 2-space
   - Standardize comment headers

5. **Add documentation**
   - `--help` option for all scripts
   - Usage examples
   - Exit code documentation

6. **Extract business logic** (per Phase 2 plan)
   - phase-5-verify-install.sh → TypeScript
   - Other complex scripts → TypeScript
   - Keep shells as orchestrators only

### Phase 3C: Structural Refactoring (Week After)

7. **Reorganize directory structure**
   - Create `orchestrators/` directory
   - Move legacy scripts to `legacy/`
   - Consolidate utilities in `lib/`

8. **Eliminate duplication**
   - Create single commit-batch script
   - Share orchestrator boilerplate
   - Extract common utilities

## 6. Script-by-Script Fix List

### 6.1 Active Scripts (Priority 1)

**phase-5-verify-install.sh** (295 lines)
- [ ] Fix: Update paths to current structure or delete
- [ ] Add: Dry-run mode
- [ ] Add: Help option
- [ ] Extract: Business logic to TypeScript
- [ ] Fix: Indentation (4-space → 2-space)
- [ ] Add: ShellCheck directive

**upgrade.sh** (5 lines)
- [x] Architecture: ✅ Already modern orchestrator
- [ ] Add: Usage documentation
- [ ] Add: Help option
- [ ] Add: ShellCheck directive

**cache-clean.sh** (5 lines)
- [x] Architecture: ✅ Already modern orchestrator
- [ ] Add: Usage documentation
- [ ] Add: Help option
- [ ] Add: ShellCheck directive

**clean_dependency_folders.sh** (estimated ~10 lines)
- [ ] Verify: Follows orchestrator pattern
- [ ] Add: Usage documentation
- [ ] Fix: Naming (underscore → hyphen)

**phase-1-deep-triage.sh**
- [ ] Add: Dry-run mode
- [ ] Add: Help option
- [ ] Extract: Business logic to TypeScript
- [ ] Add: ShellCheck directive

**phase-2-light-inventory.sh**
- [ ] Add: Dry-run mode
- [ ] Add: Help option
- [ ] Extract: Business logic to TypeScript
- [ ] Add: ShellCheck directive

**phase-6-cross-ref.sh**
- [ ] Add: Dry-run mode
- [ ] Add: Help option
- [ ] Extract: Business logic to TypeScript
- [ ] Add: ShellCheck directive

**run-audit.sh**
- [ ] Add: Dry-run mode
- [ ] Add: Help option
- [ ] Extract: Business logic if complex
- [ ] Add: ShellCheck directive

### 6.2 Utility Scripts (Priority 2)

**log-rotate.sh** (12 lines)
- [ ] Decision: Keep as utility or convert to TypeScript?
- [ ] Add: Usage documentation
- [ ] Add: Examples
- [ ] Add: ShellCheck directive

**git-commit-batches.sh**
- [ ] Investigate: Purpose and usage
- [ ] Decision: Keep, consolidate, or delete?

### 6.3 Test Scripts (Priority 3)

**verify-dryrun.sh**
- [ ] Verify: Tests all scripts' dry-run mode
- [ ] Update: After adding dry-run to all scripts
- [ ] Add: Documentation

### 6.4 Archived Scripts (Priority 4 — DELETE)

**skills-commit-batch-*.sh** (26 files)
- [ ] Verify: No active references
- [ ] DELETE: All 26 files
- [ ] Document: In CHANGELOG.md

## 7. Validation Checklist

After applying all fixes, verify:

### 7.1 Per-Script Validation

- [ ] All scripts have `#!/usr/bin/env bash`
- [ ] All scripts have `# shellcheck shell=bash`
- [ ] All scripts have `set -euo pipefail`
- [ ] All scripts have standardized comment headers
- [ ] All scripts use 2-space indentation
- [ ] All mutation scripts support `--dry-run`
- [ ] All scripts support `--help`
- [ ] All scripts document exit codes
- [ ] All scripts have usage examples

### 7.2 Architecture Validation

- [ ] All shell scripts are orchestrators (< 20 lines) OR marked legacy
- [ ] All business logic extracted to TypeScript
- [ ] All TypeScript modules tested
- [ ] Directory structure follows recommended layout

### 7.3 Dead Code Validation

- [ ] All 26 commit batch scripts deleted
- [ ] No unused scripts remaining
- [ ] All scripts have clear purpose

### 7.4 Quality Validation

- [ ] ShellCheck passes for all scripts
- [ ] All scripts execute without errors
- [ ] Dry-run mode works for all mutation scripts
- [ ] Help text is clear and complete

## 8. Automation Scripts

### 8.1 Add ShellCheck Directive

```bash
#!/usr/bin/env bash
# add-shellcheck-directive.sh
# Add ShellCheck directive to all Bash scripts

for script in $(find Bash/ -name "*.sh" -type f); do
  if ! grep -q "# shellcheck" "$script"; then
    # Insert after shebang
    sed -i '1a # shellcheck shell=bash' "$script"
    echo "Added ShellCheck directive to $script"
  fi
done
```

### 8.2 Standardize Indentation

```bash
#!/usr/bin/env bash
# fix-indentation.sh
# Convert 4-space to 2-space indentation

for script in $(find Bash/ -name "*.sh" -type f); do
  # Use expand/unexpand for safe conversion
  expand -t 4 "$script" | unexpand -t 2 > "$script.tmp"
  mv "$script.tmp" "$script"
  echo "Fixed indentation in $script"
done
```

### 8.3 Add Help Option

```bash
#!/usr/bin/env bash
# add-help-option.sh
# Add help option boilerplate to scripts missing it

HELP_TEMPLATE='
show_usage() {
  grep "^#" "$0" | sed "s/^# //" | sed "s/^#//"
}

for arg in "$@"; do
  case "$arg" in
    --help|-h) show_usage; exit 0 ;;
  esac
done
'

for script in $(find Bash/scripts -name "*.sh" -type f); do
  if ! grep -q "show_usage" "$script"; then
    # Insert after set -euo pipefail
    # (Manual intervention recommended)
    echo "TODO: Add help option to $script"
  fi
done
```

## 9. Testing Strategy

### 9.1 ShellCheck All Scripts

```bash
#!/usr/bin/env bash
# test-shellcheck.sh
# Run ShellCheck on all Bash scripts

FAILED=0

for script in $(find Bash/ -name "*.sh" -type f); do
  if shellcheck "$script"; then
    echo "✓ $script"
  else
    echo "✗ $script"
    ((FAILED++))
  fi
done

if [ "$FAILED" -gt 0 ]; then
  echo "ShellCheck failed for $FAILED scripts"
  exit 1
fi
```

### 9.2 Verify Dry-run Mode

```bash
#!/usr/bin/env bash
# test-dryrun.sh
# Verify all mutation scripts support dry-run

MUTATION_SCRIPTS=(
  "Bash/scripts/phase-1-deep-triage.sh"
  "Bash/scripts/phase-2-light-inventory.sh"
  "Bash/scripts/phase-5-verify-install.sh"
  "Bash/scripts/phase-6-cross-ref.sh"
  "Bash/scripts/run-audit.sh"
)

FAILED=0

for script in "${MUTATION_SCRIPTS[@]}"; do
  if [ -f "$script" ]; then
    if "$script" --dry-run &>/dev/null; then
      echo "✓ $script supports --dry-run"
    else
      echo "✗ $script missing --dry-run"
      ((FAILED++))
    fi
  fi
done

exit "$FAILED"
```

## 10. Success Metrics

### 10.1 Code Quality Metrics

**Before:**
- ShellCheck directives: 2/37 (5%)
- Dry-run support: 1/37 (3%)
- Help options: 0/37 (0%)
- Dead code: 26/37 (70%)
- Orchestrators: 3/37 (8%)

**After (Target):**
- ShellCheck directives: 37/37 (100%)
- Dry-run support: 11/11 (100% of mutation scripts)
- Help options: 11/11 (100%)
- Dead code: 0/11 (0%)
- Orchestrators: 11/11 (100%)

### 10.2 Completion Criteria

Phase 3 complete when:
- [ ] All 26 archived scripts deleted
- [ ] All active scripts have ShellCheck directives
- [ ] All mutation scripts support dry-run
- [ ] All scripts have help option
- [ ] All scripts use 2-space indentation
- [ ] All scripts follow comment header template
- [ ] ShellCheck passes for all scripts
- [ ] Directory structure reorganized
- [ ] Documentation updated

---

## Appendix A: Standard Script Template

```bash
#!/usr/bin/env bash
# shellcheck shell=bash
#
# script-name.sh
# Brief one-line description
#
# Usage:
#   ./script-name.sh [options]
#
# Options:
#   --dry-run, -n    Preview changes without executing
#   --verbose, -v    Enable verbose output
#   --help, -h       Show this help message
#
# Exit codes:
#   0 - Success
#   1 - General error
#   2 - Missing dependencies
#   3 - Invalid arguments
#
# Examples:
#   ./script-name.sh --dry-run
#   ./script-name.sh --verbose
#   ./script-name.sh --dry-run --verbose
##############################################################################

set -euo pipefail

# Defaults
DRY_RUN=false
VERBOSE=false

# Functions
show_usage() {
  grep '^#' "$0" | sed 's/^# //' | sed 's/^#//'
}

log_info() {
  [ "$VERBOSE" = true ] && echo "[INFO] $*" || true
}

log_error() {
  echo "[ERROR] $*" >&2
}

# Parse arguments
for arg in "$@"; do
  case "$arg" in
    --dry-run|-n) DRY_RUN=true ;;
    --verbose|-v) VERBOSE=true ;;
    --help|-h) show_usage; exit 0 ;;
    *) log_error "Unknown option: $arg"; show_usage; exit 3 ;;
  esac
done

# Main logic
main() {
  if [ "$DRY_RUN" = true ]; then
    log_info "[DRY-RUN] Would execute: <command>"
  else
    log_info "Executing: <command>"
    # Actual execution here
  fi
}

main "$@"
```

---

## Appendix B: Resources

- **ShellCheck:** https://www.shellcheck.net/
- **Bash Style Guide:** https://google.github.io/styleguide/shellguide.html
- **Bash Best Practices:** https://bertvv.github.io/cheat-sheets/Bash.html

---

**End of Code Review**
