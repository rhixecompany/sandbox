---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "update-docs-on-code-change"
title: "Update Docs on Code Change"
description: "Comprehensive prompt for synchronizing documentation whenever code changes modify behavior, APIs, or workflows."
trigger: /update-docs-on-code-change
tags:
  - hermes
  - documentation
  - sync
  - code-change
  - readme
  - api-docs
---

## Goal
Use when "Comprehensive prompt for synchronizing documentation whenever code changes modify behavior, APIs, or workflows." to accomplish the associated tasks and objectives.


## Description

Detect when code changes require documentation updates and ensure README, API docs, config docs, changelogs, and examples remain synchronized.

## Context

Use this prompt whenever application code, scripts, APIs, configuration, or public interfaces are changed.

## Skills Required

- Change-impact analysis across code and documentation
- Documentation synchronization and migration guide authoring
- Example and reference validation

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Impact Analyzer | Maps code changes to required documentation updates | Always |
| Docs Updater | Executes README/API/config/changelog updates | Always |
| Verification Reviewer | Confirms docs and examples remain accurate | Final validation |

## Personas

- Impact Analyzer: Finds every doc affected by behavior or interface changes.
- Docs Updater: Produces precise updates in standard documentation locations.
- Verification Reviewer: Ensures no stale references or broken examples remain.

## Rules

- Update docs in the same change as code whenever behavior or interfaces change.
- Always evaluate README impact for new features, setup, config, and CLI changes.
- Sync API docs for endpoint/signature/auth changes.
- Update examples and migration guidance for breaking or deprecated behavior.
- Keep changelog entries structured and user-focused.

## Phases

> ### Phase 1: Trigger and Scope Detection
> ### Phase 2: Documentation Synchronization

> **Full content:** `templates/update-docs-on-code-change/phases.md`

## Steps

1. Evaluate code changes against documentation trigger conditions.
2. Build a file-level list of required doc updates.
3. Update README, API docs, configuration docs, and examples.
4. Add changelog and migration notes where applicable.
5. Verify links, snippet correctness, and public-facing clarity.

## Tasks

- Task 1.1 — Detect documentation-triggering code changes and classify impact.
- Task 1.2 — Update required documentation files and sections.
- Task 1.3 — Synchronize code examples, API references, and configuration docs.
- Task 1.4 — Add changelog and migration guidance for breaking changes.
- Task 1.5 — Validate documentation completeness and consistency.

## Subtasks

- Subtask 1.1.1 — Map each changed public symbol or behavior to a doc target.
- Subtask 1.2.1 — Update README features, setup, CLI, and configuration sections as needed.
- Subtask 1.3.1 — Confirm snippets match current signatures and imports.
- Subtask 1.4.1 — Mark deprecated behavior and provide migration steps.
- Subtask 1.5.1 — Check links and note any deferred documentation debt.

## Actions Summary

1. Detect doc-impacting code changes.
2. Synchronize all affected docs in the same change.
3. Validate examples and references.
4. Deliver release-ready documentation alignment.


## Template References

Templates in `templates/update-docs-on-code-change/`:
- `phases.md`
