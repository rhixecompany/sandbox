---
name: debug-subgoal-spec
version: 1.0.0
status: in-progress
---

# Spec — Systematic Debug Subgoal Evidence + Fix/Verify

> Per `systematic-debugging`: Phase 1 (reproduce/evidence) before ANY fix. Per `user-communication-preferences`: concise, direct, action-first, no filler, DRY (no duplication with plan file — this is the spec, plan is the execution blueprint). Per `SOUL.md`: honest blocker reporting; no synthetic session IDs; never synthetic capabilities or rankings; `.env` untouched.

## Source Commands (User-Provided — Executed Sequentially, Not Invented)

Batch 1 — MCP test + check:
`hermes mcp test doist/todoist-ai`
`hermes mcp test io.github.basicmachines-co/basic-memory`
`bun run check`

Batch 2 — Doctor chain:
`hermes doctor`
`hermes doctor --fix`
`hermes security audit`
`hermes status`
`hermes insights`

Batch 3 — Logs inspection:
`hermes logs list`
`hermes logs errors`
`hermes logs desktop`
`hermes logs gateway`
`hermes logs gui`
`hermes logs agent`

## Evidence Requirements (Real Only)

- Each command's REAL stdout/stderr/exit code must be captured in `./plans/debug-run-logs.md`.
- No fabricated `hermes` output. If `hermes` binary is unavailable or a subcommand (e.g., `hermes mcp test doist/todoist-ai`) doesn't exist, the real error (`command not found`, `unknown server`, `exit 1`) is logged.
- No synthetic `session_id` or synthetic `user-communication-preferences` capability claims inserted into logs.

## Deliverables

- `./plans/debug-subgoal-plan-2026-09-13.md` (plan)
- `./plans/debug-run-logs.md` (real command outputs — sequential batches)
- `./specs/debug-analysis-2026-09-13.md` (analysis of real evidence)
- `./plans/` (any minimal fixes applied with verification)
- `./specs/debug-subgoal-final-verification.md` (final gate)

## Constraints
- `systematic-debugging` Phase 1 gate: NO fix applied until evidence confirms root cause.
- `systematic-debugging` Phase 2 gate: ONE hypothesis per failure; no multi-change batches.
- `systematic-debugging` Phase 4 gate: 3 failed fixes → STOP and question architecture (per `multi-file-change-protocol` gate discipline); document architectural concern if it occurs.
