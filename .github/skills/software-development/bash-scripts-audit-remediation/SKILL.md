---
name: bash-scripts-audit-remediation
title: Bash Scripts Audit Remediation
description: Five-phase script audit and remediation workflow for Bash, PowerShell, BAT, and TypeScript scripts across repos. Inventories, audits, plans, fixes, and verifies.
---

# Bash Scripts Audit & Remediation

> Use when you need to audit, fix, and verify custom scripts (`.sh`, `.ps1`, `.bat`, `.ts`) across one or more repositories. Follows a 5-phase pipeline: inventory → audit → plan → implement → verify.

## Context

This skill was born from a multi-repo script cleanup spanning 231 scripts across 6 path groups with 23 issues. The workflow handles batch processing (7 files per batch), cross-referencing between parallel script variants, and systematic verification.

**Recent updates** (from Batch 1–4b execution):
- Added `references/wrapper-orchestration-contract.md` — comprehensive platform-specific patterns for thin wrappers and business-logic bug detection
- Added `references/batch-remediation-checkpoint-workflow.md` — batch execution workflow, checkpoint verification, and append-only progress logging
- Added `references/typescript-consolidation-utilities.md` — utility-first pattern, shared orchestrator creation, deferred refactoring for risk mitigation
- Added `references/wrapper-delegation-discovery.md` — discovering canonical runners from package manifests, delegation verification testing, batch sizing for wrapper families, before/after metrics
- Added `references/cross-platform-wrapper-standardization.md` — **NEW** matching .sh and .ps1 wrappers, help flag conventions, exit-code propagation patterns, cross-platform parity testing
- Enhanced Phase 4 guidance with per-batch workflow details, wrapper-family batching strategy (group by purpose, not platform), canonical runner discovery pattern, and delegation verification steps
- Updated verification checklist to include wrapper size reduction metrics (expect ≤40 lines, 70–85% reduction for business-logic wrappers, 13% for orchestrator families)
- **Batch 1–4 complete**: 20 wrapper files normalized across Bash, Banking, and Comicwise; ~850 lines reduced; proven thin orchestrator pattern across platforms

Target paths pattern: `repo/scripts/**`, `repo/**`, `project/scripts/**`

## Extended 6-Phase Migration Pattern

When migrating 20+ scripts from multiple source locations to a centralized target directory, use the **extended 6-phase pattern** (Phases 1-6 instead of the default 5-phase audit-and-remediation model). This adds explicit Code Review (Phase 3) and Cleanup (Phase 6) phases with detailed safety gates and parity verification before deletion.

**Key advantages:**
- Explicit separation: planning → audit → code-review → migration → test → cleanup
- Parity verification before deletion (prevents data loss)
- Git-tagged checkpoints at critical transitions
- 18-point cleanup checklist for stale-reference verification
- Batch-independent execution (scale from 20 to 200+ scripts)

**References:**
- `references/six-phase-migration-specifications.md` — **Complete 6-phase specification** with detailed phase workflows, deliverables, timing, and metrics from a real 54-script migration project. Use this as the primary reference when executing large-scale migrations.
- `references/six-phase-migration-with-safety-gates.md` — Safety gate patterns and rollback procedures for phase transitions.

## Phases

### Phase 1: Inventory & Catalog

**Goal:** Discover and catalog all custom scripts.

```bash
# Search patterns for each script type
find Bash/ -name "*.sh" -not -path "*/node_modules/*" -not -path "*/.git/*" | sort
find . -name "*.ps1" -not -path "*/node_modules/*" | sort
find . -name "*.bat" -not -path "*/node_modules/*" | sort
find . -name "*.ts" -not -path "*/node_modules/*" -path "*/scripts/*" | sort
```

**Output:** `docs/<context>-scripts-list-context.md` with file counts, types, line counts, and purposes.

### Phase 2: Batch Audit

**Goal:** Read files in batches of 7 and identify issues.

