---
name: create-github-issues-for-unmet-specification-requirements
title: Create GitHub Issues for Unmet Specification Requirements
description: Create GitHub Issues for unimplemented requirements from specification files using
  feature_request.yml template.
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
  - frontend
  - generator
  - git
  - ml
  - prompts
  - specification
  - typescript
trigger: /create-github-issues-for-unmet-specification-requirements
---

## GoalCreate GitHub Issues for unimplemented requirements from specification files using feature_request.yml template.## ContextUse when you need to work on the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## Process1. Analyze specification file to extract all requirements2. Check codebase implementation status for each requirement3. Search existing issues using `search_issues` to avoid duplicates4. Create new issue per unimplemented requirement using `create_issue`5. Use `feature_request.yml` template (fallback to default)## Requirements- One issue per unimplemented requirement from specification- Clear requirement ID and description mapping- Include implementation guidance and acceptance criteria- Verify against existing issues before creation## Issue Content- Title: Requirement ID and brief description- Description: Detailed requirement, implementation method, and context- Labels: feature, enhancement (as appropriate)## Implementation Check- Search codebase for related code patterns- Check related specification files in `/spec/` directory- Verify requirement isn't partially implemented## Template ReferencesTemplates in `templates/create-github-issues-for-unmet-specification-requirements/`:- `phases.md`