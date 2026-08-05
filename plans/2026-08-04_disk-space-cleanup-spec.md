# Disk Space Cleanup — Specification

**Version:** 1.0 | **Date:** 2026-08-04 | **Owner:** OWL / Alexa

## 1. Purpose

Safely reclaim disk space on a Windows/MSYS host by deleting ephemeral, reinstallable, or stale artifacts across specified repository roots, the Hermes agent root, and a sync mirror — with a dry-run gate and full audit.

## 2. Scope

**Cleanable categories** (all reinstallable / disposable per user approval):

- `deps` — `node_modules`, `venv`, `.venv`, `myvenv`, `__pycache__`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `.tox`, `.eggs`, `dist`, `build`, `.next`, `.turbo`
- `archive` — `.archive`, `backup`, `backups`, `*.bak`, `*.backup`, `*.orig`, `*.rej`, `*.old`, `*~`
- `cache` — `.cache`, `npm-cache`, `.npm`, plus OS-level pip/npm/bun/Temp caches (opt-in)
- `logs` — `*.log`, logs/ dirs, `*.tmp`, `*.temp`

**Out of scope (never deleted):**

- Any `.git` directory
- Configured root directories themselves (unless `--allow-root-target`)
- Hermes runtime deps (its own `node_modules`/venv — use `--cats cache,logs,archive`)
- Git history rewriting (`filter-repo`/`filter-branch`) without explicit approval

## 3. Functional Requirements

| ID   | Requirement                                                                                |
| ---- | ------------------------------------------------------------------------------------------ |
| FR-1 | Script must run in **dry-run by default**; deletion only with `--apply`.                   |
| FR-2 | Must report per-category items, sizes, and total reclaimable.                              |
| FR-3 | Must record before/after free space (`--verify` / `shutil.disk_usage`).                    |
| FR-4 | Must **dedupe by resolved absolute path** when nested roots are supplied.                  |
| FR-5 | Must **never descend into `.git`** and never delete a configured root by name.             |
| FR-6 | Must support category filtering (`--cats`) so hermes-root runs only touch safe categories. |
| FR-7 | Must write an **audit log** (`results/cleanup_disk.log`) listing every deletion.           |
| FR-8 | Locked/in-use files must be skipped with an error entry, not crash the run.                |
| FR-9 | OS `Temp` must be cleaned **age-based** (not wholesale rmtree) to avoid in-use failures.   |

## 4. Non-Functional Requirements

- NFR-1: Timeout-safe on huge roots (bounded `du`, prune matched dirs in walk).
- NFR-2: Windows/MSYS safe — accepts `C:/...` paths; avoids MSYS `/c/...` pathconv by `MSYS_NO_PATHCONV=1`.
- NFR-3: Reuse existing `disk-cleanup` plugin philosophy (Hermes-home-scoped) rather than duplicate.

## 5. Inputs

Positional roots (paths or `--roots-file`), optionally `--apply`, `--min-size MB`, `--cats`, `--include-os-caches`, `--verify`.

## 6. Acceptance Criteria

- AC-1: `python scripts/cleanup_disk.py --verify <roots>` runs with zero exceptions and lists targets.
- AC-2: `df -h` shows free space increased after `--apply`.
- AC-3: Audit log records each deletion.
- AC-4: No `.git` dir or configured root is ever deleted.
- AC-5: Hermes root run with `--cats cache,logs,archive` does not touch its runtime deps.

## 7. Result (Executed)

Reclaimed **~8.5 GB** on `C:` (5.5 → 14 GB free). Biggest single win: `git gc --prune=now` on `comicwise/.git` (3.9 GB → 18 MB).
