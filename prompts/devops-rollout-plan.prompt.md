---
toolsets: ["codebase", "terminalCommand", "search", "githubRepo"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: DevOps Rollout Plan Generator
name: devops-rollout-plan
description: "Generate comprehensive rollout plans with preflight checks, step-by-step deployment, verification signals, rollback procedures, and communication plans for infrastructure and application changes"
tags:
  - deployment
  - generator
  - ml
  - prompts
  - specification
  - typescript
  - deployment
  - devops
  - documentation
  - planning
  - specification
---

## Goal

Generate comprehensive rollout plans with preflight checks, step-by-step deployment, verification signals, rollback procedures, and communication plans for infrastructure and application changes.

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

## Input Requirements

> Gather these details before generating the plan:
> ### Change Description

> **Full content:** `templates/devops-rollout-plan/input_requirements.md`

## Output Format

> Generate a structured rollout plan with these sections:
> ### 1. Executive Summary

> **Full content:** `templates/devops-rollout-plan/output_format.md`

## Plan Customization

Adapt based on:

- **Infrastructure Type**: Kubernetes, VMs, serverless, databases
- **Risk Level**: Low (simplified), medium (standard), high (additional gates)
- **Change Type**: Code deployment, infrastructure, configuration, data migration
- **Environment**: Production (full plan), staging (simplified), development (minimal)

## Remember

- Always have a tested rollback plan
- Communicate early and often
- Monitor metrics, not just logs
- Document everything
- Learn from each deployment
- Never deploy on Friday afternoon (unless critical)
- Never skip verification steps
- Never assume "it should work"


## Template References

Templates in `templates/devops-rollout-plan/`:
- `input_requirements.md`
- `output_format.md`
- `phases.md`
