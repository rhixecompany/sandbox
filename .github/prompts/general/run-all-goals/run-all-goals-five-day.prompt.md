---
name: run-all-goals-five-day
title: "Run All Goals — Five-Day Local Consolidation"
description: "Inventory, consolidate, verify, and execute the Sep 6–10 default-profile session-derived workflow locally."
version: 1.0.0
author: Alexa
license: MIT
tags: [run-all-goals, consolidation, sessions, local-only, verification]
trigger: /run-all-goals-five-day
category: general
toolsets: [terminal, filesystem, session_search]
skills: [using-superpowers, user-communication-preferences, plans-and-specs, executing-plans, executing-prompt-workflows]
references:
  - ../../../../.hermes/specs/run-all-goals-five-day-consolidated-spec.md
  - ../../../../.hermes/plans/run-all-goals-five-day-consolidated-plan.md
---

# Goal

Create a reproducible local evidence package from all default-profile sessions in Sep 6–10, 2026 WAT, then verify and execute the package without external side effects.

## Context

- Workspace: `C:/Users/Alexa/Desktop/SandBox`
- Session DB: `C:/Users/Alexa/AppData/Local/hermes/state.db`
- Window: `[2026-09-06T00:00:00+01:00, 2026-09-11T00:00:00+01:00)`
- Scope: local repository/Hermes filesystem and tests only

## Rules

- Read and verify sources before creating or executing artifacts.
- Do not read or print `.env`, tokens, credentials, or raw secret-bearing files.
- Do not commit, push, sync externally, probe live providers, or mutate global profile state.
- Treat historical completion text as evidence to verify, not as live truth.
- Keep scripts under `scripts/` and use native Windows paths for native tools.
- Stop on a failed gate; record the command and evidence.

## Phases

### Phase 1 — Corpus

1. Run `python scripts/audit_default_sessions_window.py --start 2026-09-06 --end 2026-09-11`.
2. Run `python scripts/summarize_run_all_goals_corpus.py`.
3. Confirm the corpus declares the default root `state.db` and expected WAT window.

**Gate:** Corpus and summary exist and parse.

### Phase 2 — Artifact inventory

1. Enumerate `.hermes/specs/`, `.hermes/plans/`, and this prompt package.
2. Resolve all links from the consolidated spec and plan.
3. Mark missing/stale references without fabricating replacements.

**Gate:** Inventory output exists and every required path is classified.

### Phase 3 — Verification

1. Run `python .github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py`.
2. Run the existing run-all-goals verifier and test scripts.
3. Check JSON/YAML/Markdown structure.

**Gate:** All local checks pass or a blocker is written to results.

### Phase 4 — Execute

1. Re-run the corpus and summary scripts.
2. Run the deterministic local verification suite.
3. Write `results/five-day-execution-result.md` with command outputs, counts, and blockers.

**Gate:** Result exists and contains fresh evidence.

### Phase 5 — End capture

1. Locate the installed session-end capture mechanism.
2. Run it only if its invocation is known and local-only.
3. Record the result path or explicit unavailable blocker.

**Gate:** End capture attempted and reported.

## Outputs

- `.hermes/plans/run-all-goals-five-day-session-corpus.json`
- `.hermes/plans/run-all-goals-five-day-session-summary.json`
- `.hermes/specs/run-all-goals-five-day-consolidated-spec.md`
- `.hermes/plans/run-all-goals-five-day-consolidated-plan.md`
- `.github/prompts/general/run-all-goals/run-all-goals-five-day.prompt.md`
- `.github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py`
- `.github/prompts/general/run-all-goals/skills/run-all-goals-five-day.md`
- `.github/prompts/general/run-all-goals/results/five-day-execution-result.md`

## Verification

A run is complete only when every named output exists, every referenced path is classified, and the result file records fresh local command evidence.