| Category | What To Check |
|----------|---------------|
| **Critical** | Undefined variables, typos in variable names, missing `set -e`, `local` outside functions, unreachable label/branch, ANSI artifacts |
| **High** | Placeholder comments (`Adminbot`, `Description placeholder`), wrong import extensions, callback vs promises, `@type {*}`, hardcoded user paths, missing shellcheck directives |
| **Medium** | `$ErrorActionPreference`, inconsistent shebangs, missing strict mode flags, monolithic scripts, inline Node.js in shell, naming inconsistency |
| **Low** | Hardcoded script arrays, doc redundancy, parallel script drift, duplicate comments, missing pwsh shebangs |
| **Archival** | One-shot migration artifacts (skills-commit-batch-*), generated scaffolding scripts, temporary test scripts that outlived their purpose |

**One-shot artifact detection** (new pattern):

When auditing, watch for large families of numbered scripts with similar names (e.g., `skills-commit-batch-{1-26}.sh`, `skills-commit-batch-{1-25}.ps1`). These are often one-shot migration artifacts generated by batch-processing tools. Signals:
- Sequential numbering (batch-1 through batch-N)
- Same content structure with only file paths differing
- No current references from package.json, Makefile, or README
- Clearly tied to a past migration project

**Fix for one-shot artifacts:** Archive rather than delete. See Phase 4 for the archive pattern.

**Priority 1 Safety Audit** (when CRITICAL patterns detected):

Before proceeding to Phase 3, perform manual context-dependent review of scripts flagged as CRITICAL. Many "dangerous" patterns are safe in context (trap cleanup, lock file removal, dry-run defaults). See `references/priority-1-safety-audit.md` for audit workflow, safe vs dangerous pattern classification, and scale-aware triage strategy.

**Output:** `docs/<context>-scripts-issues-context.md` + Priority 1 audit verdicts (SAFE/BLOCKED with rationale)

### Phase 3: Plan

Create `docs/<context>.prompt.md` with:
- Fix strategy (critical -> high -> medium -> low)
- Batches of exactly 7 files per batch
- Each fix includes: file path, line, current text, replacement text, and verification step
- Rollback instructions per batch

**Shared library planning** (when consolidating multiple scripts into TypeScript):

Before creating individual TS implementations, plan a shared `src/lib/` directory with common utilities that all implementations will import:
- `colors.ts` — Terminal color output with TTY/NO_COLOR detection
- `logging.ts` — Log levels, timestamps, file logger
- `errors.ts` — Error types (ScriptError, UsageError) and safeExec wrapper
- `cli.ts` — CLI argument parsing and help display

This is the **utility-first** pattern: create the shared infrastructure FIRST, then build each TS implementation importing from it. See `references/typescript-consolidation-utilities.md` for the detailed pattern.

**npm script registration**: When creating TypeScript implementations, plan corresponding `package.json` script entries:
- `clean:cache`, `clean:cache:dry` for cache-clean
- `clean:deps`, `clean:deps:dry` for dependency cleanup
- `upgrade`, `upgrade:debug` for package upgrade
- `commit:batches` for git batch commits
- Include both normal and dry-run variants where appropriate

### Phase 4: Implement (Batched & Verified)

Apply fixes using `patch()` or `write_file()` (NOT sed/awk). Execute in batches of exactly 7 files, with checkpoint verification after each batch.

**Utility-first consolidation pattern** (critical for multi-batch TypeScript/orchestrator work):

When consolidating duplicated logic across multiple runners or wrappers:
1. **Create reusable utilities FIRST** — extract common patterns into new shared modules (e.g., `orchestrator-spawn.ts`)
2. **Verify utility interface** — ensure the new utility solves the consolidation problem before applying it widely
3. **Document deferred refactoring** — record which existing runners should migrate to the new utility, and defer active refactoring to a later checkpoint
4. **Defer high-risk refactoring** — don't refactor all consumers immediately; prioritize creation, verification, then staged migration

