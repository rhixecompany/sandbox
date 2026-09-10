---
name: run-all-goals-five-day
title: "Run All Goals Five-Day Consolidation"
description: "Use when consolidating a fixed five-day default-profile session corpus into local specs, plans, prompts, and verified execution results."
version: 1.0.0
author: Alexa
license: MIT
tags: [consolidation, sessions, plans, specs, verification]
---

# Run All Goals Five-Day Consolidation

## Skills Required

| Skill | Purpose |
|---|---|
| `using-superpowers` | Workflow and safety gates |
| `plans-and-specs` | Linked requirements and plan decomposition |
| `executing-plans` | Sequential execution with checkpoints |
| `executing-prompt-workflows` | Run prompt phases against real files |
| `verification-before-completion` | Fresh evidence before completion claims |

## Workflow

### Phase 1 — Freeze evidence

Run the session-window auditor against default `state.db`, then summarize the corpus. Do not create implementation artifacts until the corpus exists and its window/scope fields match the request.

### Phase 2 — Inventory artifacts

Enumerate specs, plans, prompts, scripts, skills, templates, references, approvals, tests, and results under the clarified workspace roots. Classify stale historical outputs separately from live artifacts.

### Phase 3 — Create linked artifacts

Create the consolidated spec, implementation plan, executable prompt, verifier, and result template. Link spec↔plan bidirectionally. Keep all executable code in `scripts/`.

### Phase 4 — Verify and execute

Parse generated JSON/YAML/Markdown, resolve references, run local verification, and write fresh results. Stop on gate failure and preserve exact evidence.

### Phase 5 — Close

Attempt session-end capture using a verified local mechanism. Report unavailable capture paths explicitly; never synthesize a session ID.

## Guardrails

- Default-profile sessions only; never scan other profile databases.
- Redact credentials from excerpts.
- Never read or copy `.env` values.
- No commits, pushes, provider probes, or remote writes.
- Historical “complete” messages are not proof of current state.
- Use Git/local rollback; do not create backup artifacts.

## Verification Checklist

- [ ] Fixed WAT window is recorded
- [ ] Default `state.db` is the only database source
- [ ] Session count and evidence summary are fresh
- [ ] Spec and plan are linked both ways
- [ ] Prompt references resolve
- [ ] Scripts compile and run
- [ ] Existing run-all-goals checks pass or blocker is recorded
- [ ] Final result exists on disk
- [ ] Session-end capture was attempted

## References

- `.hermes/specs/run-all-goals-five-day-consolidated-spec.md`
- `.hermes/plans/run-all-goals-five-day-consolidated-plan.md`
- `scripts/audit_default_sessions_window.py`
- `scripts/summarize_run_all_goals_corpus.py`
- `scripts/verify_run_all_goals_five_day.py`
