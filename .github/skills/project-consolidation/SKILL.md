---
name: project-consolidation
description: Five-phase workflow for cleaning up and restructuring a project. Use when consolidating duplicate scripts, standardizing file layout, and reconciling divergent project structures.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - consolidation
  - project
  - restructuring
  - cleanup
title: Project Consolidation
---

# Project Consolidation

Five-phase workflow for cleaning up and restructuring a project. Handles migration of assets, deduplication, deletion of stale artifacts, and final structural verification.

## Profile Selection

| Task Intensity | Profile |
|----------------|---------|
| General cleanup (safe deletions) | `default` or `alexa` |
| Aggressive cleanup (bulk deletions, deep reorganization) | `alexa` |

## Phases

### Phase 0: Pre-cleanup Snapshot
Before any destructive action, capture current state:
```bash
cd <project-root>
git stash list        # check for stashed changes
git status --short    # baseline
```
- Record the modified/untracked count. This is your reference for verification.
- If the tree is already dirty, note that deletions will appear as ` D` in git status.

### Phase 1: Inventory
Scan the workspace, index all files by type and purpose.
- Use `execute_code` with `pathlib.Path` or `os.scandir` — **avoid `rglob("*")`** on repos with `node_modules` or broken symlinks (Python 3.11+ crashes on broken symlinks; use targeted `iterdir()` with max depth or error-tolerant walk).
- Use `search_files` for content searches (ripgrep-backed, handles broken paths).
- Batch independent scans in a single `execute_code` call.
- Categorize: operational vs stale, reference vs pipeline artifact, source vs generated.

### Phase 2: Cross-reference
Map equivalent files, detect duplicates, identify orphans.
- Check content hashes (MD5) for exact duplicates.
- Check file sizes and timestamps for variant duplicates (same data, different detail level — e.g. judge runs with `batch_0001` vs `batch_00001` zero-padding).
- Search for references to migration targets before moving.
- Use `search_files` across the workspace for paths to migrated assets.

### Phase 3: Planning
Design the canonical layout, plan migrations.
- Write a structured plan as a markdown file in `plan/` or `.hermes/plans/`.
- Each phase must be self-contained with explicit commands and verification steps.
- Order by dependency: migrations first (copy assets), then deletions.
- Estimate disk savings per phase.
- Get user approval before executing destructive phases.
- For "aggressive" cleanup: plan for full directory deletions (not just contents) and batch file deletions.

### Phase 4: Execution
Move/merge/delete files according to plan.
- **Migration pattern**: always COPY first (`cp`), then the source can be bulk-deleted later. Never `mv` across filesystem boundaries (Hermes vs workspace).
- **Windows file locks**: if `rm -rf` fails with "Device or resource busy", fall back to:
  ```bash
  cmd.exe /c "rd /s /q <path>"
  ```
  This happens with directories held open by Windows Explorer or background processes.
- **Batch deletions**: use `rm -f` with multiple file arguments, not a loop. Use glob patterns for groups (e.g. `rm -f batch_0000{1..9}_results.md`).
- **`find -delete` on Windows/MSYS**: times out on broken symlinks. Use `-maxdepth` to limit depth and `-not -path '*/node_modules/*'` to exclude known-bad trees.

### Phase 5: Verification
Validate structure, run tests, verify no breaks.
- Verify every deleted path: `ls <path> 2>&1` should show "No such file or directory".
- Check migrated assets landed: `ls <destination>`.
- Re-run `git status --short` and compare diff count to baseline.
- Check `skills-lock.json` and other dependency manifests are still valid.
- Run the project's test suite if one exists.

## When to use

- Duplicate scripts littered across the workspace
- Divergent project structures between repos
- After a migration that left orphan files
- Before onboarding new team members
- User says "aggressively cleanup" — use the aggressive patterns

## Decision Framework for Keep vs Delete

| Signal | Keep | Delete |
|--------|------|--------|
| Pipeline intermediate artifact (context, fix-issues, verify-context) | ❌ | **Delete** |
| Generator output (architecture blueprints, MCP docs) | **Keep** if actively referenced | Delete if stale |
| One-time audit/remediation report | **Archive or delete** | ❌ |
| Operational script (health check, CI) | **Keep** | ❌ |
| Shallow clone of another repo (`.git/` + docs) | Strip `.git/`, keep content, or delete | Delete if unneeded |
| Debug log from completed pipeline | ❌ | **Delete** |
| Duplicated skill (in `.agents/` + Hermes library) | Keep Hermes version | Delete duplicate |

## Verification

| Phase | Check |
|-------|-------|
| 0 | Baseline git status recorded |
| 1 | All files discovered and categorized; broken-symlink paths handled |
| 2 | Duplicate mapping complete; references checked |
| 3 | Migration plan reviewed and approved |
| 4 | Files migrated/deleted without data loss |
| 5 | Git status compared to baseline, deleted paths verified, manifests intact |

## Pitfalls

- **Windows file locks**: `rm -rf` may fail with "Device or resource busy" on directories held open by Explorer or background processes. Fall back to `cmd.exe /c "rd /s /q <path>"`.
- **Broken symlinks in node_modules**: Python 3.11+ `pathlib.rglob("*")` crashes with `FileNotFoundError` on broken symlinks. Use `os.scandir` with error handling, `search_files` (ripgrep-backed), or `find` with `-maxdepth` and `-not -path '*/node_modules/*'`.
- **`find -delete` timeout**: The `find . -type d -empty -delete` pattern can hang indefinitely on large trees with broken symlinks. Always add `-maxdepth N` and `-not -path '*/node_modules/*' --not -path '*/.git/*'`.
- **Interleaved duplicate runs**: Two pipeline runs may produce files like `batch_0001.md` and `batch_00001.md` — different zero-padding, different sizes, different detail levels. Don't assume they're duplicates; check content hashes and counts.
- **Aggressive ≠ destructive to dependencies**: "Aggressive cleanup" still means preserve `.github/agents/`, `.github/instructions/`, `.github/workflows/`, and the core project config files. Operations take precedence over cleanup.
- **Comprehensive over selective**: When given a choice between targeted and full cleanup (e.g. "all judge results" vs "just batch 1-5"), user prefers the comprehensive pass. Default to full scope unless told otherwise.

## Support Files

- `references/aggressive-cleanup-patterns.md` — concrete code recipes for inventory, duplicate detection, batch deletion, Windows lock fallback, find patterns, and the category keep/delete matrix from an actual 10-phase aggressive cleanup.
- `references/plan-migration-pattern.md` — rules for locating and migrating implementation plans into `.hermes/plans/`.

## Verification Checklist

- [ ] Baseline git status recorded before destructive work
- [ ] All files discovered (broken-symlink paths handled)
- [ ] Duplicate mapping complete; cross-references checked
- [ ] Migration plan reviewed and approved by user
- [ ] Migrated assets verified at destination
- [ ] Deleted paths verified gone
- [ ] Dependency manifests valid
- [ ] No empty directories remaining
- [ ] `git status` compared to baseline
- [ ] Plan file updated with completion status
