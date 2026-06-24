---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "execute-dev-init-spec"
title: "Dev Init Spec"
description: "Execute the Dev Init Spec plan."
trigger: /execute-dev-init-spec
tags: []
  - hermes
  - plan
  - execute
---

## Goal
Execute the plan at `.hermes/plans/dev-init-spec.md`.

## Context
This prompt loads and executes the consolidated plan document.

## Execution
1. Load the plan from `.hermes/plans/dev-init-spec.md`
2. Follow the plan's phases and requirements
3. Report progress and completion
