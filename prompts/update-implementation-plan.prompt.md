---
license: MIT
author: Hermes Agent
version: 1.0.0
title: update-implementation-plan
name: update-implementation-plan
trigger: update-implementation-plan
description: >-
  Create or update an implementation plan with new or updated requirements for features, refactoring, package upgrades, design, or infrastructure.
tags:
  - architecture
  - frontend
  - maintenance
  - migration
  - prompts
  - refactoring
  - specification
  - typescript
  - hermes
  - copilot
  - planning
  - implementation
dependencies:
  - skill:writing-plans
  - skill:plans-and-specs
  - skill:context-map
skills:
  - writing-plans — Author structured implementation plans
  - plans-and-specs — Plan and spec management
metadata:
  hermes:
    related_skills: []
    tags:
    - update-implementation-plan.prompt

---
metadata:
  hermes:
    related_skills: []
    tags:
    - update-implementation-plan.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - update-implementation-plan.prompt

# update-implementation-plan

> Create or update an implementation plan file with new or updated requirements for features, refactoring, package upgrades, design, architecture, or infrastructure.

## Goal

Systematically create or update structured implementation plans with proper version control and status tracking. This ensures all requirements, dependencies, and implementation steps are documented and discoverable for team coordination and project tracking.

## Context

Use when you need to create or update an implementation plan for the current workspace or task. The output implementation plan follows a standard section template with status badges.

## Inputs

The following inputs are gathered to create or update an implementation plan:

- **Workspace State**: The current contents of `<workspace_root>`, including existing files, directory structure, and any plan files in the `plan/` directory. Discovered via Phase 1 file system scan.
- **User Request**: The specific request, diff, spec, or features provided by the user initiating the command. Passed as command arguments or context.
- **Plan Variables**: Any explicit prompt variables, paths, or constraints named in the original instructions (e.g., `<purpose>`, `<component>`, `<version>`). Extracted from user input.
- **Existing Plan File**: If updating an existing plan, the current content at `<workspace_root>/plan/<purpose>-<component>-<version>.md`. Loaded during Phase 1 assessment.

## Template Variables

Template variables used in this prompt follow this convention:

| Variable | Scope | Example |
| --- | --- | --- |
| `<workspace_root>` | Absolute path to project root | `$HOME/Desktop/SandBox` (e.g. `C:\Users\Alexa\Desktop\Sandbox`) |
| `<purpose>` | Slug derived from task/feature name | `feature-auth-refactor` |
| `<component>` | Target component or module | `database` |
| `<version>` | Plan version (typically `v1`, `v2`) | `v1` |

**Composite Example:**
When combined in the output path template, these variables produce a concrete file path:
```
<workspace_root>/plan/<purpose>-<component>-<version>.md
`$HOME/Desktop/Sandbox/plan/feature-auth-refactor-database-v1.md`
```

## Outputs

- A complete implementation plan at `<workspace_root>/plan/<purpose>-<component>-<version>.md`
- A concise verification note when the task benefits from one

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


> 1. Use only evidence from the current workspace and the user request
> 2. Change only the implementation plan sections directly affected by new require

> **Full content:** `templates/update-implementation-plan/rules.md`

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#update-implementation-plan)

The skills listed below in the "Skills Required" section mirror the YAML front-matter `skills` declaration and indicate which Hermes skills must be available for this prompt to execute successfully. The Hermes agent will verify skill availability before running this prompt.

| Skill | Purpose |
| --- | --- |
| `context-map` | Pre-change map of plan-related files and dependencies |
| `writing-plans` | Author structured implementation plans |
| `plans-and-specs` | Plan and spec namespace management |

## Phases

> **Goal:** Read the current workspace state and determine whether to create or up
> 1. Read the request and identify the exact scope

> **Full content:** `templates/update-implementation-plan/phases.md`

## Actions Summary

1. Read the request and workspace state
2. Determine create vs. update mode
3. Write or update the implementation plan with standard sections
4. Apply the correct status badge
5. Verify all sections are present and accurate


## Template References

Detailed templates in `templates/update-implementation-plan/`:
- `phases.md`
- `rules.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
