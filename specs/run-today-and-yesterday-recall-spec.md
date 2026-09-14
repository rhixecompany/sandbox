---
name: run-today-and-yesterday-recall-spec
sidebar_position: 18
title: "Run Today and Yesterday — Session Recall"
description: "Define per-session recall and evidence extraction for the requested session fields."
version: 1.0.0
author: Alexa
license: MIT
tags: [spec, sessions, recall, session-search, evidence]
status: completed
---

# Run Today and Yesterday — Session Recall Specification

## Goal

Recall each discovered session individually and extract the requested evidence fields without treating missing, compacted, or historical material as verified live facts.

## Canonical recall procedure

1. Read the discovery output and take its exact session-ID list.
2. For **every** ID, call `session_search` with the default profile and that session ID. Use the tool's scroll shape when the session is too large for one response.
3. Preserve the session ID, title, and recall status even when a session is empty, unavailable, or partially compacted.
4. Use local `state.db` message metadata and the read-only report builder for deterministic counts; use `session_search` recall to inspect conversation evidence and classify it.
5. Mark unavailable or ambiguous evidence explicitly. Do not infer a plan, goal, tool, answer, or error that is not present in the recalled evidence.

## Required per-session fields

Every report section must contain these headings, even when the value is `—`:

1. **Session title**
2. **Query** — the first direct user query after removing non-input memory context.
3. **User inputs** — bounded, ordered direct user inputs.
4. **Plans**
5. **Specs**
6. **Prompts**
7. **Goals**
8. **Subgoals**
9. **Tools** — names and counts only; never raw secret-bearing tool payloads.
10. **Usage** — message, tool-call, token, cache, reasoning, and cost fields when available.
11. **Clarifying questions** — assistant questions that request a decision, confirmation, or missing requirement.
12. **Clarifying-question answers** — the next direct user evidence associated with each captured question, or `—` when no answer is present.
13. **Session-report evidence** — `SESSION_REPORT.md`, end-capture, execution-summary, or equivalent references found in evidence.
14. **Errors and warnings** — explicit failures, exceptions, blockers, timeouts, or warnings.
15. **Assistant output excerpts** — bounded beginning/end excerpts proving that outputs were inspected.

## Classification rules

- A message may appear in more than one evidence category when it contains multiple explicit signals.
- `plans`, `specs`, and `prompts` classify paths, headings, and direct references; do not count a generic use of the word as a created artifact unless the evidence says so.
- `goals` and `subgoals` classify explicit goal/subgoal labels, numbered goal sections, or named subgoal IDs.
- Tools come from recorded `tool_name` and structured tool-call metadata; do not infer tools from prose alone.
- Clarifying answers are associated only when a subsequent direct user message is actually present.
- Errors are evidence excerpts, not a claim that the entire session failed.

## Safety requirements

- Omit `<memory-context>` blocks from direct user-input output.
- Redact credentials, API keys, tokens, bearer values, passwords, private keys, and raw `.env`/auth contents before writing the report.
- Do not persist raw tool output when tool names/counts satisfy the requested field.
- Keep session IDs and timestamps literal; never synthesize IDs or timestamps.

## Acceptance criteria

- **AC-R001:** The recall ledger has one row/status for every discovered session ID.
- **AC-R002:** Every per-session report section contains all 15 required headings.
- **AC-R003:** Sessions with no clarifying question explicitly show `—`, not an invented answer.
- **AC-R004:** Tool sections contain names/counts and no raw tool payload.
- **AC-R005:** Recalled evidence is distinguishable from deterministic database metadata.
- **AC-R006:** Missing or partial recall is visible in a `Recall status` note and does not reduce the session count.

## References

- `./run-today-and-yesterday-discovery-spec.md`
- `./run-today-and-yesterday-report-spec.md`
- `../.github/prompts/general/run-all-goals/run-today-and-yesterday.prompt.md`
- `../plans/run-today-and-yesterday-consolidated-plan.md`
