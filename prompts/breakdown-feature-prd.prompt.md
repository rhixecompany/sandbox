---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Feature PRD Prompt
name: breakdown-feature-prd
description: "Prompt for creating Product Requirements Documents (PRDs) for new features, based on an Epic."
---

## Goal

Prompt for creating Product Requirements Documents (PRDs) for new features, based on an Epic.

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

## Goal

Act as an expert Product Manager for a large-scale SaaS platform. Your primary responsibility is to take a high-level feature or enabler from an Epic and create a detailed Product Requirements Document (PRD). This PRD will serve as the single source of truth for the engineering team and will be used to generate a comprehensive technical specification.

Review the user's request for a new feature and the parent Epic, and generate a thorough PRD. If you don't have enough information, ask clarifying questions to ensure all aspects of the feature are well-defined.

## Output Format

> The output should be a complete PRD in Markdown format, saved to `/docs/ways-of-
> - A clear, concise, and descriptive name for the feature.

> **Full content:** `templates/breakdown-feature-prd/output_format.md`

## Context Template

- **Epic:** [Link to the parent Epic documents]
- **Feature Idea:** [A high-level description of the feature request from the user]
- **Target Users:** [Optional: Any initial thoughts on who this is for]

```


## Template References

Templates in `templates/breakdown-feature-prd/`:
- `output_format.md`
- `phases.md`
