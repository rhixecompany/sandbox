# executing-plans — Body Reference

Long-form execution guidance lives here. `executing-plans/SKILL.md` is the index; use this file for full phase details, batch rules, patch patterns, and verification procedures.

## Entry Checks

Every major phase includes an entry check:
- Skip completed phases when their artifact or marker exists on disk.
- Never trust plan headers alone; verify live inventory first.
- Re-read source files after edits instead of relying on cached context.

## Inventory Before Execution

Run checks before plan execution:
- `hermes hooks list`
- `hermes plugins list`
- `hermes mcp list`
- `hermes skills audit`
- confirm referenced artifacts exist

Capture outputs under `.hermes/plans/verification/*.txt` when available.

## Batch Execution Rules

- Use batches of <=7 files for file-heavy plans.
- Progress logs are append-only.
- Use artifacts as the source of truth for resume.
- Aggregate results to `.hermes/plans/batch-execution-progress.md`.

## Approval Gates for Destructive Changes

Before destructive steps, create `.hermes/approvals/<timestamp>_<short-title>.md` and wait for recorded approval. Include scope, justification, rollback plan, verification steps, and recorded +1s.

## Patch-First Editing

Prefer `patch` over `write_file`. After any `replace_all=true`, verify whether the original source still exists. If matching text is not unique, add more surrounding context.

## Bulk Sweeps

Use bulk sweeps when the same exact pattern is applied across many files:
- Prefer `execute_code` with Python for reproducibility.
- Use terminal sed only when the affected file list is exact and bounded.
- Verify with targeted search after completion.

## Cross-Platform Notes

- Windows path construction: `%USERPROFILE%` and `C:/Users/...` both acceptable.
- Git Bash wrapper behavior differs from Linux bash; prefer `set -euo pipefail` and `printf` over `echo -e`.
- MSYS path translation can affect pipe behavior; keep paths absolute when crossing subsystems.

## Verification Checklist Baseline

- The final plan includes a dedicated verification phase.
- Disk state is re-read after edits.
- Claims are cross-checked against actual files on disk.
- Verification results are appended to artifacts.
- If late fixes happen, add addenda and re-run targeted checks.
