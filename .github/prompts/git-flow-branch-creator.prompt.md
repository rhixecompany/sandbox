---
name: git-flow-branch-creator
title: Git Flow Branch Creator
description: Intelligent Git Flow branch creator that analyzes git status/diff and creates appropriate
  branches following the nvie Git Flow branching model.
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
  - git
  - linting
  - ml
  - prompts
  - specification
  - typescript
trigger: /git-flow-branch-creator
---

## GoalIntelligent Git Flow branch creator that analyzes git status/diff and creates appropriate branches following the nvie Git Flow branching model.## ContextUse when you need to work on the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## Template ReferencesDetailed templates in `templates/git-flow-branch-creator/`:- `legacy_prompt_details.md`