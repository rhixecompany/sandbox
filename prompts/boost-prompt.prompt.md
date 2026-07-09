---
license: MIT
author: Hermes Agent
version: 1.0.0
title: boost-prompt
name: boost-prompt
trigger: /boost-prompt
description: >-
  Interactive prompt refinement workflow: interrogates scope, deliverables, and constraints, then copies final markdown to clipboard using Joyride.
tags:
  - frontend
  - markdown
  - ml
  - prompts
  - typescript
  - workflow
  - hermes
  - copilot
  - writing-skills
  - refinement
  - joyride
dependencies:
  - skill:writing-skills
  - skill:writing-plans
  - skill:joyride
  - skill:context-map
  - skill:prompt-engineering
skills:
  - writing-skills — Crafting and optimizing prompts and instructions
  - writing-plans — Structured prompt authoring
---

# boost-prompt

> Interactive prompt refinement workflow: interrogates scope, deliverables, constraints; copies final markdown to clipboard; never writes code.

## Goal

Iteratively refine a user's task prompt into a high-quality, detailed prompt through interrogation, exploration, and structured formatting.

## Context

Use when you need to improve a draft prompt before submitting it to an AI system. Requires the Joyride VS Code extension for clipboard operations. This prompt does NOT write code - it only refines prompts.

**Critical rules (must appear within the first 15% of execution):**
- DO NOT WRITE ANY CODE - this is a prompt refinement workflow only
- Always ask clarifying questions before finalizing the prompt
- Copy the final markdown to clipboard using Joyride after each revision

## Inputs

- A draft prompt from the user
- The current workspace context (for project exploration)
- Optional constraints or specific requirements

## Outputs

- An improved, structured prompt in markdown format
- Prompt copied to system clipboard via Joyride
- Verification that the user is satisfied with the result

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


1. **No code** - DO NOT write any code; this workflow is for prompt refinement only
2. **Interrogate first** - Ask specific questions to understand scope, objectives, deliverables, and constraints before refining
3. **Explore the project** - Use available tools to understand the codebase and task context
4. **Map context first** - Run `/context-map` before deep prompt refinement so file and dependency context is explicit
5. **Structured output** - Organize the prompt into clear sections or steps
6. **Clipboard delivery** - Use Joyride to copy the final markdown to the system clipboard
7. **Iterate** - After delivering, ask the user if they want changes or additions

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#boost-prompt)

| Skill | Purpose |
| --- | --- |
| `context-map` | Preflight map of relevant files and references before refinement |
| `writing-skills` | Crafting and optimizing prompts and instructions |
| `writing-plans` | Structured prompt authoring and organization (section layout, phase flow) |

## Tools Required

> **Requirement**: VS Code Joyride extension installed and active
> - Install from VS Code Extensions marketplace: search "Joyride"

> **Full content:** `templates/boost-prompt/tools_required.md`

## Phases

> ### Phase 1: Interrogate
> **Goal:** Understand the task scope, objectives, deliverables, and constraints.

> **Full content:** `templates/boost-prompt/phases.md`

## Actions Summary

1. Interrogate the user about scope, deliverables, and constraints
2. Explore the project workspace for context
3. Refine the prompt into structured markdown
4. Copy to clipboard via Joyride
5. Present in chat
6. Ask for feedback and iterate if needed


## Template References

Templates in `templates/boost-prompt/`:
- `phases.md`
- `tools_required.md`
