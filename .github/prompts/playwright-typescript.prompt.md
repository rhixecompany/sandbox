---
name: playwright-typescript
title: Playwright Typescript
description: Comprehensive Playwright TypeScript prompt aligned to repository testing standards.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: None
tags:
  - frontend
  - playwright
  - prompts
  - skills
  - testing
  - typescript
trigger: /playwright-typescript
dependencies: []
metadata:
  hermes: {}
---
## GoalUse when "Comprehensive Playwright TypeScript prompt aligned to repository testing standards." to accomplish the associated tasks and objectives.

## DescriptionAuthor and refine Playwright TypeScript tests that are resilient, readable, and aligned with accessibility-first locator and assertion practices.

## ContextUse this prompt when creating or updating Playwright tests in the tests directory for user flows, regression scenarios, and end-to-end behavior validation.

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)- Playwright test design and isolation- Accessibility-first locator strategy- Deterministic assertion and flake reduction

## Subagents| Subagent | Role | When to Use || --- | --- | --- || Test Author | Writes structured Playwright tests | Always || Locator Auditor | Ensures robust user-facing locator choices | Locator-heavy tests || Stability Checker | Identifies flake and timing anti-patterns | Failing or intermittent tests |

## Personas- Test Author: Writes behavior-focused tests with clear steps.- Locator Auditor: Prefers role and label-based locators over brittle selectors.- Stability Checker: Eliminates fixed waits and unstable timing assumptions.

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Use @playwright/test with clear test.describe and test.step grouping.- Prefer getByRole, getByLabel, and user-visible locators.- Use web-first auto-retrying assertions and avoid hard-coded waits.- Keep tests feature-focused and stored under tests/ with clear names.- Verify navigation with URL assertions and structure with accessibility snapshots when applicable.

## Phases>

### Phase 1: Scenario and Test Design>>

### Phase 2: Test Implementation> **Full content:** `templates/playwright-typescript/phases.md`

## Steps1. Define scenario and expected outcomes.2. Choose robust, accessible locators.3. Implement tests with explicit action/assertion steps.4. Run tests and inspect failures.5. Iterate to stable green execution.

## Tasks- Task 1.1 — Convert scenario requirements into explicit user-facing test outcomes.- Task 1.2 — Implement tests with role/label/text-based locators.- Task 1.3 — Add meaningful web-first assertions for content and navigation.- Task 1.4 — Execute and fix instability without hard waits.- Task 1.5 — Confirm stable pass and summarize coverage.

## Subtasks- Subtask 1.1.1 — Capture setup and prerequisite state assumptions.- Subtask 1.2.1 — Replace brittle CSS/XPath selectors when possible.- Subtask 1.3.1 — Use toHaveText, toContainText, toHaveURL, and toHaveCount appropriately.- Subtask 1.4.1 — Resolve strict-mode violations and flaky transitions.- Subtask 1.5.1 — Document remaining gaps or deferred scenarios.

## Actions Summary1. Design behavior-driven scenarios.2. Implement robust Playwright tests.3. Run and stabilize.4. Deliver passing tests with clear intent.

## Template ReferencesTemplates in `templates/playwright-typescript/`:- `phases.md`

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

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.


## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

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

Comprehensive Playwright TypeScript prompt aligned to repository testing standards.


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


