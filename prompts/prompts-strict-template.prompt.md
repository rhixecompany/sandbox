---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "prompts-strict-template"
title: "Prompts Strict Template"
description: "Comprehensive prompt for enforcing strict .prompt.md template structure and formatting rules."
trigger: /prompts-strict-template
tags: []
  - hermes
  - prompts
  - template
  - enforce
  - format
---

## Goal
Use when "Comprehensive prompt for enforcing strict .prompt.md template structure and formatting rules." to accomplish the associated tasks and objectives.


## Description

Normalize and validate prompt markdown files so they follow the repository's strict required structure, section order, phase table format, and task numbering conventions.

## Context

Use this prompt when creating, editing, reviewing, or repairing files that match .prompt.md naming conventions.

## Skills Required

- Markdown structure and lint-aware formatting
- Template compliance verification
- Controlled normalization without intent loss

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Template Enforcer | Applies required section order and presence checks | Always |
| Structure Validator | Validates phase tables and numbering syntax | Always |
| Intent Preserver | Prevents semantic drift during normalization | Existing prompt migrations |

## Personas

- Template Enforcer: Treats required section order as non-negotiable.
- Structure Validator: Rejects malformed phases, tables, and numbering patterns.
- Intent Preserver: Keeps original prompt purpose and guidance intact.

## Rules

- Ensure all required top-level sections exist and are non-empty.
- Keep required section order exact.
- Include at least one phase with required Field/Details table and mandatory rows.
- Enforce Task N.x and Subtask N.x.y numbering patterns.
- Preserve source intent and wording as much as possible.

## Phases

> ### Phase 1: Structural Intake
> ### Phase 2: Template Normalization

> **Full content:** `templates/prompts-strict-template/phases.md`

## Steps

1. Parse prompt content and compare with strict template requirements.
2. Add missing sections in exact required order.
3. Normalize phase formatting and table rows.
4. Correct Tasks and Subtasks numbering syntax.
5. Validate final structure and preserve original intent.

## Tasks

- Task 1.1 — Detect missing or out-of-order top-level sections.
- Task 1.2 — Ensure Phase sections include required table schema and rows.
- Task 1.3 — Normalize Tasks and Subtasks numbering patterns.
- Task 1.4 — Preserve source intent while restructuring content.
- Task 1.5 — Produce final compliance validation output.

## Subtasks

- Subtask 1.1.1 — Check exact sequence of all 11 required sections.
- Subtask 1.2.1 — Verify Goal, Inputs, Outputs, and Validation rows exist.
- Subtask 1.3.1 — Rewrite list entries to Task N.x and Subtask N.x.y format.
- Subtask 1.4.1 — Retain meaningful prompt semantics and role guidance.
- Subtask 1.5.1 — Confirm no new markdown diagnostics were introduced.

## Actions Summary

1. Detect structural drift.
2. Normalize to strict template.
3. Validate numbering and phase tables.
4. Deliver compliance-preserving updates.


## Template References

Templates in `templates/prompts-strict-template/`:
- `phases.md`
