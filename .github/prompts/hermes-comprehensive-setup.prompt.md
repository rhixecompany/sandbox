---
name: hermes-comprehensive-setup
title: Comprehensive Hermes and OpenCode Setup, Migration, and Validation
description: 'Configure Hermes and OpenCode using best practices: load all prompts, plans, markdown files, skills, MCP servers, hooks, and templates. Run enhancement, validation, and dry-run verification end to end.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
- hermes
- opencode
- migration
- mcp
- validation
- setup
- automation
toolsets:
- terminal
- file
- skills
- todo
- web
- browser
- memory
- context_engine
- session_search
- delegation
- code_execution
scripts:
- ~/AppData/Local/hermes/scripts/build_registry.py
- ~/AppData/Local/hermes/scripts/audit_prompts.py
- ~/AppData/Local/hermes/scripts/verify_sync.py
trigger: /hermes-comprehensive-setup
skills: []
dependencies: []
metadata:
  hermes: {}
formatter: default
plan: ''
---
## Goal

Execute the `hermes-comprehensive-setup` workflow. Full details: `templates/hermes-comprehensive-setup/README.md`.

## Template Reference

Detailed template in `templates/hermes-comprehensive-setup/`:

- `README.md`

## Execution

See `templates/hermes-comprehensive-setup/README.md` for phases/steps/workflow.

## Steps

1. Read `templates/hermes-comprehensive-setup/README.md`.
2. Execute the workflow.
3. Verify outputs.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.


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
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `test-driven-development` | TDD workflow enforcement |
| `code-review` | Code quality assurance |
| `systematic-debugging` | Debugging and root cause analysis |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |


## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `code-sandbox` | Isolated code execution and testing |
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



## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.