This minimizes risk during wrapper stabilization phases. See `references/typescript-consolidation-utilities.md` for patterns and examples.

**Per-batch workflow** (see `references/batch-remediation-checkpoint-workflow.md` for full details):

1. **Select batch scope** — choose ≤7 files grouped by logical unit (e.g., all variants of a wrapper family)
   - **Wrapper family batching**: When normalizing cross-platform wrappers (e.g., `dev.sh`, `dev.ps1`, `dev.bat`), group by script purpose rather than platform count. E.g., if you have 10 root-level launchers (5 scripts × 2 platforms), split into batches by purpose: Batch 4a handles dev + setup-dev (4 files), Batch 4b handles quality-gate + cleanup + install-extensions (6 files). This keeps related functionality together and makes verification easier.
2. **Read & analyze** — understand current patterns, detect bugs, identify canonical implementations
   - **Canonical runner discovery**: Before converting wrappers, check package.json (or Makefile/config) to identify what command each wrapper should delegate to. See `references/wrapper-delegation-discovery.md` for patterns and tools.
3. **Implement** — apply changes with `patch()` or `write_file()`
4. **Verify checkpoint** — run syntax checks, execution tests, exit-code propagation, argument pass-through
   - **Wrapper delegation testing**: After converting a wrapper family, test help output, argument forwarding, and exit code propagation against the canonical runner. Record before/after line counts to measure business-logic reduction. See `references/wrapper-delegation-discovery.md` for testing patterns.
5. **Update artifacts** — append entries to progress log and verification report (append-only, never overwrite)
6. **Review & proceed** — confirm checkpoint passed before moving to next batch

**Wrapper normalization** (see `references/wrapper-orchestration-contract.md` for platform-specific patterns):

When normalizing a wrapper family, all platform variants (`.sh`, `.ps1`, `.bat`) must follow the same contract:
- Accept all arguments from caller
- Forward all arguments to TypeScript runner unchanged
- Propagate exit code back to caller
- Keep no business logic — orchestration only
- Detect and fix: thin wrappers hiding business logic (loops, conditionals, test runners, flag handling)

**Bulk operations**: For large-scale edits across 10+ files (e.g. adding Set-StrictMode to 41 .ps1 files), use a PowerShell script via `terminal()` to apply the change programmatically. Call `powershell -NoProfile -Command` and iterate the file list with `Get-Content`/`Set-Content`. Use regex patterns to find the insertion point (after `param()` block, after `<#...#>`, after `#` comments).

For background on specific fix patterns, see:
- `references/bash-common-pitfall-fixes.md` — subshell, eval, $?, and unbound var fixes
- `references/bash-heredoc-quoting-pitfalls.md` — heredoc quoting, `write_file` alternative, MSYS-specific issues
- `references/powershell-strict-mode-and-deprecations.md` — Set-StrictMode and PSIsContainer
- `references/bat-thin-delegator-pattern.md` — .bat to .ps1 delegator pattern
- `references/wrapper-orchestration-contract.md` — thin wrapper patterns and business-logic bug detection
- `references/batch-remediation-checkpoint-workflow.md` — batch execution, verification checkpoints, and append-only logging
- `references/wrapper-delegation-discovery.md` — discovering canonical runners from package manifests, delegation testing, batch sizing for wrapper families
- `references/cross-platform-wrapper-standardization.md` — matched .sh/.ps1 pairs, help flag conventions, exit-code propagation, parity testing
- `references/typescript-consolidation-utilities.md` — utility-first pattern, shared orchestrator creation, staged migration strategy
- `references/typescript-migration-architecture.md` — **Complete TypeScript migration framework:** AST transformations (ts-morph), dry-run executor, behavior testing, orchestrator pattern, safety protocols, migration utilities, and lessons learned from 290+ script modernization project
- `references/common-bash-pre-existing-bugs.md` — Three pre-existing bug patterns found via `bash -n` during 54-script migration: case-statement parse failure, missing `fi`, and double-quote escaping conflicts in grep patterns. Includes fix patterns and detection workflow.
- `references/bash-json-and-float-pitfalls.md` — JSON Lines format pitfalls (`jq -c`), float comparison in bash (`awk` vs `bc + (( ))`), and env var passing in pipelines.

