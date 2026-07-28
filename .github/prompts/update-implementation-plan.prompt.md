---
name: update-implementation-plan
title: Update Implementation Plan
description: 'Create or update an implementation plan with new or updated requirements for features, refactoring, package upgrades, design, or infrastructure.'
version: 2.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - writing-plans
  - plans-and-specs
  - context-map
formatter: default
plan: None
dependencies:
  - skill:writing-plans
  - skill:plans-and-specs
  - skill:context-map
tags:
  - architecture
  - frontend
  - maintenance
  - migration
  - prompts
  - refactoring
  - specification
  - typescript
trigger: /update-implementation-plan
metadata:
  hermes: None
  related_skills:
    - writing-plans
    - plans-and-specs
    - context-map
---
## Goal

Create or update an implementation plan with new or updated requirements for features, refactoring, package upgrades, design, or infrastructure.

# update-implementation-plan> Create or update an implementation plan file with new or updated requirements for features, refactoring, package upgrades, design, architecture, or infrastructure.

## GoalSystematically create or update structured implementation plans with proper version control and status tracking. This ensures all requirements, dependencies, and implementation steps are documented and discoverable for team coordination and project tracking.

## ContextUse when you need to create or update an implementation plan for the current workspace or task. The output implementation plan follows a standard section template with status badges.

## InputsThe following inputs are gathered to create or update an implementation plan:- **Workspace State**: The current contents of `<workspace_root>`, including existing files, directory structure, and any plan files in the `plan/` directory. Discovered via Phase 1 file system scan.- **User Request**: The specific request, diff, spec, or features provided by the user initiating the command. Passed as command arguments or context.- **Plan Variables**: Any explicit prompt variables, paths, or constraints named in the original instructions (e.g., `<purpose>`, `<component>`, `<version>`). Extracted from user input.- **Existing Plan File**: If updating an existing plan, the current content at `<workspace_root>/plan/<purpose>-<component>-<version>.md`. Loaded during Phase 1 assessment.

## Template VariablesTemplate variables used in this prompt follow this convention:| Variable | Scope | Example || --- | --- | --- || `<workspace_root>` | Absolute path to project root | `$HOME/Desktop/SandBox` (e.g. `C:\Users\Alexa\Desktop\Sandbox`) || `<purpose>` | Slug derived from task/feature name | `feature-auth-refactor` || `<component>` | Target component or module | `database` || `<version>` | Plan version (typically `v1`, `v2`) | `v1` |**Composite Example:**When combined in the output path template, these variables produce a concrete file path:```<workspace_root>/plan/<purpose>-<component>-<version>.md`$HOME/Desktop/Sandbox/plan/feature-auth-refactor-database-v1.md````

## Outputs- A complete implementation plan at `<workspace_root>/plan/<purpose>-<component>-<version>.md`- A concise verification note when the task benefits from one

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)> 1. Use only evidence from the current workspace and the user request> 2. Change only the implementation plan sections directly affected by new require> **Full content:** `templates/update-implementation-plan/rules.md`

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)The skills listed below in the "Skills Required" section mirror the YAML front-matter `skills` declaration and indicate which Hermes skills must be available for this prompt to execute successfully. The Hermes agent will verify skill availability before running this prompt.| Skill | Purpose || --- | --- || `context-map` | Pre-change map of plan-related files and dependencies || `writing-plans` | Author structured implementation plans || `plans-and-specs` | Plan and spec namespace management |

## Phases> **Goal:** Read the current workspace state and determine whether to create or up> 1. Read the request and identify the exact scope> **Full content:** `templates/update-implementation-plan/phases.md`

## Actions Summary1. Read the request and workspace state2. Determine create vs. update mode3. Write or update the implementation plan with standard sections4. Apply the correct status badge5. Verify all sections are present and accurate

## Template ReferencesDetailed templates in `templates/update-implementation-plan/`:- `phases.md`- `rules.md`

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


