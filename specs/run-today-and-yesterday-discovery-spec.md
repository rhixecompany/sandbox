---
name: run-today-and-yesterday-discovery-spec
sidebar_position: 17
title: "Run Today and Yesterday — Session Discovery"
description: "Define the reproducible WAT session-window inventory used by the today-and-yesterday report."
version: 1.0.0
author: Alexa
license: MIT
tags: [spec, sessions, discovery, recall, local-only]
status: completed
---

# Run Today and Yesterday — Session Discovery Specification

## Goal

Enumerate every default-profile Hermes session whose `started_at` falls in the current and previous calendar day in West Africa Time (WAT), without silently dropping sources, inventing IDs, or mutating Hermes state.

## Scope

- **Workspace:** `C:/Users/Alexa/Desktop/SandBox`
- **Session database:** `C:/Users/Alexa/AppData/Local/hermes/state.db`
- **Profile scope:** the root/default profile database, all recorded sources in that database (`tui`, `cli`, `cron`, desktop, and any other real source values).
- **Window:** `[yesterday 00:00:00 WAT, tomorrow 00:00:00 WAT)`; today is computed at execution time.
- **Selection key:** `sessions.started_at`; `ended_at` and `last_activity_at` are reported but do not expand the selection window.
- **Side effects:** read-only database access and local report/artifact writes only. No network, model call, provider probe, config mutation, commit, push, or profile mutation.

## Functional requirements

- **DISC-001:** Derive today from `Africa/Lagos`/WAT, not from an implicit UTC or host-local date.
- **DISC-002:** Use an inclusive start and exclusive end boundary so midnight sessions are classified deterministically.
- **DISC-003:** Return every matching session ID exactly as stored in `state.db`.
- **DISC-004:** Capture title, source, profile, start/end/last-activity timestamps, message count, tool-call count, token usage, cost fields, end reason, cwd, and branch when present.
- **DISC-005:** Read active messages for every selected session in database order for downstream recall and extraction.
- **DISC-006:** Preserve zero-message and untitled sessions as real records; represent missing values as `—` or an explicit null marker.
- **DISC-007:** Record the exact window, database path, selection rule, session count, and message read-back count in the report frontmatter and body.
- **DISC-008:** Treat historical counts as comparison evidence only; fresh database counts are authoritative for the run.

## Acceptance criteria

- **AC-D001:** The discovery output contains `window_start_wat`, `window_end_wat_exclusive`, `source_db`, and an exact `session_count`.
- **AC-D002:** The session count equals the number of selected rows returned by the read-only query.
- **AC-D003:** Every selected row has a corresponding per-session report section.
- **AC-D004:** No session ID is fabricated, normalized, or replaced by a placeholder.
- **AC-D005:** A rerun for a supplied `--date YYYY-MM-DD` reproduces the same window and selection for an unchanged database.
- **AC-D006:** Database open mode is read-only and no write transaction is issued.

## Evidence and implementation references

- `./.github/prompts/general/run-all-goals/scripts/build_today_and_yesterday_report.py`
- `./.github/prompts/general/run-all-goals/run-today-and-yesterday.prompt.md`
- `./.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-2026-09-14.md`
- `../plans/run-today-and-yesterday-consolidated-plan.md`

## Verification

- Run the report builder with `--date 2026-09-14` and verify the WAT boundaries and count.
- Query `state.db` read-only and compare selected IDs with report session IDs.
- Compile the builder and run the repository Markdown/frontmatter checks.
