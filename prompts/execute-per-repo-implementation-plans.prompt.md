---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "execute-per-repo-implementation-plans"
title: "Per Repo Implementation Plans"
description: "Execute the Per Repo Implementation Plans plan."
trigger: /execute-per-repo-implementation-plans
tags:
  - hermes
  - plan
  - execute
---

## Goal
Execute the plan at `.hermes/plans/per-repo-implementation-plans.md`.

## Context
This prompt loads and executes the consolidated plan document.

## Execution
1. Load the plan from `.hermes/plans/per-repo-implementation-plans.md`
2. Follow the plan's phases and requirements
3. Report progress and completion
