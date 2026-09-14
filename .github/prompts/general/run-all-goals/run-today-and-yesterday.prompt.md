---
name: run-today-and-yesterday
sidebar_position: 17
category: general
title: "Run Today and Yesterday — Session Recall and Report"
description: "Recall every default-profile session from today and yesterday in WAT, extract requested evidence, and write one redacted Markdown report."
version: 1.0.0
author: Alexa
license: MIT
tags: [prompt, general, sessions, recall, report, local-only]
trigger: /run-today-and-yesterday
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
  - ./run-all-goals-five-day.prompt.md
  - ../../../../specs/run-today-and-yesterday-discovery-spec.md
  - ../../../../specs/run-today-and-yesterday-recall-spec.md
  - ../../../../specs/run-today-and-yesterday-report-spec.md
  - ../../../../specs/run-today-and-yesterday-orchestration-spec.md
  - ../../../../plans/run-today-and-yesterday-consolidated-plan.md
  - ./scripts/build_today_and_yesterday_report.py
  - ./results/run-today-and-yesterday-report-2026-09-14.md
  - ./orchestrate-run-today-and-yesterday.prompt.md
---

# Goal

Create a reproducible, local-only Markdown report containing the recalled outputs of **all default-profile Hermes sessions started today and yesterday in WAT**. Then list, triage, consolidate, and deduplicate the related requirements into the four canonical specs, while using only the one consolidated implementation plan.

This prompt is derived from `run-all-goals-five-day.prompt.md`, but its time window is rolling and limited to the current WAT day plus the preceding WAT day.

## Scope and fixed decisions

- Workspace: `C:/Users/Alexa/Desktop/SandBox`
- Session database: `C:/Users/Alexa/AppData/Local/hermes/state.db`
- Profile scope: root/default profile database; include every real recorded source in that database.
- Window: `[yesterday 00:00:00 WAT, tomorrow 00:00:00 WAT)`; today is computed at runtime using `Africa/Lagos`/WAT.
- Selection: sessions whose `started_at` falls inside the window. Report `ended_at` and `last_activity_at` but do not silently expand the selection.
- Current baseline report: `./.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-2026-09-14.md`
- One plan: `./plans/run-today-and-yesterday-consolidated-plan.md`
- Four canonical specs: discovery, recall, report, and orchestration.

## Non-negotiable safety rules

- Read `AGENTS.md` and relevant source files before writing or executing artifacts.
- Do not read or print `.env`, auth files, tokens, credentials, private keys, or raw secret-bearing files.
- Do not call live models/providers, write Hermes config, mutate profiles or `state.db`, commit, push, sync externally, or delete unrelated artifacts.
- Use read-only database access and local files/tests only.
- Keep literal session IDs and fresh counts; never fabricate missing sessions, answers, plans, specs, tools, usage, errors, or session reports.
- If `SESSION_REPORT.md` is absent, record `missing` with the checked path; do not invent a report.
- Treat prior completion text as historical evidence until verified against the current database/filesystem.
- Stop on a failed gate and record the command, exit code, and blocker.

## Phase 1 — Read and inventory

1. Read `AGENTS.md`.
2. Read the template prompt `./run-all-goals-five-day.prompt.md` and the four linked specs/plan.
3. Read the current dated report as a baseline, recording its generation time, WAT window, count, and caveats.
4. List `./specs/`, `./plans/`, and `./.github/prompts/general/run-all-goals/`.
5. Classify relevant artifacts as canonical input, supporting reference, historical evidence, duplicate/overlap, missing, or out of scope.

**Gate:** Scope, source DB, baseline report, and artifact classifications are recorded.

## Phase 2 — Discover the rolling session window

Run the deterministic read-only builder:

```bash
C:/Users/Alexa/myvenv/Scripts/python.exe \
  .github/prompts/general/run-all-goals/scripts/build_today_and_yesterday_report.py
```

For reproducible verification of a known day, use:

```bash
C:/Users/Alexa/myvenv/Scripts/python.exe \
  .github/prompts/general/run-all-goals/scripts/build_today_and_yesterday_report.py \
  --date YYYY-MM-DD \
  --output .github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-YYYY-MM-DD.md
```

Verify the generated frontmatter declares the WAT start/end, default source DB, exact session count, and active-message read-back count.

**Gate:** Discovery succeeds and the report contains one inventory record per selected ID.

## Phase 3 — Recall every session

