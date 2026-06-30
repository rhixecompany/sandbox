---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "execute-acpx-agents-feature-specs"
title: "Acpx Agents Feature Specs"
description: "Execute the Acpx Agents Feature Specs plan."
trigger: execute-acpx-agents-feature-specs
tags:
  - agents
  - ai-assistant
  - execution
  - frontend
  - prompts
  - specification
  - typescript
  - hermes
  - plan
  - execute
metadata:
  hermes:
    related_skills: []
    tags:
    - execute-acpx-agents-feature-specs.prompt

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - execute-acpx-agents-feature-specs.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - execute-acpx-agents-feature-specs.prompt

## Goal
Execute the plan at `.hermes/plans/acpx-agents-feature-specs.md`.

## Context
This prompt loads and executes the consolidated plan document.

## Execution
1. Load the plan from `.hermes/plans/acpx-agents-feature-specs.md`
2. Follow the plan's phases and requirements
3. Report progress and completion

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
