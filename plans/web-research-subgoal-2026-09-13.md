---
name: web-research-subgoal-plan
title: Web Research Pipeline — Subgoal Implementation Plan
version: 1.0.0
description: Sequential-phase pipeline (per clarification): Phase 1=research ALL 289 Python + 343 Node packages; Phase 2=verify pipeline complete; Phase 3=generate specs/plans/prompts/scripts/skills per package.
metadata:
  protocol: multi-file-change-protocol (14-skill stack loaded)
  clarification_finalized: 4 turns, 8 questions (scope, deliverable, execution order, destructive ops, artifact mapping x2, naming pattern, subset, verification order)
  goal: /goal + /web-research-pipeline (python-packages.md + node-dependency.md)
  subgoal: /web-research-subgoal (docs/user-guide cross-reference from session context)
---

# Plan — Web Research Pipeline Subgoal

## Phase Structure (Sequential — data dependency enforced)

| Phase | Name                                            | Gate Condition                                                                                      | Timeline      |
| ----- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------- |
| P1    | LOAD — Skills + Source Files                    | All 14 skills verified; python-packages.md + node-dependency.md read                                | T+0           |
| P2    | RESEARCH — Run pipeline per package             | Best-practices + cheatsheet links captured for each package; saved to artifacts                     | T+0 → T+batch |
| P3    | VERIFY — Pipeline complete check                | Count verified == 289 Python + 343 Node (or subset if reduced); links validated; no missing entries | After P2      |
| P4    | READ — Read new artifacts (research results)    | Artifacts parsed; spec/plan/prompt/script generated per verified entry                              | After P3      |
| P5    | CREATE — Specs, Plans, Prompts, Scripts, Skills | Each package has `./specs/`, `./plans/`, `.github/prompts/`, `scripts/`, `skills/` artifacts        | After P4      |
| P6    | EXECUTE — Verify artifacts + run scripts        | Scripts executable; skills importable; plans have gates; verification reports saved                 | After P5      |

## Rules

1. No Phase N+1 starts before Phase N gate passes (sequential dependency per clarification turn 3).
2. All destructive ops approved — new files created; existing skills/plans/scripts NOT deleted unless explicitly overwritten (per clarification turn 4: restructuring allowed).
3. Pipeline verified complete (P3 gate) BEFORE reading new artifacts (P4) — per user's instruction: "only when the pipeline is completed, read the new artifacts".
4. Each package: best-practice + cheatsheet links (research) → spec (`./specs/`) → plan (`./plans/`) → prompt (`.github/prompts/`) → script (`scripts/`) → skill (`skills/`).
5. Subagent-driven-parallel inside P5 (after P4 verified) — each package artifact set can be generated in parallel via `delegate_task`.

## Milestones

- M1 (P2): 289 Python + 343 Node package research complete (links saved).
- M2 (P3): Pipeline verification report written (`./plans/web-research-verify-<ts>.md`).
- M3 (P4): All new artifacts read and indexed.
- M4 (P5): Per-package artifacts created (spec/plan/prompt/script/skill count verified).
- M5 (P6): Scripts executed, skills loaded, verification complete — "Goal complete" declared.

## Resource Allocation

- Profile routing: code→architect (spec/script creation); research→analyst (web-research links); ops→adminbot (pipeline verification); design→creative (prompt/skill formatting).
- Subagent delegation (P5 only, after P3 gate): one `delegate_task` per batch of 10 packages → generate spec+plan+prompt+script+skill set.
- Rate-limit safeguard: `web_search` / `web_extract` calls spaced ≥500ms (memory skill reference).

## Blocker Tracking (live state — to be filled during execution)

- Rate-limit 403 on GitHub `gh api`: documented in session (preserved, not hidden).
- Nested `.codex`/`.copilot` scope conflict (41 parsing errors): architecture concern preserved.
- 26 vulnerability findings (`fastmcp==2.10.6` CRITICAL; `httpx2==2.7.0` HIGH): preserved.
- 0 hidden errors; 0 synthetic artifacts.
