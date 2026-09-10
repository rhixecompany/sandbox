---
name: run-all-goals-five-day-consolidated-plan
title: "Run All Goals — Five-Day Consolidated Implementation Plan"
description: "Sequential local-only plan derived from the Sep 6–10 default-profile session corpus and SandBox artifact inventory."
version: 1.0.0
author: Alexa
license: MIT
tags: [plan, consolidation, sessions, local-only, run-all-goals]
status: completed
profile: default
model: openai/gpt-5.6-luna
linked_specs:
  - ../specs/run-all-goals-five-day-consolidated-spec.md
---

# Run All Goals — Five-Day Consolidated Implementation Plan

## Goal
Turn the verified five-day session corpus and workspace inventory into a linked, executable, locally verified implementation package.

## Evidence baseline

- Window: Sep 6–10, 2026 WAT inclusive; exclusive end Sep 11.
- Default profile source: `C:/Users/Alexa/AppData/Local/hermes/state.db`.
- Corpus: 136 sessions, 742 bounded redacted evidence excerpts.
- Workspace inventory: 31 specs, 126 plan entries/dirs, existing run-all-goals prompt package.
- Scope exclusion: no remote writes, provider probes, commits, pushes, `.env` copying, or profile fan-out.

## Dependencies

| ID | Dependency | Gate |
|---|---|---|
| DEP-001 | Session corpus exists | Phase 1 |
| DEP-002 | Disk inventory exists | Phase 2 |
| DEP-003 | Spec and plan links parse | Phase 3 |
| DEP-004 | Prompt and scripts verify | Phase 4 |
| DEP-005 | Local execution output exists | Phase 5 |

## Phases

### Phase 1 — Corpus freeze and recall

**Tasks**

- T1.1: Confirm WAT window and default profile.
- T1.2: Run `audit_default_sessions_window.py` against root `state.db`.
- T1.3: Run `summarize_run_all_goals_corpus.py`.
- T1.4: Use `session_search` to recall relevant goal/spec/plan/prompt evidence.

**Gate:** Corpus and summary exist; counts and scope match the clarified request.

### Phase 2 — Workspace inventory

**Tasks**

- T2.1: Enumerate `.hermes/specs/` files and sizes.
- T2.2: Enumerate `.hermes/plans/` files/dirs and sizes.
- T2.3: Enumerate `/run-all-goals` prompt package files.
- T2.4: Resolve references and classify missing/stale/generated artifacts.

**Gate:** Inventory is complete and no artifact is treated as present without a disk check.

### Phase 3 — Artifact creation

**Tasks**

- T3.1: Create the consolidated spec and link it to this plan.
- T3.2: Create this plan and link it back to the spec.
- T3.3: Create the executable local-only prompt.
- T3.4: Create/verify the deterministic scripts and workflow skill.

**Gate:** YAML frontmatter parses; bidirectional links resolve; scripts are present.

### Phase 4 — Artifact verification

**Tasks**

- T4.1: Verify all generated paths and references.
- T4.2: Check placeholder/secret markers without reading `.env` values.
- T4.3: Run prompt package verification and tests.
- T4.4: Record historical claims separately from live results.

**Gate:** All artifact checks pass or produce an explicit blocker report.

### Phase 5 — Local execution

**Tasks**

- T5.1: Re-run corpus and summary scripts.
- T5.2: Execute the local prompt phase runner.
- T5.3: Run final workspace-native checks.
- T5.4: Write an execution result under the prompt package results directory.

**Gate:** Every local phase has a result and no out-of-scope side effect occurred.

### Phase 6 — End capture and closeout

**Tasks**

- T6.1: Run session-end capture using the installed capture mechanism if available.
- T6.2: Re-read the final result and plan/spec status.
- T6.3: Report pass/fail/blocker evidence.

**Gate:** End-capture attempted; final artifacts and blockers are on disk.

## Resource allocation

| Resource | Allocation |
|---|---|
| Main agent | Sequential gates, artifact authoring, final verification |
| MCP filesystem | Read/list/write workspace artifacts |
| session_search | Historical session recall |
| Terminal | Local scripts, syntax, tests |
| Subagents | None required; corpus and gates are stateful/sequential |
| External APIs | 0; explicitly out of scope |

## Rollback

- Generated artifacts can be removed individually through Git/local file rollback.
- No global Hermes config, `.env`, profile memory, or remote state is modified by this plan.
- If a generated artifact is malformed, stop and repair it before Phase 5.

## Linked Specs

- `../specs/run-all-goals-five-day-consolidated-spec.md`

## Status

- [x] Session scope clarified
- [x] Five-day corpus inventoried
- [x] Workspace spec/plan/prompt inventory completed
- [x] Consolidated artifact package created and verified
- [x] Local execution completed
- [x] End capture completed — `C:/Users/Alexa/AppData/Local/hermes/logs/sessions/20260910_230758_d40589.end.json`
