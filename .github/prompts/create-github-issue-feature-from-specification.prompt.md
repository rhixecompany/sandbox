---
name: create-github-issue-feature-from-specification
title: Create GitHub Issue from Specification
description: Create GitHub Issue for feature request from specification file using feature_request.yml
  template.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - web
scripts: []
skills: []
formatter: default
plan: ''
tags:
  - generator
  - git
  - ml
  - prompts
  - specification
  - typescript
  - generator
  - git
  - ml
  - prompts
  - specification
  - typescript
trigger: /create-github-issue-feature-from-specification
---

## GoalCreate GitHub Issue for feature request from specification file using feature_request.yml template.## ContextUse when you need to work on the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## Process1. Analyze specification file to extract requirements2. Check existing issues using `search_issues`3. Create new issue using `create_issue` or update existing with `update_issue`4. Use `feature_request.yml` template (fallback to default)## Requirements- Single issue for the complete specification- Clear title identifying the specification- Include only changes required by the specification- Verify against existing issues before creation## Issue Content- Title: Feature name from specification- Description: Problem statement, proposed solution, and context- Labels: feature, enhancement (as appropriate)## Template ReferencesTemplates in `templates/create-github-issue-feature-from-specification/`:- `phases.md`