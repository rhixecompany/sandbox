---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Hermes Breakdown Plan
name: hermes-breakdown-plan
description: "Hermes-equivalent: generate a GitHub project plan from PRD, technical breakdown, implementation plan, and test strategy artifacts."
tags:
  - ai-assistant
  - frontend
  - generator
  - git
  - planning
  - prompts
  - specification
  - testing
  - typescript
  - agile
  - ai-assistant
  - ci-cd
  - documentation
  - github
  - markdown
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - hermes-breakdown-plan.prompt

trigger: hermes-breakdown-plan

---
metadata:
  hermes:
    related_skills: []
    tags:
    - hermes-breakdown-plan.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - hermes-breakdown-plan.prompt

## Goal

Generate a project plan that turns feature and epic inputs into an execution-ready planning package.

## Context

- Use when the user needs a Project Plan plus issue-creation support.
- Prefer concise, actionable language.
- Keep the plan aligned with the provided PRD, technical breakdown, implementation plan, and test strategy.
- Do not invent scope that is not supported by the source artifacts.

## Inputs

- Epic PRD path: `/docs/ways-of-work/plan/{epic-name}/epic.md`
- Feature PRD path: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`
- Optional: `technical-breakdown.md`, `implementation-plan.md`, `test-strategy.md`

## Outputs

- Project Plan markdown at `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`
- Issue Creation Checklist at `/docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md`
- GitHub issue templates for Epic, Feature, Story, Enabler, and Test work items
- A minimal GitHub Actions snippet for issue creation

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


1. Use the provided artifacts as the only source of scope.
2. Keep outputs concise and directly usable.
3. Use Mermaid diagrams for hierarchy and dependency views.
4. Include practical issue templates, not generic prose.
5. Create backup copies before overwriting existing outputs.
6. Split large outputs into companion files if a single file would exceed the size limit.

## Phases

> ### Phase 1: Parse the source artifacts
> **Goal:** identify the epic, feature, and supporting planning inputs.

> **Full content:** `templates/hermes-breakdown-plan/phases.md`

## Actions Summary

1. Read the source planning artifacts.
2. Derive the project scope and hierarchy.
3. Write the project plan and issue checklist.
4. Add the minimal automation snippet.
5. Verify the outputs and backup state.


## Template References

Templates in `templates/hermes-breakdown-plan/`:
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
