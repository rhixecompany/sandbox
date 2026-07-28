---
name: plan-execute
title: Execute Implementation Plan
description: 'Load and execute any implementation plan step-by-step. Reads the plan from a `.prompt.md` or `.md` file, runs each phase sequentially with verification gates. Replaces all ad-hoc execute-plan-* prompts with a single generic executor.'
version: 1.0.0
license: MIT
author: Hermes Agent (consolidated)
toolsets:
  - file
  - terminal
scripts: []
skills:
  - plans-and-specs
  - subagent-driven-development
  - verification-before-completion
  - writing-plans
formatter: default
plan: None
dependencies:
  - skill:plans-and-specs
  - skill:subagent-driven-development
  - skill:verification-before-completion
  - skill:writing-plans
  - tool:terminal
  - tool:search_files
tags:
  - debugging
  - planning
  - prompts
  - typescript
trigger: /plan-execute
metadata:
  hermes: {}
---
## Goal

Load and execute any implementation plan step-by-step. Reads the plan from a `.prompt.md` or `.md` file, runs each phase sequentially with verification gates. Replaces all ad-hoc execute-plan-* prompts with a single generic executor.

> **Shared template references:**>> - [Core rules](templates/_shared/rules-core.md)> - [Section skeleton](templates/_shared/section-skeleton.md)> - [Verification checklist](templates/_shared/verification-checklist.md)

## GoalExecute a structured implementation plan from start to finish. Load the plan file, process each phase in order with verification gates, and report completion or blockers.**Consolidates:** All previous `execute-plan-*` and `execute-*plan*` prompts(comicwise-session, debugger, eslint, optimization, setup, skills-debug,acpx-agent-integration, bash-scripts-plan, dev-init, docs, hermes-config,orchestrator, per-repo, prompt-conversion, sandbox-projects-merge, etc.)

## Input- **Plan file path** — e.g. `prompts/plan-xxx.prompt.md` or `.hermes/plans/xxx.md`- **Optional overrides** — phase to start from, env vars, profile selections

## Core RulesSee [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md).Additional execution-specific rules:1. **Strict sequential** — Never skip ahead. Complete each phase, verify its gate, then proceed.2. **No silent failures** — If a phase fails, stop and report before retrying or continuing.3. **Git checkpoint per phase** — After each successful phase, `git add && git commit` with descriptive message.4. **Idempotent phases** — Each phase should be safe to re-run if it fails mid-way.5. **Plan is read-only** — Never modify the plan file during execution; log progress separately.

## Workflow

### Phase 1: Load plan1. Read the plan file (`read_file`).2. Parse phases, gates, dependencies, and outputs.3. Verify all referenced skills/prompts/tools exist.4. Write session start marker to `.hermes/plans/docs/<plan-name>-progress.md`.

### Phase 2: Execute phasesFor each phase in order:1. **Pre-check** — Confirm verification gate from previous phase is met.2. **Execute** — Run the steps using appropriate tools.3. **Verify** — Run the phase's verification gate explicitly.4. **Checkpoint** — `git add -A && git commit -m "feat(plan): <plan-name> phase <N>: <name>"`5. **Log** — Update progress doc with phase result.

### Phase 3: Final verification1. Run the plan's full verification checklist.2. Confirm all outputs exist and match expected format.3. Write session summary to progress doc.

### Phase 4: ReportSummarise:- Phases completed / total- Any skipped phases and why- All verification gates passed- Outputs produced- Git commit SHAs for each phase

## Verification Checklist- [ ] Plan loaded and parsed successfully- [ ] All phase dependencies resolved- [ ] Each phase executed in strict order- [ ] Verification gate passed for every phase- [ ] Git checkpoint committed after each phase- [ ] No dangling processes or background jobs- [ ] All expected outputs exist and are valid- [ ] Progress doc written with complete trail

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

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.


## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

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


