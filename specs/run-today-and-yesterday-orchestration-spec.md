---
name: run-today-and-yesterday-orchestration-spec
sidebar_position: 20
title: "Run Today and Yesterday — Orchestration"
description: "Define the single-plan orchestration, triage, dedupe, and verification workflow for the two-day session report."
version: 1.0.0
author: Alexa
license: MIT
tags: [spec, orchestration, plans, triage, dedupe, verification]
status: completed
---

# Run Today and Yesterday — Orchestration Specification

## Goal

Orchestrate discovery, per-session recall, report generation, and artifact verification through one consolidated implementation plan. The workflow must list and triage existing artifacts, deduplicate overlapping requirements into the four canonical specs, and never create a competing plan.

## Artifact inventory and triage

Before execution, enumerate:

- `./specs/`
- `./plans/`
- `./.github/prompts/general/run-all-goals/`
- The current report and its generator.

Classify each relevant item as **canonical input**, **supporting reference**, **historical evidence**, **duplicate/overlap**, **missing**, or **out of scope**. Preserve historical artifacts; do not delete or rewrite unrelated plans/specs. Consolidate only this request's requirements into:

1. `run-today-and-yesterday-discovery-spec.md`
2. `run-today-and-yesterday-recall-spec.md`
3. `run-today-and-yesterday-report-spec.md`
4. `run-today-and-yesterday-orchestration-spec.md`

The single implementation plan is `../plans/run-today-and-yesterday-consolidated-plan.md`. Do not create another plan for this request.

## Orchestration requirements

- **ORCH-001:** Read the generated report baseline before executing the plan.
- **ORCH-002:** Execute phases in dependency order: inventory → discovery → recall → report → spec/plan/prompt verification.
- **ORCH-003:** Parallelize only independent read-only inventory or static checks; serialize report writes and final verification.
- **ORCH-004:** Stop on failed gates and record the exact command, exit code, and blocker.
- **ORCH-005:** Keep the report path, session count, ID list, and WAT boundaries consistent across all artifacts.
- **ORCH-006:** Verify prompt/spec/plan links and frontmatter before claiming completion.
- **ORCH-007:** Do not call live providers, write Hermes config, mutate profiles, access secrets, commit, push, or perform external sync.
- **ORCH-008:** Preserve fresh evidence separately from historical completion claims.

## Acceptance criteria

- **AC-O001:** The artifact inventory is present or its missing-source blocker is explicit.
- **AC-O002:** Exactly four new canonical specs and exactly one new consolidated plan are linked.
- **AC-O003:** The execution prompt and orchestration prompt both reference the report and plan.
- **AC-O004:** The report and plan agree on WAT window and scope.
- **AC-O005:** Static, syntax, link, and secret-pattern checks pass, or the result records a real blocker.
- **AC-O006:** The final handoff names all created artifacts and does not claim unperformed external actions.

## References

- `./run-today-and-yesterday-discovery-spec.md`
- `./run-today-and-yesterday-recall-spec.md`
- `./run-today-and-yesterday-report-spec.md`
- `../plans/run-today-and-yesterday-consolidated-plan.md`
- `../.github/prompts/general/run-all-goals/run-today-and-yesterday.prompt.md`
- `../.github/prompts/general/run-all-goals/orchestrate-run-today-and-yesterday.prompt.md`
- `../.github/prompts/general/run-all-goals/results/run-today-and-yesterday-report-2026-09-14.md`
