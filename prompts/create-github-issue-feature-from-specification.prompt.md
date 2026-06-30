---
toolsets:
  - search/codebase
  - search
  - github
  - create_issue
  - search_issues
  - update_issue
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create GitHub Issue from Specification
name: create-github-issue-feature-from-specification
description: "Create GitHub Issue for feature request from specification file using feature_request.yml template."
tags:
  - generator
  - git
  - ml
  - prompts
  - specification
  - typescript
  - ci-cd
  - documentation
  - generator
  - github
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - create-github-issue-feature-from-specification.prompt

trigger: create-github-issue-feature-from-specification

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - create-github-issue-feature-from-specification.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - create-github-issue-feature-from-specification.prompt

## Goal

Create GitHub Issue for feature request from specification file using feature_request.yml template.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Process

1. Analyze specification file to extract requirements
2. Check existing issues using `search_issues`
3. Create new issue using `create_issue` or update existing with `update_issue`
4. Use `feature_request.yml` template (fallback to default)

## Requirements

- Single issue for the complete specification
- Clear title identifying the specification
- Include only changes required by the specification
- Verify against existing issues before creation

## Issue Content

- Title: Feature name from specification
- Description: Problem statement, proposed solution, and context
- Labels: feature, enhancement (as appropriate)


## Template References

Templates in `templates/create-github-issue-feature-from-specification/`:
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