**Key patterns to implement:**
- Add `# shellcheck shell=bash` after shebang on all `.sh` files
- Standardize shebangs to `#!/usr/bin/env bash`
- Add `set -euo pipefail` to all shell scripts (fix bare `set -e` or `set -uo pipefail`)
- Add `#!/usr/bin/env pwsh` to PowerShell scripts
- Add `Set-StrictMode -Version Latest` to all `.ps1` files (the PS equivalent of `set -euo pipefail`). Skip `skills-commit-batch-*.ps1` — they're git command lists, not real PS scripts.
- Replace `$_.PSIsContainer` with `-File`/`-Directory` switches (deprecated in PS 7.4+)
- Replace `C:\\Users\\<user>\\Desktop\\SandBox` with `$HOME/Desktop/SandBox` or `$env:USERPROFILE`
- Replace placeholder comments (`@author Adminbot` -> `@author <user>`, `Description placeholder` -> meaningful description)
- Convert callback `fs.readFile` patterns to `fs.promises`
- Add `.js` extension to TypeScript imports from sibling files
- Add `Select-Object -Unique` to deduplicate arrays in PowerShell

**Shell-specific fixes (see `references/bash-common-pitfall-fixes.md`):**
- Replace `find | while` subshells with `while ... done < <(find ...)` — preserves variable assignments
- Replace `eval "$cmd"` with `bash -c "$cmd"` — eliminates injection risk
- Fix `$?` after `command &` — `$?` checks launch success, not command result
- Fix unbound vars with `${VAR:-}` safe defaults for `set -u` compliance

**BAT remediation (see `references/bat-thin-delegator-pattern.md`):**
- Replace monolithic `.bat` with thin delegator to `.ps1` counterpart
- Keep fallback for systems without PowerShell

### Phase 5: Verify

Run systematic verification:

```bash
# 1. Shellcheck all modified .sh files
shellcheck -f gcc Bash/*.sh Bash/scripts/*.sh 2>&1

# 2. Check for remaining placeholder patterns
grep -r "Adminbot\|Description placeholder\|CreatedBy: convert-scripts" --include="*.ts" --include="*.ps1" --include="*.sh" ./

# 3. Verify specific fixes
grep -c 'CRITICAL_REPOS_REPOS' Bash/scripts/phase-1-deep-triage.sh  # should be 0
grep 'set -euo pipefail' Rhixe-company/comicwise/quality-gate.sh    # should exist
grep 'shellcheck shell=bash' Bash/clean_dependency_folders.sh       # should exist

# 4. Verify install module structure
ls install/lib/ 2>/dev/null | wc -l  # should be 9 modules

# 5. Verify cross-ref tools exist
ls Bash/scripts/phase-6-cross-ref.* 2>/dev/null | wc -l  # should be 2
```

## Rules

1. **Process in batches of exactly 7** when auditing and applying fixes.
2. **Use `patch()` for all edits** -- never sed/awk for file changes.
3. **Bash/PowerShell/BAT = orchestrators only** -- core logic goes into TypeScript scripts.
4. **Include code samples, file references, and diffs** in the remediation plan.
5. **Remove dead code** during consolidation and deduplication.
**6. Index-doc staleness**: When an index file (e.g., `RESEARCH_INDEX.md`) claims subsidiary files exist but they don't on disk, the index is stale. Always verify index claims with `find` before trusting them. Regenerate or update the index after file creation/deletion. A stale index is worse than no index — it creates false confidence.
7. **Bump `$ErrorActionPreference` to `"Stop"`** on PowerShell scripts that use color output.

