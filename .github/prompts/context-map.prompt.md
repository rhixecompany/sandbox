---
name: context-map
title: Context Map
description: Build a dependency and reference map before making changes so implementation starts
  from the right files.
version: 2.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - codemap
formatter: default
plan: ''
dependencies:
  - skill:codemap
tags:
  - audit
  - frontend
  - prompts
  - specification
  - testing
  - typescript
trigger: /context-map
metadata:
  hermes:
  related_skills:
  - codemap
---

# context-map> Build a dependency-aware context map before implementation begins.## GoalBuild a dependency and reference map before making changes so implementation starts from the right files.## Context- Use when the task needs a safe pre-change inventory- Focus on direct dependencies, related tests, and nearby patterns- Keep the map concrete and file-driven- Do not proceed to implementation until the map is reviewed## Inputs- Task description- Optional target area, feature, or bug report- Optional constraints or known files## Outputs- A context map with files to modify, dependencies, tests, and reference patterns- A short risk assessment- Present the context map as a Markdown table with columns: File | Role (modify/dependency/test) | Notes- Follow with a bulleted risk assessment of 3-5 items max## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)1. If the task description is too vague to identify specific files, stop and ask the user to clarify the target area before proceeding to Phase 12. Search for the files directly related to the task3. Identify imports, exports, and other dependencies4. Identify the likely test files5. If no related test files are found, explicitly state "No related tests identified" in the map and flag it as a risk item6. Find 2-3 existing code examples in the codebase that demonstrate the same pattern (for example, same hook usage, same module export style) that the new change should follow7. Call out breaking-change risks clearly8. Stop after mapping; do not implement yet## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill | Purpose || --- | --- || `codemap` | Codebase discovery and dependency mapping (loads symbol tables, dependency trees, and cross-file references) |## Phases> ### Phase 1: Discover the scope>> **Goal:** find the files and relationships that matter.>> **Full content:** `templates/context-map/phases.md`## Actions Summary1. **Phase 1:** Discover the scope2. **Phase 2:** Map dependencies, tests, and reference patterns3. **Phase 3:** Record the risks and review completeness4. **Phase 4:** Return the context map and stop## Template ReferencesTemplates in `templates/context-map/`:- `phases.md`