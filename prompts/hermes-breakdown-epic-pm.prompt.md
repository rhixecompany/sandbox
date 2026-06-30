---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Hermes Breakdown Epic Pm
name: hermes-breakdown-epic-pm
description: "Hermes-equivalent: author a complete Epic PRD from a high-level epic idea or request."
tags:
  - ai-assistant
  - frontend
  - ml
  - planning
  - prompts
  - specification
  - typescript
  - agile
  - ai-assistant
  - authentication
  - documentation
  - planning
  - security
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - hermes-breakdown-epic-pm.prompt

trigger: hermes-breakdown-epic-pm

---
metadata:
  hermes:
    related_skills: []
    tags:
    - hermes-breakdown-epic-pm.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - hermes-breakdown-epic-pm.prompt

## Goal

Produce a complete Epic PRD that is ready for downstream feature planning.

## Context

- Use when the user provides an epic idea, short brief, or high-level request.
- Keep the output measurable, concise, and aligned to business value.
- Ask a short clarifying list if the input is missing key details.
- Do not drift into implementation detail.

## Inputs

- Epic idea text or short brief
- Optional target metrics or constraints

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/epic.md`

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


1. Include problem, solution, and impact.
2. Define user personas and high-level journeys.
3. Include functional and non-functional business requirements.
4. Include success metrics and out-of-scope items.
5. Estimate business value in a clear, comparable way.
6. Ask for clarification when the epic is underspecified.

## Phases

> ### Phase 1: Understand the epic
> **Goal:** capture the idea, audience, and business objective.

> **Full content:** `templates/hermes-breakdown-epic-pm/phases.md`

## Actions Summary

1. Read the epic brief.
2. Draft the Epic PRD structure and content.
3. Add journeys, requirements, metrics, and scope limits.
4. Verify completeness and file path.


## Template References

Templates in `templates/hermes-breakdown-epic-pm/`:
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
