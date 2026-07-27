---
name: refactor-plan
title: Refactor Plan
description: Plan a multi-file refactor with proper sequencing and rollback steps
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - terminal
  - file
scripts: []
skills: []
formatter: default
plan: ''
tags:
  - ml
  - prompts
  - refactoring
  - specification
  - typescript
trigger: /refactor-plan
---

## GoalPlan a multi-file refactor with proper sequencing and rollback steps.## ContextUse when you need to work on the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## Refactor Goal{{refactor_description}}## Instructions1. Search the codebase to understand current state2. Identify all affected files and their dependencies3. Plan changes in a safe sequence (types first, then implementations, then tests)4. Include verification steps between changes5. Consider rollback if something fails## Output Format```markdown## Refactor Plan: [title]> [Brief description of how things work now]> [Brief description of how things will work after]> **Full content:** `templates/refactor-plan/refactor_plan_title.md`## Template ReferencesTemplates in `templates/refactor-plan/`:- `phases.md`- `refactor_plan_title.md`