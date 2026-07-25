---
name: refactor-code
title: Drizzle ORM + next-auth Migration Plan (2026 Upgrade, DRY, markdownlint, Drizzle Patterns)
description: Refactor code for maintainability and standards.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - web
  - browser
  - todo
scripts: []
skills: []
formatter: default
plan: ''
dependencies: []
tags:
  - linting
  - markdown
  - migration
  - ml
  - nextjs
  - prompts
  - refactoring
  - specification
  - typescript
  - linting
  - markdown
  - migration
  - ml
  - nextjs
  - prompts
  - refactoring
  - specification
  - typescript
trigger: /refactor-code
---

## GoalRefactor code for maintainability and standards.## ContextUse when you need to next.js expert for the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## OverviewMigrate from legacy Appwrite/Prisma auth to Drizzle ORM + next-auth (Drizzle Adapter), using a hybrid user model and leveraging Drizzle’s latest features and patterns:## Steps> ### 1. Remove Legacy Auth/ORM>> ### 2. Install & Configure Drizzle ORM> **Full content:** `templates/refactor-code/steps.md`## Drizzle ORM Patterns to Use## Verification## Decisions & Scope**Ready for your confirmation or further tweaks!**## Template ReferencesTemplates in `templates/refactor-code/`:- `phases.md`- `steps.md`