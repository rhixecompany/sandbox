---
agent: "agent"
description: "Hermes-equivalent: produce a Feature Implementation Plan from a Feature PRD."
---

## Goal

Turn a feature PRD into an implementation plan that an engineering team can execute.

## Context

- Use when the feature PRD is already available.
- Focus on architecture, data flow, API shape, and delivery considerations.
- Keep the plan grounded in the source PRD and any technical notes.
- Do not omit deployment or security concerns.

## Inputs

- Feature PRD path: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`
- Optional: `technical-breakdown.md`, implementation constraints

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`

## Rules

1. Keep the plan tied to the PRD requirements.
2. Include architecture, schema, API, frontend, deployment, security, and performance.
3. Use Mermaid where diagrams add clarity.
4. Make the API section concrete with request and response shapes.
5. Surface migration strategy and CI/CD considerations explicitly.
6. Keep the document easy to hand to an engineer.

## Phases

> ### Phase 1: Analyze the PRD
> **Goal:** extract the technical work implied by the feature.

> **Full content:** `templates/hermes-breakdown-feature-implementation/phases.md`

## Actions Summary

1. Read and analyze the feature PRD.
2. Draft the implementation plan structure.
3. Add architecture, schema, API, UI, and delivery notes.
4. Review the draft for completeness and clarity.


## Template References

Templates in `templates/hermes-breakdown-feature-implementation/`:
- `phases.md`
