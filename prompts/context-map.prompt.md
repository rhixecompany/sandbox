---
license: MIT
author: Hermes Agent
version: 1.0.0
title: context-map
name: context-map
trigger: /context-map
description: >-
  Build a dependency and reference map before making changes so implementation starts from the right files.
tags:
  - audit
  - frontend
  - prompts
  - specification
  - testing
  - typescript
  - hermes
  - copilot
  - analysis
  - dependencies
  - planning
dependencies:
  - skill:codemap
skills:
  - codemap — Codebase discovery and dependency mapping
---

# context-map

> Build a dependency-aware context map before implementation begins.

## Goal

Build a dependency and reference map before making changes so implementation starts from the right files.

## Context

- Use when the task needs a safe pre-change inventory
- Focus on direct dependencies, related tests, and nearby patterns
- Keep the map concrete and file-driven
- Do not proceed to implementation until the map is reviewed

## Inputs

- Task description
- Optional target area, feature, or bug report
- Optional constraints or known files

## Outputs

- A context map with files to modify, dependencies, tests, and reference patterns
- A short risk assessment
- Present the context map as a Markdown table with columns: File | Role (modify/dependency/test) | Notes
- Follow with a bulleted risk assessment of 3-5 items max

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


1. If the task description is too vague to identify specific files, stop and ask the user to clarify the target area before proceeding to Phase 1
2. Search for the files directly related to the task
3. Identify imports, exports, and other dependencies
4. Identify the likely test files
5. If no related test files are found, explicitly state "No related tests identified" in the map and flag it as a risk item
6. Find 2-3 existing code examples in the codebase that demonstrate the same pattern (for example, same hook usage, same module export style) that the new change should follow
7. Call out breaking-change risks clearly
8. Stop after mapping; do not implement yet

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#context-map)

| Skill | Purpose |
| --- | --- |
| `codemap` | Codebase discovery and dependency mapping (loads symbol tables, dependency trees, and cross-file references) |

## Phases

> ### Phase 1: Discover the scope
> **Goal:** find the files and relationships that matter.

> **Full content:** `templates/context-map/phases.md`

## Actions Summary

1. **Phase 1:** Discover the scope
2. **Phase 2:** Map dependencies, tests, and reference patterns
3. **Phase 3:** Record the risks and review completeness
4. **Phase 4:** Return the context map and stop


## Template References

Templates in `templates/context-map/`:
- `phases.md`
