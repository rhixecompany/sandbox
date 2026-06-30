---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "documentation"
title: "Documentation"
description: "Comprehensive documentation prompt aligned to repository documentation standards."
trigger: documentation
tags:
  - api
  - architecture
  - documentation
  - frontend
  - markdown
  - ml
  - prompts
  - skills
  - typescript
  - hermes
  - documentation
metadata:
  hermes:
    related_skills: []
    tags:
    - documentation.prompt

---
metadata:
  hermes:
    related_skills: []
    tags:
    - documentation.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - documentation.prompt

## Goal
Use when "Comprehensive documentation prompt aligned to repository documentation standards." to accomplish the associated tasks and objectives.


## Description

Create and maintain documentation that is accurate, complete, and updated in the same change set as code updates.

## Context

Use this prompt when writing or updating markdown docs, TSDoc comments, API docs, README sections, architecture notes, or doc examples.

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#documentation)

- Technical writing for developers and maintainers
- API and architecture documentation design
- Consistency and change-tracking discipline

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Docs Writer | Drafts and restructures docs for clarity | Always |
| API Documenter | Ensures endpoint docs are accurate and complete | API or SDK updates |
| Reviewer | Checks doc drift and missing sections | Final verification |

## Personas

- Docs Writer: Produces concise, accurate docs with practical examples.
- API Documenter: Maps implementation to endpoint and schema documentation.
- Reviewer: Rejects stale or incomplete docs that diverge from code behavior.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


- Update documentation in the same PR or change as code modifications.
- Use TSDoc for non-trivial types, functions, hooks, and component props.
- Ensure README setup and usage instructions remain executable.
- Keep examples current and aligned with current APIs and config.
- Validate internal links and remove obsolete references.

## Phases

> ### Phase 1: Documentation Impact Analysis
> ### Phase 2: Authoring and Synchronization

> **Full content:** `templates/documentation/phases.md`

## Steps

1. Identify code changes that alter behavior, APIs, setup, or configuration.
2. Map each change to required documentation updates.
3. Update README, API docs, and relevant architecture references.
4. Refresh examples, TSDoc, and configuration documentation.
5. Validate links, terminology consistency, and maintenance readiness.

## Tasks

- Task 1.1 — Build a documentation impact matrix for all relevant code changes.
- Task 1.2 — Update user-facing docs such as README and usage guides.
- Task 1.3 — Update developer-facing docs including TSDoc and architecture notes.
- Task 1.4 — Verify examples, links, and API references for correctness.
- Task 1.5 — Publish a concise change summary of documentation updates.

## Subtasks

- Subtask 1.1.1 — Identify public API and configuration surface changes.
- Subtask 1.2.1 — Revise setup, usage, and troubleshooting sections when needed.
- Subtask 1.3.1 — Add or refresh TSDoc on complex types and hooks.
- Subtask 1.4.1 — Statistically validate snippets for syntax and symbol accuracy.
- Subtask 1.5.1 — Note any known doc debt and planned follow-ups.

## Actions Summary

1. Analyze doc impact.
2. Update all affected docs in the same change.
3. Validate correctness and link integrity.
4. Deliver a maintainable, synchronized documentation set.


## Template References

Templates in `templates/documentation/`:
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