## Pitfalls

- **Migration scripts create nested `<target>/<target>/` directories**: When migration scripts live inside the target directory (e.g., `Bash/migrate-script.sh`) and you run them from a parent directory, their output paths may create artifacts at `Bash/Bash/somefile` instead of `Bash/somefile`. Always run migration scripts from the target directory itself (`cd Bash && bash migrate-script.sh`), or verify the output lands in the right place.
- **Fix → re-copy timing**: When fixing scripts after copying to target, fix the ORIGINALS first, then re-copy to target. Copying then fixing leaves the target copies stale. Run `bash -n` on BOTH before declaring clean.
- **Pre-existing bugs surface during migration**: Running `bash -n` on migrated copies for the first time often reveals pre-existing syntax bugs that were latent in the originals. Always verify originals are also buggy before fixing — if only the copy is broken, something went wrong during copy. See `references/common-bash-pre-existing-bugs.md` for the three common patterns found during a 54-script migration and their fixes.
- **CRITICAL_REPOS_REPOS**: Double variable name reference is a common typo that silently skips all loop iterations
- **Clean-DependencyFolders name** may exist as PascalCase or kebab-case on disk -- check both
- **`local` outside function** in bash is a syntax error in some contexts but may silently fail
- **`.bat` label ordering**: all subroutine labels must appear BEFORE `:main` or they're unreachable
- **`[0A]`/`[0B]`/`[0C]` ANSI codes** in batch files are artifacts from terminal recording
- **Business logic hiding in thin wrappers**: Shell or PowerShell wrappers sometimes run test suites, build steps, or verification logic instead of delegating to a TypeScript runner. Red flags: 50+ lines, loops/conditionals, runs external commands like `bun run type-check`, handles flags like `--dry-run` locally. Fix: convert to thin wrapper and move logic to TypeScript runner. See `references/wrapper-orchestration-contract.md` for detection rules.
- **`set -u` breaks with empty arrays** -- add safe defaults: use `${VAR:-}` for safe defaults
- **PowerShell `Write-Host` vs `Write-Output`** -- use `-ForegroundColor` parameter instead of ANSI escapes where possible
- **`skills-commit-batch-*.ps1` are git command lists** not real PowerShell scripts. Skip Add-StrictMode and PSIsContainer fixes for these.
- **Backslash paths in .sh files** on Windows/MSYS work but are not portable. Normalize to forward slashes: `git add 'path/to/file'` not `git add 'path\\\\to\\\\file'`
- **Heredoc quoting**: Unquoted heredocs (`<< EOF`) expand `$(...)` and `$vars` in the parent shell before writing to the file, causing empty variables and premature execution. Always use single-quoted delimiters (`<< 'EOF'`) when the script body contains `$` constructs. For complex dynamic scripts, prefer `write_file` entirely. See `references/bash-heredoc-quoting-pitfalls.md`.
- **Context-dependent risk assessment**: Automated pattern matching flags many SAFE scripts as CRITICAL (trap cleanup, lock files, dry-run defaults). Always perform manual review before blocking migration. See `references/priority-1-safety-audit.md` for audit workflow and safe pattern classification. At scale (11K+ scripts), use risk-based triage: Priority 1 (manual audit 4-5 CRITICAL), Priority 2-4 (automated fix), Archive (tag for deletion, defer audit).
- **TS compilation can break after migration when tsconfig has strict flags**: Common post-migration TS errors and fixes:
  - `process.env.X` → `process.env["X"]` when `noUncheckedIndexedAccess` is enabled
  - `tsConfigFilePath: undefined` fails with `exactOptionalPropertyTypes` — omit the property or use `as any`
  - `import { X } from "foo"` when `X` is a type → `import type { X } from "foo"` (verbatimModuleSyntax)
  - `import X from "./module"` → `import X from "./module.js"` (moduleResolution node16/nodenext requires extensions)
  - `arr[i]` returns `T | undefined` with `noUncheckedIndexedAccess` → use `arr[i]!` when index is known valid
  - `Bun.spawn` type: `SpawnOptions.OptionsObject` requires 3 type args — remove the type annotation and let inference work, or use `as any`
  - `this.opts.cwd: string | undefined` in Bun.spawn opts fails with `exactOptionalPropertyTypes` — use `cwd: this.opts.cwd ?? process.cwd()` instead of passing bare `cwd`
  - `import { SpawnOptions }` → `import type { SpawnOptions }` when `verbatimModuleSyntax` is enabled and it's a type-only import — otherwise you get TS1484
  - **Stale nested copies in build output cause phantom errors**: After running migration scripts inside the target directory, run `find . -type d -path '*/<target>/<target>'` (e.g., `find Bash/ -type d -path '*/Bash/Bash'`) to catch stale artifacts that `tsc` resolves through nested tsconfig.json files. Delete before running typecheck or the errors compound.
