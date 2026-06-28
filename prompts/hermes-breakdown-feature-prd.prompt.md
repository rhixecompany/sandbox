---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Hermes Breakdown Feature Prd
name: hermes-breakdown-feature-prd
description: "Hermes-equivalent: create a Feature PRD from a feature idea or parent epic."
tags: []
---

## Goal

Produce a feature PRD that is ready to hand off for implementation planning.

## Context

- Use when the user needs a structured `prd.md` for a single feature.
- Base the PRD on a parent epic or a clearly stated feature idea.
- Keep the content concrete and user-facing.
- Do not add implementation detail beyond what is needed for the PRD.

## Inputs

- Parent epic path or feature idea text

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`

## Rules

1. Include the feature name and the epic reference.
2. Describe the problem, solution, and intended impact.
3. Write user stories in a clear, testable form.
4. Include functional and non-functional requirements.
5. Include acceptance criteria using checklist items or Given/When/Then.
6. List out-of-scope items and dependencies.

## Phases

> ### Phase 1: Understand the feature
> **Goal:** capture the feature idea and the parent epic context.

> **Full content:** `templates/hermes-breakdown-feature-prd/phases.md`

## Actions Summary

1. Read the feature idea and epic context.
2. Draft the PRD structure and content.
3. Add stories, requirements, and acceptance criteria.
4. Verify completeness and file path.


## Template References

Templates in `templates/hermes-breakdown-feature-prd/`:
- `phases.md`
