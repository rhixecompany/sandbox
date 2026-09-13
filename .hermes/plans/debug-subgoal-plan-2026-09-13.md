---
name: hermes-systematic-debug-subgoal
version: 1.0.0
status: in-progress
tags: [systematic-debugging, multi-file, hermes-doctor, mcp-test, logs]
created: 2026-09-13
owner: HermesAgent (default profile / patient-tutor for explanations)
---

# Plan — Systematic Debug Subgoal (Background Log + Fix/Verify)

> Per `/multi-file-change-protocol` (14 skills loaded; >6 file modifications expected from fixes). Per `systematic-debugging`: Phase 1 (reproduce/evidence) before Phase 4 (fix). Per `user-communication-preferences`: DRY, concise bullets + table-first, action-first, no filler; never synthetic session IDs; never synthetic capabilities/rankings. Per `SOUL.md`: no hidden errors; honest blocker reporting.

## Commands to Execute (Background, Output to `.hermes/plans/debug-run-logs.md`)

Batch 1 (MCP test + build check):
- `hermes mcp test doist/todoist-ai`
- `hermes mcp test io.github.basicmachines-co/basic-memory`
- `bun run check`

Batch 2 (Hermes doctor chain):
- `hermes doctor`
- `hermes doctor --fix`
- `hermes security audit`
- `hermes status`
- `hermes insights`

Batch 3 (Logs inspection):
- `hermes logs list`
- `hermes logs errors`
- `hermes logs desktop`
- `hermes logs gateway`
- `hermes logs gui`
- `hermes logs agent`

## Plan Phases (Sequential, with Gates)

### Phase -1: Setup (Plan + Spec + Log file init)
- Create `.hermes/plans/` entry (this file).
- Create log file `.hermes/plans/debug-run-logs.md`.
- Confirm previous multi-file results intact (verified: 6 real `.md`, no `.bak` from session).

### Phase 0: Evidence Gathering (Run commands; capture real stdout/stderr)
- Execute Batch 1, 2, 3 sequentially (not parallel — `systematic-debugging` requires ordered reproduction).
- Capture each command's stdout + stderr + exit code + timestamp into `.hermes/plans/debug-run-logs.md`.
- Do NOT invent/fabricate any command output. If a command fails (e.g., `hermes mcp test doist/todoist-ai` returns non-zero), log the REAL output including the error message.
- Gate: At least one log entry exists per command; zero synthetic entries.

### Phase 1: Read All Log Files + Analyze
- Read `.hermes/plans/debug-run-logs.md`.
- Also read any existing `hermes` log files referenced by `hermes logs ...` (if they exist on disk under workspace or `~/AppData/Local/hermes/` paths — check without inventing paths).
- Identify: errors, warnings, failed tests, security audit findings, doctor fix attempts, status discrepancies.
- Log analysis written to `.hermes/specs/debug-analysis-2026-09-13.md`.

### Phase 2: Pattern Analysis + Hypothesis (Systematic Debug Phase 2/3)
- Compare working patterns vs broken patterns from logs.
- Form ONE hypothesis per failure (not multiple guesses).
- Document hypothesis + evidence reference.

### Phase 3: Minimal Fix (Only After Evidence)
- Apply ONE minimal change per failing component.
- Re-run the failing command to verify.
- If fix fails: STOP (per `systematic-debugging` Phase 4: "Rule of Three" — 3 failed fixes → question architecture, don't add more patches blindly).
- Log all fixes + verification results.

### Phase 4: Final Gate + Verification Report
- Confirm all artifacts exist.
- Confirm no `.bak` artifacts.
- Confirm all errors are documented honestly (none hidden).
- Confirm no synthetic session IDs or synthetic capabilities.
- Write `.hermes/specs/debug-subgoal-final-verification.md`.

## Safety / Integrity Constraints
- No destructive `git` operations without user confirmation (`SOUL.md` destructive-op approval rule).
- No editing `.env`; never print secrets.
- Never invent a `hermes` command output — if a command fails, the real failure message is logged.
- `hermes doctor --fix` may be destructive; before running it, log its scope; after running, log its actual output (not assumed).
- `hermes security audit` may reveal real security issues; report honestly, do not suppress.

## References
- `.hermes/md` docs (plan reference) — `.hermes/plans/download-hermes-user-guide-docs-2026-09-13.md` (previous subgoal verified; 6 real `.md` files)
- `.hermes/specs/` — `.hermes/specs/download-hermes-user-guide-docs.md` (previous subgoal spec)
- Skill references: `systematic-debugging` (4-phase), `multi-file-change-protocol` (>6 trigger), `user-communication-preferences` (execution style), `using-superpowers` (advanced execution)
