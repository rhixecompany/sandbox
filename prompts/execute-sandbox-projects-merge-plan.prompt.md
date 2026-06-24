---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "execute-sandbox-projects-merge-plan"
title: "Sandbox Projects Merge Plan"
description: "Execute the Sandbox Projects Merge Plan plan."
trigger: /execute-sandbox-projects-merge-plan
tags: []
  - hermes
  - plan
  - execute
---

## Goal
Execute the plan at `.hermes/plans/sandbox-projects-merge-plan.md`.

## Context
This prompt loads and executes the consolidated plan document.

## Execution
1. Load the plan from `.hermes/plans/sandbox-projects-merge-plan.md`
2. Follow the plan's phases and requirements
3. Report progress and completion
