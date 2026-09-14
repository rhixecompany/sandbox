---
name: run-today-and-yesterday-consolidated-plan
sidebar_position: 17
title: "Run Today and Yesterday — Consolidated Implementation Plan"
description: "One dependency-gated plan implementing the discovery, recall, report, and orchestration specifications."
version: 1.0.0
author: Alexa
license: MIT
tags: [plan, sessions, recall, report, orchestration, local-only]
status: completed
specs:
  - ../specs/run-today-and-yesterday-discovery-spec.md
  - ../specs/run-today-and-yesterday-recall-spec.md
  - ../specs/run-today-and-yesterday-report-spec.md
  - ../specs/run-today-and-yesterday-orchestration-spec.md
---

# Run Today and Yesterday — Consolidated Implementation Plan

## Plan rule

This is the **only new implementation plan** for the request. It implements all four canonical specs; no parallel or duplicate plan should be created.

## Objective

Create and verify a reusable general-category prompt that discovers every default-profile Hermes session started today or yesterday in WAT, recalls each session, extracts the requested evidence fields, and writes one redacted Markdown report. Keep the workflow local-only and reproducible.

## Baseline evidence

- Current generated report: `../.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-2026-09-14.md`
- Current verified WAT window: `2026-09-13T00:00:00+01:00` through `2026-09-15T00:00:00+01:00` (exclusive end).
- Current fresh baseline: 93 selected sessions and 7,314 active messages read from the default root database at report-generation time.
- The report is a dated baseline; future executions must recompute the rolling window rather than reuse these counts as live truth.

## Artifact inventory and dedupe decisions

| Requirement cluster | Canonical owner | Duplicate handling |
|---|---|---|
| WAT boundaries, source DB, exact session inventory | `run-today-and-yesterday-discovery-spec.md` | Remove repeated boundary/query rules from other specs; link back. |
| One recall per session and field classification | `run-today-and-yesterday-recall-spec.md` | Keep extraction semantics here; report spec owns layout only. |
| Markdown sections, counts, redaction, bounded excerpts | `run-today-and-yesterday-report-spec.md` | Keep schema and safety rules here; do not duplicate query logic. |
| List/triage/consolidate/dedupe, dependency order, one-plan rule | `run-today-and-yesterday-orchestration-spec.md` | Keep workflow governance here; other specs link to this plan. |

Historical five-day artifacts remain references and are not rewritten or deleted.

## Dependency graph

```text
inventory existing artifacts
        |
        v
P1 discovery/window  --->  P2 per-session recall
        |                         |
        +-------------------------v
                         P3 report generation
                                  |
                                  v
                  P4 specs/links/prompt verification
                                  |
                                  v
                         P5 final evidence gate
```

## Phases and tasks

### P0 — Read-only preflight and inventory

1. Read `AGENTS.md`, the existing five-day prompt, its linked references, and the four new specs.
2. Read the current dated report and record its generation time, window, count, and caveats.
3. List `specs/`, `plans/`, and `.github/prompts/general/run-all-goals/`; classify relevant artifacts as canonical, supporting, historical, duplicate, missing, or out of scope.
4. Confirm the default root `state.db` exists and that `SESSION_REPORT.md` is either present or explicitly unavailable.

**Gate P0:** Source paths and scope are classified; no secret-bearing file is read.

### P1 — Discover the rolling two-day corpus

1. Run the read-only builder with the current WAT date (or an explicit `--date YYYY-MM-DD` for reproducible verification).
2. Confirm the inclusive/exclusive WAT boundaries.
3. Re-read the selected session IDs from the database and compare them to the report's per-session sections.
4. Preserve untitled and zero-message sessions.

**Gate P1:** Exact selected-ID count and report section count agree.

### P2 — Recall and classify every session

1. For every selected session ID, call `session_search` using the default profile.
2. Scroll in bounded windows for large sessions; never replace unavailable evidence with a guess.
3. Extract: title, query, user inputs, plans, specs, prompts, goal, subgoal, tools, usage, clarifying questions, clarifying-question answers, session-report evidence, and errors/warnings.
4. Record recall status, evidence source, and omission/redaction markers per session.

**Gate P2:** A recall status exists for all selected IDs and every required heading is present.

### P3 — Generate the Markdown report

1. Run `build_today_and_yesterday_report.py` as the deterministic base.
2. Add/verify recalled evidence without overwriting literal metadata or changing counts without fresh evidence.
3. Keep tool names/counts but omit raw tool payloads.
4. Apply secret and memory-context redaction before writing.
5. Write the dated report under `.github/prompts/general/run-all-goals/results/`.

**Gate P3:** Report is valid Markdown/UTF-8, contains one section per session, and passes secret-pattern scans.

### P4 — Verify prompt/spec/plan/orchestrator links

1. Verify the execution prompt is named `run-today-and-yesterday.prompt.md` and is under the `general` category.
2. Verify the orchestration prompt references this plan and the created dated report.
3. Verify each spec links to the consolidated plan and its owning artifacts.
4. Verify no second new plan was created for this request.
5. Compile the report-builder script and run static structure/link checks.

**Gate P4:** All links resolve or are explicitly marked missing; frontmatter parses; exactly four new specs and one new plan are present.

### P5 — Final evidence and handoff

1. Record every verification command, exit code, artifact path, and live count.
2. Preserve blockers separately from successful checks.
3. Confirm no model calls, external writes, config writes, commits, pushes, or profile mutations occurred.
4. Return the report, prompts, four specs, plan, and verification summary.

**Gate P5:** Completion claims are backed by fresh tool output and no synthetic IDs/counts are introduced.

## Deliverables

- `../.github/prompts/general/run-all-goals/run-today-and-yesterday.prompt.md`
- `../.github/prompts/general/run-all-goals/orchestrate-run-today-and-yesterday.prompt.md`
- `../.github/prompts/general/run-all-goals/scripts/build_today_and_yesterday_report.py`
- `../.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-2026-09-14.md`
- `./run-today-and-yesterday-discovery-spec.md`
- `./run-today-and-yesterday-recall-spec.md`
- `./run-today-and-yesterday-report-spec.md`
- `./run-today-and-yesterday-orchestration-spec.md`
- `../plans/run-today-and-yesterday-consolidated-plan.md` (this file)

## Safety and non-goals

- Do not read `.env`, auth files, tokens, or raw credential stores.
- Do not call providers or execute live model probes.
- Do not mutate `state.db`, Hermes config, profiles, Git history, remotes, or external services.
- Do not delete or rewrite unrelated specifications/plans.
- Do not claim a session report exists when only a missing-path check was performed.

## Verification checklist

- [ ] WAT date derivation and explicit-date replay pass.
- [ ] Read-only database query returns selected sessions.
- [ ] Report session count equals per-session section count.
- [ ] All required per-session headings exist.
- [ ] Four specs and one plan exist with valid links.
- [ ] Both prompts reference the plan and dated report.
- [ ] Report secret scan passes.
- [ ] Python compilation and repository checks pass.
- [ ] No external/config/model side effects occurred.
