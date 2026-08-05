# Disk Space Cleanup Plan

**Date:** 2026-08-04
**Status:** Executed
**Goal:** Free disk on `C:` (was 97-98% full) by safely deleting unused/stale venvs, node_modules, caches, `.archive`, backups, temp/logs across SandBox repos, subrepos, hermes root, and hermes-profiles mirror — then verify disk space.

## Before State

- `C:` = 5.5 GB free / 236.8 GB (97-98% used)
- Biggest sandbox dirs: `projects/` 4.9 GB (mostly `comicwise/.git` 3.9 GB), root `node_modules` 85 MB, `hermes-profiles/` 120 MB

## Required Artifacts (all written to disk)

| Artifact | Path                                                               | Status               |
| -------- | ------------------------------------------------------------------ | -------------------- |
| Script   | `scripts/cleanup_disk.py`                                          | ✅ created + lint-ok |
| Skill    | `~/AppData/Local/hermes/skills/devops/disk-space-cleanup/SKILL.md` | ✅ created           |
| Plan     | `plans/2026-08-04_disk-space-cleanup-plan.md`                      | ✅ this file         |
| Spec     | `plans/2026-08-04_disk-space-cleanup-spec.md`                      | ✅ created           |
| Prompt   | `.github/prompts/disk-space-cleanup.prompt.md`                     | ✅ created           |

## Execution Sequence (validated step-by-step)

1. **Dry-run scan** (SandBox repos + subrepos + hermes-profiles): 4 items, 404.6 MB
   - `projects/rhixecompany-comics/frontend/node_modules` 279.1 MB
   - root `node_modules` 54.2 MB
   - `projects/mcp-servers/typescript/node_modules` 42.7 MB
   - `projects/mcp-servers/copilot-studio/node_modules` 28.6 MB
2. **Approval** obtained (full sweep).
3. **Apply deps sweep** → freed 404.6 MB.
4. **Hermes root safe cleanup** (cats `cache,logs,archive`): 93 items freed, 12.7 MB; 1 locked file `mcp-stderr.log` skipped (in use).
5. **OS caches**: pip/npm/bun caches absent; `Temp` cleared of aged (>3d) entries + empty dirs.
6. **git gc** on `projects/comicwise` (found `size-garbage 1.54 GiB`): `.git` 3.9 GB → 18 MB.

## After State

- `C:` = **14 GB free** (was 5.5 GB) → **~8.5 GB reclaimed**, 95% used

## Remaining / Open Items

- App uninstall: inventory taken, deletion list pending user approval (DO NOT uninstall without approval).
- Git Bash ASLR (ForceRelocateImages) fix: needs elevated shell; user to confirm.
- `git filter-repo` to purge large blobs from deeper history — NOT run (history-rewriting, needs explicit approval).