- **6-phase execution for large migrations (MANDATORY at 20+ scripts)**: When moving 20+ scripts across multiple source locations, **always extend to 6-phase model** (add explicit Code Review phase 3, Cleanup phase 6 with 18-point checklist). This forces parity verification before deletion and prevents data loss. At 54+ scripts, the 6-phase pattern becomes critical for safety and auditability. See `references/six-phase-migration-specifications.md` (primary reference with real 54-script example) and `references/six-phase-migration-with-safety-gates.md` (safety gates & rollback patterns). TL;DR: Catalog → Plan → Review → Migrate (with parity checks) → Test → Cleanup (with git tags).

## When to Use

- When performing bash scripts audit remediation operations or tasks
- When managing bash scripts audit remediation infrastructure or configurations
- When automating or debugging bash scripts audit remediation workflows
- **Triggers**: "set up software-development/bash-scripts-audit-remediation", "configure bash scripts audit remediation", "debug bash scripts audit remediation issue"

## Overview

Bash Scripts Audit Remediation is a skill for handling bash scripts audit remediation tasks and automation workflows. Use this skill when you need to perform bash scripts audit remediation operations efficiently.

## Verification Checklist

After implementation, confirm:
- [ ] `bun run typecheck` (or `tsc --noEmit`) passes with 0 errors when TypeScript files were modified
- [ ] Shellcheck: 0 errors on all modified `.sh` files
- [ ] `bash -n` syntax check: 0 errors on ALL migrated `.sh` files (catches pre-existing bugs early)
- [ ] PowerShell files parse with AST parser (zero syntax errors)
- [ ] Wrapper size reduction: thin wrappers ≤40 lines (expect 70–85% reduction from business-logic originals)
- [ ] No `Adminbot`/`Description placeholder`/`CreatedBy: convert-scripts` remain in TypeScript
- [ ] All `.sh` files have `# shellcheck shell=bash` after shebang
- [ ] All `.sh` files use `#!/usr/bin/env bash`
- [ ] All `.sh` files have `set -euo pipefail` (not just `set -e` or `set -uo pipefail`)
- [ ] All `.ps1` files have `Set-StrictMode -Version Latest` (excluding `skills-commit-batch-*`)
- [ ] No `$_.PSIsContainer` references remain in `.ps1` files
- [ ] No `find | while` subshell patterns in `.sh` files
- [ ] No `eval "$cmd"` in `.sh` files (use `bash -c` instead)
- [ ] No `$?` checked after `command &` (background launch)
- [ ] Key PS1 files have `#!/usr/bin/env pwsh`
- [ ] `install.sh` refactored to <=250 lines with modules under `install/lib/`
- [ ] Log rotation present in cleanup scripts
- [ ] Cross-reference scripts exist (both `.sh` and `.ps1`)
- [ ] Naming convention documented at `docs/NAMING_CONVENTION.md`
- [ ] Root `.gitignore` has `Bash/logs/` entry

