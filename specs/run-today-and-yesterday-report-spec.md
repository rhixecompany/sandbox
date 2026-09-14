---
name: run-today-and-yesterday-report-spec
sidebar_position: 19
title: "Run Today and Yesterday — Markdown Report"
description: "Define the redacted Markdown report and deterministic evidence schema for the two-day session window."
version: 1.0.0
author: Alexa
license: MIT
tags: [spec, report, markdown, redaction, sessions]
status: completed
---

# Run Today and Yesterday — Markdown Report Specification

## Goal

Create one auditable Markdown report containing the outputs and evidence summary for every discovered today-and-yesterday session, with exact coverage counts and explicit redaction/caveat handling.

## Report identity

- **Current generated artifact:** `./.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-2026-09-14.md`
- **Future output pattern:** `run-today-and-yesterday-report-YYYY-MM-DD.md`, where the date is today in WAT.
- **Generator:** `./.github/prompts/general/run-all-goals/scripts/build_today_and_yesterday_report.py`
- **Source:** root/default `C:/Users/Alexa/AppData/Local/hermes/state.db`, opened read-only.

## Required document structure

1. YAML frontmatter with report name, generation time, WAT window, session count, message read-back count, source DB, and redaction policy.
2. Scope and method section explaining selection by `started_at`, `session_search` recall requirement, and side-effect boundary.
3. Coverage summary table with sessions found, active messages read, titled sessions, tool-call sessions, and zero-message sessions.
4. `## Per-session outputs` followed by one numbered section per discovered ID.
5. Each session section contains the exact headings from the recall specification: Query, User inputs, Plans, Specs, Prompts, Goals, Subgoals, Tools, Usage, Clarifying questions, Clarifying-question answers, Session-report evidence, Errors and warnings, and Assistant output excerpts.
6. A final verification/caveats section when the orchestrator adds recall status, stale-baseline notes, or blockers.

## Redaction and size rules

- Remove `<memory-context>` blocks from direct user inputs.
- Replace obvious secrets with `[REDACTED]` and private-key bodies with `[PRIVATE_KEY_REDACTED]`.
- Do not expose `.env` or auth-file contents.
- Bound excerpts per field and preserve omitted-count/ellipsis markers when content is larger than the bound.
- Store tool names and invocation counts, not raw tool payloads.
- Preserve literal session identifiers and report missing values as `—`.

## Triage and dedupe decisions

The source requirements were triaged into four non-overlapping concerns:

- **Discovery:** date boundaries, database query, exact session inventory, and metadata.
- **Recall:** per-session `session_search`, field extraction, and evidence classification.
- **Report:** Markdown schema, coverage, redaction, bounded excerpts, and caveats.
- **Orchestration:** execution order, one-plan rule, verification gates, and no-side-effect policy.

Repeated requirements were retained only in the canonical spec that owns them; other specs link to that owner instead of duplicating the full rule. No fifth overlapping spec is needed.

## Acceptance criteria

- **AC-M001:** The report has exactly one per-session section for every discovered ID.
- **AC-M002:** Frontmatter counts match the report's coverage table and session sections.
- **AC-M003:** All requested fields are present for every session, including explicit empty markers.
- **AC-M004:** Secret-pattern scans find no unredacted bearer/key/token/private-key values.
- **AC-M005:** The generated report is valid UTF-8 Markdown and its links resolve or are marked as missing.
- **AC-M006:** The report distinguishes fresh local evidence from historical claims and unavailable session-report files.

## References

- `./run-today-and-yesterday-discovery-spec.md`
- `./run-today-and-yesterday-recall-spec.md`
- `./run-today-and-yesterday-orchestration-spec.md`
- `../plans/run-today-and-yesterday-consolidated-plan.md`
- `../.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-2026-09-14.md`
