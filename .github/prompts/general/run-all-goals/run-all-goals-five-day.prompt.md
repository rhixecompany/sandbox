---
name: run-all-goals-five-day
sidebar_position: 16
title: "Run All Goals — Five-Day Consolidation"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
version: 1.0.0
author: Alexa
license: MIT
tags: [prompt, consolidation, sessions, local-only, run-all-goals]
trigger: /run-all-goals-five-day
dependencies:
  - skill:using-superpowers
  - skill:plans-and-specs
  - skill:executing-plans
  - skill:executing-prompt-workflows
  - skill:verification-before-completion
skills:
  - using-superpowers
  - plans-and-specs
  - executing-plans
  - executing-prompt-workflows
  - verification-before-completion
references:
  - ./specs/run-all-goals-five-day-consolidated-spec.md
  - ./plans/run-all-goals-five-day-consolidated-plan.md
  - ./scripts/audit_default_sessions_window.py
  - ./scripts/summarize_run_all_goals_corpus.py
  - ./.github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py
  - ./.github/prompts/general/run-all-goals/skills/run-all-goals-five-day.md
  - ./.github/prompts/general/run-all-goals/results/five-day-artifact-inventory.md
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

1. Enumerate `./specs/`, `./plans/`, and this prompt package.
2. Resolve all links from the consolidated spec and plan.
3. Mark missing/stale references without fabricating replacements.
4. Write `.github/prompts/general/run-all-goals/results/five-day-artifact-inventory.md` with the live counts and classifications.

**Gate:** Inventory output exists and every required path is classified.

### Phase 3 — Verification

1. Run `python .github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py`.
2. Run `python .github/prompts/general/run-all-goals/scripts/verify_run_all_goals.py`.
3. Run `python .github/prompts/general/run-all-goals/scripts/test_run_all_goals.py`.
4. Check JSON/YAML/Markdown structure.

**Gate:** All local checks pass or a blocker is written to results.

### Phase 4 — Execute

1. Re-run the corpus and summary scripts.
2. Run the deterministic local verification suite and record every exit code.
3. Write `results/five-day-execution-result.md` with command outputs, counts, and blockers.
4. Re-run `python .github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py --require-result` after the result exists.

**Gate:** Result exists and contains fresh evidence.

### Phase 5 — End capture

1. Locate the installed session-end capture mechanism.
2. Run it only if its invocation is known and local-only.
3. Record the result path or explicit unavailable blocker.

**Gate:** End capture attempted and reported.

## Outputs

- `./plans/run-all-goals-five-day-session-corpus.json`
- `./plans/run-all-goals-five-day-session-summary.json`
- `./specs/run-all-goals-five-day-consolidated-spec.md`
- `./plans/run-all-goals-five-day-consolidated-plan.md`
- `.github/prompts/general/run-all-goals/run-all-goals-five-day.prompt.md`
- `.github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py`
- `.github/prompts/general/run-all-goals/skills/run-all-goals-five-day.md`
- `.github/prompts/general/run-all-goals/results/five-day-artifact-inventory.md`
- `.github/prompts/general/run-all-goals/results/five-day-execution-result.md`

## Verification

A run is complete only when every named output exists, every referenced path is classified, and the result file records fresh local command evidence.
