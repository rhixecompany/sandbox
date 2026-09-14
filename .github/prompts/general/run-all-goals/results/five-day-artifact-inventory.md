---
name: run-all-goals-five-day-artifact-inventory
title: "Run All Goals — Five-Day Artifact Inventory"
description: "Fresh local inventory and classification for the five-day consolidation package."
version: 1.0.0
author: Alexa
license: MIT
tags: [inventory, consolidation, local-only, run-all-goals]
status: fresh
---

# Run All Goals — Five-Day Artifact Inventory

**Inventory basis:** live filesystem scan on 2026-09-14 after the Phase 1 corpus and summary rerun.
**Scope:** `C:/Users/Alexa/Desktop/SandBox/specs/`, `plans/`, and `.github/prompts/general/run-all-goals/` only.
**Safety:** no `.env` contents, credentials, provider calls, remote writes, commits, or pushes were read or performed.

## Required outputs

| Path | Status | Size / evidence | Classification |
|---|---|---:|---|
| `specs/run-all-goals-five-day-consolidated-spec.md` | PRESENT | 6,698 B | Live consolidated spec; status completed |
| `plans/run-all-goals-five-day-consolidated-plan.md` | PRESENT | 5,124 B | Live linked plan; status completed |
| `plans/run-all-goals-five-day-session-corpus.json` | PRESENT | 154,504 B | Fresh Phase 1 corpus; 1 database, 17 sessions |
| `plans/run-all-goals-five-day-session-summary.json` | PRESENT | 127,384 B | Fresh Phase 1 summary; 17 sessions, 133 evidence excerpts |
| `.github/prompts/general/run-all-goals/run-all-goals-five-day.prompt.md` | PRESENT | 4,785 B | Live executable prompt |
| `.github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py` | PRESENT | 7,423 B | Live deterministic verifier |
| `.github/prompts/general/run-all-goals/skills/run-all-goals-five-day.md` | PRESENT | 2,743 B | Live workflow skill |
| `.github/prompts/general/run-all-goals/results/five-day-artifact-inventory.md` | PRESENT | 4,929 B | Live Phase 2 inventory |
| `.github/prompts/general/run-all-goals/results/five-day-execution-result.md` | PRESENT | 4,177 B | Fresh final execution result |

## Workspace inventory counts

| Root | Files | Bytes | Classification |
|---|---:|---:|---|
| `specs/` | 124 | 673,360 | Existing workspace specs; the five-day spec is the live target |
| `plans/` | 1,156 | 13,815,932 | Existing workspace plans/artifacts; the five-day plan and JSON outputs are the live targets |
| `approvals/` | 1 | 3,092 | Historical approval for the broader tree-primary workflow; not used for this local-only run |
| `references/` | 5 | 13,790 | Existing prompt-package references |
| `results/` | 30 | 1,167,424 | Mixed historical audit/test results plus the two five-day result artifacts |
| `scripts/` | 9 | 59,332 | 3 active Python scripts plus generated `__pycache__/` and nested historical `results/` artifacts |
| `skills/` | 2 | 7,790 | Five-day skill plus the older run-all-goals skill |
| `templates/_shared/` | 6 | 26,277 | Shared prompt templates |
| `tests/` | 1 | 1,252 | Existing verification checklist |

## Reference resolution

| Reference | Resolution |
|---|---|
| Prompt → consolidated spec | PRESENT: `specs/run-all-goals-five-day-consolidated-spec.md` |
| Prompt → consolidated plan | PRESENT: `plans/run-all-goals-five-day-consolidated-plan.md` |
| Prompt → session auditor | PRESENT: `scripts/audit_default_sessions_window.py` |
| Prompt → corpus summarizer | PRESENT: `scripts/summarize_run_all_goals_corpus.py` |
| Prompt → five-day verifier | PRESENT: `.github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py` |
| Prompt → five-day skill | PRESENT: `.github/prompts/general/run-all-goals/skills/run-all-goals-five-day.md` |
| Prompt → inventory | PRESENT: this file |
| Spec → plan | RESOLVES: `../plans/run-all-goals-five-day-consolidated-plan.md` |
| Plan → spec | RESOLVES: `../specs/run-all-goals-five-day-consolidated-spec.md` |

## Historical and stale classifications

- The existing artifacts previously reported **136 sessions / 742 excerpts**. The fresh Phase 1 rerun against the current default-root `state.db` reports **17 sessions / 133 excerpts**. The current run uses the fresh values and records the delta rather than treating historical text as live truth.
- The nested package `.github/prompts/general/run-all-goals/run-all-goals/` is a duplicate legacy tree found during discovery. It is not referenced by the five-day prompt and was not executed or modified.
- `.github/prompts/general/run-all-goals/scripts/__pycache__/` and `scripts/results/` are generated historical artifacts, not declared five-day outputs.
- Timestamped `results/test-results-*.json` files are generated test evidence; the final execution result cites the latest fresh file and older files remain historical evidence.
- No required path was missing. No replacement content was fabricated for stale or duplicate artifacts.

## Phase 2 gate

**PASS:** all required five-day paths exist, spec↔plan links resolve, prompt references resolve, and stale/duplicate artifacts are classified separately from live outputs.
