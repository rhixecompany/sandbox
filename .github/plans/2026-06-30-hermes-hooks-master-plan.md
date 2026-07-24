---
status: completed
---

# Hermes Hooks Master Plan

## Purpose

Consolidate the overlapping hooks planning fragments into one executable plan before any destructive or config-changing work.

## Source Plans

- `.hermes/plans/2026-06-30-174800-hermes-hooks-discovery-summary.md`
- `.hermes/plans/2026-06-30-180000-hermes-hooks-continue.md`

## Verified Current State

- `docs/hermes-hooks-summary.md` exists.
- `hermes hooks list` shows no configured shell hooks.
- `hermes hooks --help` exposes `list|test|revoke|remove|doctor` only; no config registration subcommand.
- Live hook families discovered under `~/AppData/Local/hermes/hooks/`:
  - `session-logger`
  - `session-auto-commit`
  - `governance-audit`
  - `docs-cleanup-verify.sh`
- Approval file exists: `.hermes/approvals/2026-06-30-hermes-hooks-unconfigure.md`

## Current Constraints

- Hook registration/configuration must be done through Hermes config editing, not `hermes hooks` CLI.
- Need to keep secrets untouched; only structural config and hook files are in scope.
- Renewed unconfigure approval was recorded on 2026-07-09 at `.hermes/approvals/2026-07-09-hermes-hooks-unconfigure.md`.

## Execution Plan

1. **Pre-flight gate** — confirm plan, approval, and hook command surface are sufficient.
2. **Revision gate** — unconfigure/remove the approved hook registrations and verify the live list changes.
3. **Revision gate** — delete or replace the obsolete hook scripts/configs in `~/AppData/Local/hermes/hooks/`.
4. **Revision gate** — recreate the approved hook tree with current best practices.
5. **Revision gate** — update Hermes config registration using the supported config path, then verify hooks load cleanly.
6. **Revision gate** — fix related docs/config drift across skills, memories, `SOUL.md`, and `USER.md` only after hook remediation is stable.
7. **Abort gate** — stop immediately on any unsafe config drift, missing command surface, or secret-handling risk.

## Done Criteria

- Hooks are recreated and registered as intended.
- `hermes hooks list` and the relevant hook tests pass.
- Conflicting docs/configs are updated and verified.
- No unapproved secrets or backups were introduced.
---
*Workflow: subagent-driven-development | Two-stage review (spec → quality)*
