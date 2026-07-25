---
name: execute-plan
title: Execute Plan
description: Load and execute any plan document from .hermes/plans/ by specifying its filename.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - subagent-driven-development
formatter: default
plan: ''
dependencies:
  - skill:subagent-driven-development
tags:
  - agents
  - ai-assistant
  - execution
  - frontend
  - prompts
  - specification
  - typescript
  - plan
  - execution
  - workflow
trigger: /execute-plan
---

## GoalExecute the specified plan from `.hermes/plans/`.**Parameter** — set `plan` to the plan filename (e.g., `acpx-agents-feature-specs.md`).## ContextLoads a target plan document and follows its phases, steps, and requirementssequentially. Use when a written plan already exists and needs driven to completion.## Inputs- `plan` — plan filename under `.hermes/plans/` (required).## Outputs- Plan phases executed in order.- Completion report with key outcomes.- Blockers surfaced honestly if encountered.## Rules> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the plan literally — do not skip or reorder.- Verify each phase's output before advancing.- If a phase references a file that does not exist, stop and report the gap.- Keep the response structured, deterministic, and easy to act on.## Phases### Phase 1: Load Plan1. Read `.hermes/plans/{plan}`.2. Parse the plan's phases, rules, and verification steps.3. Report the plan title and total number of phases.### Phase 2: Execute1. Walk through each phase in order.2. Perform the requested work with the smallest safe change set.3. Keep the steps explicit and reproducible.### Phase 3: Verify1. Run each verification step listed in the plan.2. Confirm outputs match the plan's acceptance criteria.### Phase 4: ReportSummarise what was done, what was verified, and any deviations from the plan.## Verification Checklist- [ ] `plan` parameter is provided and points to an existing file under `.hermes/plans/`.- [ ] Plan loaded and understood before execution.- [ ] Every phase completed before advancing to the next.- [ ] Blockers reported honestly (never fabricated).- [ ] Final report includes verification results.