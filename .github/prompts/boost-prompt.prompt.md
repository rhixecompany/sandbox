---
name: boost-prompt
title: Boost Prompt
description: 'Interactive prompt refinement workflow: interrogates scope, deliverables, and constraints, then copies final markdown to clipboard using Joyride.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - writing-skills
  - writing-plans
  - joyride
  - context-map
  - prompt-engineering
formatter: default
plan: None
dependencies:
  - skill:writing-skills
  - skill:writing-plans
  - skill:joyride
  - skill:context-map
  - skill:prompt-engineering
tags:
  - frontend
  - markdown
  - ml
  - prompts
  - typescript
  - workflow
trigger: /boost-prompt
metadata:
  hermes: {}
---
## Goal

Interactive prompt refinement workflow: interrogates scope, deliverables, and constraints, then copies final markdown to clipboard using Joyride.

# boost-prompt> Interactive prompt refinement workflow: interrogates scope, deliverables, constraints; copies final markdown to clipboard; never writes code.

## GoalIteratively refine a user's task prompt into a high-quality, detailed prompt through interrogation, exploration, and structured formatting.

## ContextUse when you need to improve a draft prompt before submitting it to an AI system. Requires the Joyride VS Code extension for clipboard operations. This prompt does NOT write code - it only refines prompts.**Critical rules (must appear within the first 15% of execution):**- DO NOT WRITE ANY CODE - this is a prompt refinement workflow only- Always ask clarifying questions before finalizing the prompt- Copy the final markdown to clipboard using Joyride after each revision

## Inputs- A draft prompt from the user- The current workspace context (for project exploration)- Optional constraints or specific requirements

## Outputs- An improved, structured prompt in markdown format- Prompt copied to system clipboard via Joyride- Verification that the user is satisfied with the result

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)1. **No code** - DO NOT write any code; this workflow is for prompt refinement only2. **Interrogate first** - Ask specific questions to understand scope, objectives, deliverables, and constraints before refining3. **Explore the project** - Use available tools to understand the codebase and task context4. **Map context first** - Run `/context-map` before deep prompt refinement so file and dependency context is explicit5. **Structured output** - Organize the prompt into clear sections or steps6. **Clipboard delivery** - Use Joyride to copy the final markdown to the system clipboard7. **Iterate** - After delivering, ask the user if they want changes or additions

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill | Purpose || --- | --- || `context-map` | Preflight map of relevant files and references before refinement || `writing-skills` | Crafting and optimizing prompts and instructions || `writing-plans` | Structured prompt authoring and organization (section layout, phase flow) |

## Tools Required> **Requirement**: VS Code Joyride extension installed and active>> - Install from VS Code Extensions marketplace: search "Joyride"> **Full content:** `templates/boost-prompt/tools_required.md`

## Phases>

### Phase 1: Interrogate>> **Goal:** Understand the task scope, objectives, deliverables, and constraints.> **Full content:** `templates/boost-prompt/phases.md`

## Actions Summary1. Interrogate the user about scope, deliverables, and constraints2. Explore the project workspace for context3. Refine the prompt into structured markdown4. Copy to clipboard via Joyride5. Present in chat6. Ask for feedback and iterate if needed

## Template ReferencesTemplates in `templates/boost-prompt/`:- `phases.md`- `tools_required.md`

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


