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
plan: None
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
  - workflow
trigger: /execute-plan
metadata:
  hermes: {}
---
## GoalExecute the specified plan from `.hermes/plans/`.**Parameter** — set `plan` to the plan filename (e.g., `acpx-agents-feature-specs.md`).

## ContextLoads a target plan document and follows its phases, steps, and requirementssequentially. Use when a written plan already exists and needs driven to completion.

## Inputs- `plan` — plan filename under `.hermes/plans/` (required).

## Outputs- Plan phases executed in order.- Completion report with key outcomes.- Blockers surfaced honestly if encountered.

## Rules> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the plan literally — do not skip or reorder.- Verify each phase's output before advancing.- If a phase references a file that does not exist, stop and report the gap.- Keep the response structured, deterministic, and easy to act on.

## Phases

### Phase 1: Load Plan1. Read `.hermes/plans/{plan}`.2. Parse the plan's phases, rules, and verification steps.3. Report the plan title and total number of phases.

### Phase 2: Execute1. Walk through each phase in order.2. Perform the requested work with the smallest safe change set.3. Keep the steps explicit and reproducible.

### Phase 3: Verify1. Run each verification step listed in the plan.2. Confirm outputs match the plan's acceptance criteria.

### Phase 4: ReportSummarise what was done, what was verified, and any deviations from the plan.

## Verification Checklist- [ ] `plan` parameter is provided and points to an existing file under `.hermes/plans/`.- [ ] Plan loaded and understood before execution.- [ ] Every phase completed before advancing to the next.- [ ] Blockers reported honestly (never fabricated).- [ ] Final report includes verification results.

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |


## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes


## Context

Use when researching topics or synthesizing findings. Start with broad discovery, then narrow to specific sources.


## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Verify sources before citing.
- Extract to structured markdown.
- Note confidence levels for findings.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.


## Phases

### Phase 1: Intake
- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute
- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify
- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off
- Return final artifact or findings clearly.
- Stop once the requested result is delivered.


## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.


## Verification Checklist

| # | Gate | Criterion |
|---|------|-----------|
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |


## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

Load and execute any plan document from .hermes/plans/ by specifying its filename.


## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |


## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |



## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions


