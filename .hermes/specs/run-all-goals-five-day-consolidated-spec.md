---
name: run-all-goals-five-day-consolidated-spec
title: "Run All Goals — Five-Day Session Consolidation Specification"
description: "Evidence-backed local-only consolidation of all default-profile sessions and SandBox planning artifacts from Sep 6–10, 2026 WAT."
version: 1.0.0
author: Alexa
license: MIT
tags: [spec, consolidation, sessions, run-all-goals, local-only]
status: approved
linked_plan: ../plans/run-all-goals-five-day-consolidated-plan.md
---

# Run All Goals — Five-Day Consolidation Specification

## Goal
Create an auditable, local-only execution package from the default-profile Hermes session corpus for **Sep 6–10, 2026 WAT inclusive**, then execute it against the SandBox workspace and verify every deliverable on disk.

## Scope and evidence

- **Session scope:** root default-profile `C:/Users/Alexa/AppData/Local/hermes/state.db`; all sources, including cron.
- **Session evidence:** `session_search` recall plus the generated metadata/evidence corpus.
- **Workspace scope:** `C:/Users/Alexa/Desktop/SandBox`, `.hermes/`, `.github/`.
- **Output roots:** `.hermes/specs/`, `.hermes/plans/`, `.github/prompts/general/run-all-goals/`.
- **Side effects:** local files and tests only. No provider probes, external sync, commit, push, or remote writes.
- **Current evidence baseline:** 136 sessions, 742 bounded redacted excerpts, 31 specs, 126 plan entries/dirs, and the existing `/run-all-goals` artifact tree.

## Requirements

- **REQ-001:** Preserve the exact five-day WAT window and default-profile scope.
- **REQ-002:** Inventory every session before creating consolidated artifacts.
- **REQ-003:** Recall goals, subgoals, specs, plans, prompts, phases, steps, tasks, and actions from session evidence without fabricating missing facts.
- **REQ-004:** Inventory existing specs, plans, prompts, scripts, skills, templates, references, approvals, tests, and results on disk.
- **REQ-005:** Create one linked specification, one linked implementation plan, one executable prompt, and deterministic local verification scripts.
- **REQ-006:** Execute artifacts only after frontmatter, links, paths, and source counts pass validation.
- **REQ-007:** Execute phases sequentially; parallelize only independent read-only inventory work.
- **REQ-008:** Preserve `.env`, credentials, profile databases, Git history, and external state.
- **REQ-009:** Record blockers and historical claims separately from live verification.
- **REQ-010:** Perform final on-disk verification and session-end capture before completion.

## Consolidated goals and subgoals

### GOAL-1 — Session and artifact evidence
- **SG1.1:** Capture session-start state and validate memory/profile prerequisites.
- **SG1.2:** Enumerate default-profile sessions for the fixed WAT window.
- **SG1.3:** Recall and classify goal/spec/plan/prompt/phase/task/action evidence.
- **SG1.4:** Inventory workspace specs, plans, prompts, scripts, skills, templates, references, approvals, tests, and results.

### GOAL-2 — Consolidated artifact package
- **SG2.1:** Create this specification with measurable acceptance criteria.
- **SG2.2:** Create the linked implementation plan with dependency gates.
- **SG2.3:** Create the executable `/run-all-goals-five-day` prompt.
- **SG2.4:** Create deterministic scripts and a reusable workflow skill.

### GOAL-3 — Local execution
- **SG3.1:** Re-validate sources and links before execution.
- **SG3.2:** Run the consolidated prompt in phase order.
- **SG3.3:** Run workspace-native verification plus artifact-specific verification.
- **SG3.4:** Capture the end state and preserve blockers.

### GOAL-4 — Integrity and safety
- **SG4.1:** No secrets or credentials enter generated artifacts.
- **SG4.2:** No destructive or external action executes outside the clarified scope.
- **SG4.3:** Every completion claim is backed by fresh tool output.
- **SG4.4:** Historical completion claims are not treated as live evidence.

## Acceptance criteria

- **AC-001:** Corpus JSON exists and declares `start_wat=2026-09-06`, `end_wat_exclusive=2026-09-11`, default root `state.db`, and `session_count=136` or a fresh, explained delta.
- **AC-002:** Corpus summary exists with per-day/source counts and bounded redacted evidence.
- **AC-003:** This spec, the linked plan, and the executable prompt exist and parse.
- **AC-004:** Every referenced artifact path exists or is explicitly marked missing/blocking.
- **AC-005:** Plan↔spec links are bidirectional.
- **AC-006:** Prompt frontmatter is valid and its local script references resolve.
- **AC-007:** Verification scripts execute successfully against the current workspace, or return an explicit blocker with evidence.
- **AC-008:** No generated file contains credential values, raw `.env` content, or fabricated session IDs.
- **AC-009:** Final verification records file existence, JSON/YAML/Markdown structure, and execution results.
- **AC-010:** Session-end capture is attempted after all local work and its result is recorded.

## Non-functional requirements

- **NFR-001:** Deterministic, resumable, append-only evidence files.
- **NFR-002:** Windows/MSYS-safe paths using native `C:/...` paths for native tools.
- **NFR-003:** No broad recursive deletion or profile fan-out.
- **NFR-004:** Redact obvious secrets from persisted evidence excerpts.
- **NFR-005:** Keep scripts in `scripts/`; no inline executable code in the prompt.

## Linked Plan

- `../plans/run-all-goals-five-day-consolidated-plan.md`

## Verification

- `python scripts/audit_default_sessions_window.py --start 2026-09-06 --end 2026-09-11`
- `python scripts/summarize_run_all_goals_corpus.py`
- `python scripts/verify_run_all_goals_five_day.py`
- `python .github/prompts/general/run-all-goals/scripts/verify_run_all_goals.py`
- `python .github/prompts/general/run-all-goals/scripts/test_run_all_goals.py`

## Known blockers carried forward

- Requested names `/create-implementation-spec`, `/implementation-spec`, `/executing-specs`, `/create-implementation-prompt`, `/implementation-prompt`, `/executing-prompts`, and `/brainstorming` variants were not all resolvable as installed skills; verified equivalents are used.
- `validate_memories.py` currently reports 4 memory issues outside this local consolidation scope.
- Live tooling MCP servers were blocked by a FastMCP/MCP dependency mismatch during the preceding run; this package records the blocker but does not mutate global environments or run provider probes.
