---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "execute-plan-debugger"
title: "Copilot Instructions Generator"
description: "Execute Copilot Instructions Generator"
trigger: /execute-plan-debugger
tags:
  - ai-assistant
  - debugging
  - execution
  - generator
  - prompts
  - hermes
  - plan
  - execute
dependencies:
  - skill:plan:debugger.md
---

## Goal
Execute the plan at `.hermes/plans/debugger.md`.

## Execution
1. Load the plan from `.hermes/plans/debugger.md`
2. Follow the plan's phases and instructions
3. Report progress and completion
