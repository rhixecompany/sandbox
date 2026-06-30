---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Optimize Agentsmd
name: optimize-agentsmd
description: "optimize-agentsMd.prompt"
tags:
  - agents
  - ml
  - performance
  - prompts
  - specification
  - typescript
  - workflow
  - agents
  - documentation
  - markdown
  - optimization
  - orchestration
  - performance
  - planning
  - specification
  - workflow
metadata:
  hermes:
    related_skills: []
    tags:
    - optimize-agentsmd.prompt

trigger: optimize-agentsmd

---
metadata:
  hermes:
    related_skills: []
    tags:
    - optimize-agentsmd.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - optimize-agentsmd.prompt

## Goal

Use this prompt to handle the optimize agentsmd workflow.

## Context

Use when you need to optimize agentsmd for the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note summarizing what was changed, assumptions made, and any missing sources.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the chat response structured, deterministic, and easy to act on; if the artifact is large, provide a concise summary plus the file update.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear and non-blocking, state the assumption explicitly; if it blocks correctness, ask for clarification or mark it as "not present".

## Phases

The outer phases map to the source prompt as follows: Phase 1 Intake = Phase 1, Phase 2 Execute = Phases 2-3, Phase 3 Verify = Phase 4, Phase 4 Hand off = final presentation.

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Produce the AGENTS.md rewrite/update described in the source prompt details; do not constrain scope when full coverage updates are required.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Source Prompt Details
```text
## Plan: Comprehensive AGENTS.md for Agentic Coding in Banking Repo

> **TL;DR:** I will analyze the codebase and existing documentation to produce a d
> ### Phase 1: Discovery & Research

> **Full content:** `templates/optimize-agentsMd/plan_comprehensive_agentsmd_fo.md`

## Template References

Detailed templates in `templates/optimize-agentsMd/`:
- `plan_comprehensive_agentsmd_fo.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
