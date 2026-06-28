---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "execute-IMPLEMENTATION_PLAN"
title: "Implementation_Plan"
description: "Execute the Implementation_Plan plan."
trigger: /execute-IMPLEMENTATION_PLAN
tags:
  - hermes
  - plan
  - execute
---

## Goal
Execute the plan at `.hermes/plans/IMPLEMENTATION_PLAN.md`.

## Context
This prompt loads and executes the consolidated plan document.

## Execution
1. Load the plan from `.hermes/plans/IMPLEMENTATION_PLAN.md`
2. Follow the plan's phases and requirements
3. Report progress and completion
