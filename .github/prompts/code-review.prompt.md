---
name: code-review
title: Code Review
description: 'Comprehensive code review prompt for correctness, security, and testing risk.'
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
  - audit
  - data
  - frontend
  - prompts
  - security
  - skills
  - testing
  - typescript
trigger: /code-review
dependencies: []
metadata:
  hermes: {}
---
## GoalUse when "Comprehensive code review prompt for correctness, security, and testing risk." to accomplish the associated tasks and objectives.

## DescriptionPerform high-signal code reviews that prioritize correctness, security, and high-risk logic such as authentication, payments, and data operations.

## ContextUse this prompt when reviewing diffs, pull requests, or selected files and when the user asks for a review. Focus on actionable findings with evidence.

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)- Risk-based review and severity ranking- Security threat spotting and input-validation analysis- Test coverage and regression analysis

## Subagents| Subagent | Role | When to Use || --- | --- | --- || Reviewer | Primary correctness and behavior reviewer | Always || Security Checker | Security and data-handling review | Auth, secrets, external input, payment flows || Test Checker | Test sufficiency and CI readiness review | New behavior or risky refactors |

## Personas- Reviewer: Treats correctness and regressions as first priority, style as secondary.- Security Checker: Looks for unsafe trust boundaries, privilege mistakes, and missing validation.- Test Checker: Ensures new and changed behavior is covered by deterministic tests.

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Lead with findings ordered by severity.- Include concrete evidence with file paths and line references when possible.- Prioritize bugs, security risks, behavior regressions, and missing tests over style suggestions.- Request clarification instead of guessing when intent is ambiguous.- Keep summary concise after findings.

## Phases>

### Phase 1: Scope and Risk Mapping>>

### Phase 2: Deep Review> **Full content:** `templates/code-review/phases.md`

## Steps1. Read the diff and identify behavior-changing areas.2. Rank risk by security sensitivity and blast radius.3. Review changed logic and edge cases in depth.4. Check tests, docs, and configuration implications.5. Produce severity-ordered findings and concise summary.

## Tasks- Task 1.1 — Identify review scope and classify high-risk modules.- Task 1.2 — Verify correctness against expected business behavior.- Task 1.3 — Evaluate security controls and input validation boundaries.- Task 1.4 — Assess test coverage and CI readiness for changed behavior.- Task 1.5 — Deliver severity-ranked findings with evidence.

## Subtasks- Subtask 1.1.1 — List changed files and impacted public interfaces.- Subtask 1.2.1 — Check edge cases, null/empty states, and failure paths.- Subtask 1.3.1 — Confirm least-privilege and secret-safe practices.- Subtask 1.4.1 — Verify tests cover auth, payments, and reconciliation flows when applicable.- Subtask 1.5.1 — Separate must-fix findings from optional improvements.

## Actions Summary1. Scope the review.2. Analyze highest-risk logic first.3. Validate security and tests.4. Return prioritized findings and residual risks.

## Template ReferencesTemplates in `templates/code-review/`:- `phases.md`

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

Comprehensive code review prompt for correctness, security, and testing risk.


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