For each exact session ID from the discovery output, perform an individual `session_search` recall using the default profile. Use bounded scroll windows for large sessions. Do not skip untitled, zero-message, compacted, or partially available sessions; record their recall status.

For each session, extract these headings exactly:

1. Session title
2. Query
3. User inputs
4. Plans
5. Specs
6. Prompts
7. Goals
8. Subgoals
9. Tools
10. Usage
11. Clarifying questions
12. Clarifying-question answers
13. Session-report evidence
14. Errors and warnings
15. Assistant output excerpts

Classification rules:

- Query = first direct user query after omitting non-input memory context.
- User inputs remain ordered and bounded; do not collapse distinct inputs into one invented summary.
- Plans/specs/prompts are included only when explicitly evidenced by recalled text or a real path.
- Goals/subgoals require explicit labels or named goal IDs.
- Tools come from recorded tool names/structured calls; store names and counts, never raw payloads.
- Usage comes from real session metadata and read-back counts.
- Clarifying-question answers are the next direct user evidence only when present.
- Errors are evidence excerpts and do not imply total session failure.

**Gate:** Every discovered ID has a recall status and every required heading is present.

## Phase 4 — Write the report

Use the deterministic builder output as the base, then add verified `session_search` evidence without changing literal metadata or counts without fresh evidence. Write a dated file at:

```text
./.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-YYYY-MM-DD.md
```

Apply these report rules:

- Remove `<memory-context>` blocks from direct user-input sections.
- Replace obvious credentials, API keys, tokens, bearer values, passwords, and private keys with `[REDACTED]`.
- Do not persist raw `.env`/auth contents or raw tool payloads.
- Preserve omitted-count/ellipsis markers for bounded excerpts.
- Distinguish fresh evidence, historical claims, missing files, and unavailable recall.

**Gate:** The report is valid UTF-8 Markdown, has exact coverage counts, and passes secret-pattern scanning.

## Phase 5 — List, triage, consolidate, deduplicate

1. List the relevant existing specs, plans, prompts, scripts, references, and reports.
2. Triage each item as canonical input, supporting reference, historical evidence, duplicate/overlap, missing, or out of scope.
3. Consolidate this request into exactly these four specs:
   - `specs/run-today-and-yesterday-discovery-spec.md`
   - `specs/run-today-and-yesterday-recall-spec.md`
   - `specs/run-today-and-yesterday-report-spec.md`
   - `specs/run-today-and-yesterday-orchestration-spec.md`
4. Deduplicate repeated rules by keeping each rule in its owning spec and linking from the others.
5. Use only `plans/run-today-and-yesterday-consolidated-plan.md` as the implementation plan. Never create a second plan for this request.
6. Verify both this prompt and `orchestrate-run-today-and-yesterday.prompt.md` reference the dated report and the single plan.

**Gate:** Exactly four canonical specs and one new consolidated plan are linked; unrelated historical files remain untouched.

## Phase 6 — Verification and handoff

Run local checks for:

- Python compilation of `build_today_and_yesterday_report.py`.
- Markdown/frontmatter structure for the two prompts, four specs, plan, and report.
- Internal links and required headings.
- Report session count versus per-session sections.
- Secret-pattern scan.
- Read-only/no-side-effect confirmation.

Write a concise execution result or append a verification section to the dated report with exact commands, exit codes, counts, artifact paths, and blockers. Do not claim `SESSION_REPORT.md` or any other artifact exists unless the filesystem read confirms it.

## Outputs

- `./.github/prompts/general/run-all-goals/run-today-and-yesterday.prompt.md`
- `./.github/prompts/general/run-all-goals/orchestrate-run-today-and-yesterday.prompt.md`
- `./.github/prompts/general/run-all-goals/scripts/build_today_and_yesterday_report.py`
- `./.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-YYYY-MM-DD.md`
- `./specs/run-today-and-yesterday-discovery-spec.md`
- `./specs/run-today-and-yesterday-recall-spec.md`
- `./specs/run-today-and-yesterday-report-spec.md`
- `./specs/run-today-and-yesterday-orchestration-spec.md`
- `./plans/run-today-and-yesterday-consolidated-plan.md`

## Completion condition

The prompt is complete only when the current WAT window is freshly enumerated, every selected session is individually recalled or explicitly marked unavailable, all requested fields are represented, the report is written and redacted, the four specs are deduplicated and linked, the single plan is verified, and every claim is backed by fresh local tool output.
