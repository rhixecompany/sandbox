---
name: update-implementation-plan
title: Update Implementation Plan
description: Create or update an implementation plan with new or updated requirements for features, refactoring, package upgrades, design, or infrastructure work.
version: 1.0.0
author: Hermes Agent
tags:
  - planning
  - implementation
  - specification
  - documentation
  - refactor
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---

# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Template Variables](#template-variables)
- [Outputs](#outputs)
- [Rules](#rules)
- [Skills Required](#skills-required)
- [Phases](#phases)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)


## Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Template Variables](#template-variables)
- [Outputs](#outputs)
- [Rules](#rules)
- [Skills Required](#skills-required)
- [Phases](#phases)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)




## Goal

Create or update an implementation plan with new or updated requirements for features, refactoring, package upgrades, design, or infrastructure.

## update-implementation-plan> Create or update an implementation plan file with new or updated requirements for features, refactoring, package upgrades, design, architecture, or infrastructure.

## Context

Use when you need to create or update an implementation plan for the current workspace or task. The output implementation plan follows a standard section template with status badges.

## Inputs

The following inputs are gathered to create or update an implementation plan:- **Workspace State**: The current contents of `<workspace_root>`, including existing files, directory structure, and any plan files in the `plan/` directory. Discovered via Phase 1 file system scan.

- **User Request**: The specific request, diff, spec, or features provided by the user initiating the command. Passed as command arguments or context.
- **Plan Variables**: Any explicit prompt variables, paths, or constraints named in the original instructions (e.g., `<purpose>`, `<component>`, `<version>`). Extracted from user input.
- **Existing Plan File**: If updating an existing plan, the current content at `<workspace_root>/plan/<purpose>-<component>-<version>.md`. Loaded during Phase 1 assessment.

## Template Variables

Template variables used in this prompt follow this convention:| Variable | Scope | Example || --- | --- | --- || `<workspace_root

> ` | Absolute path to project root | `$HOME/Desktop/SandBox` (e.g. `C:\Users\Alexa\Desktop\Sandbox`) || `<purpose>` | Slug derived from task/feature name | `feature-auth-refactor` || `<component>` | Target component or module | `database` || `<version>` | Plan version (typically `v1`, `v2`) | `v1` |**Composite Example:**When combined in the output path template, these variables produce a concrete file path:```<workspace_root>/plan/<purpose>-<component>-<version>.md`$HOME/Desktop/Sandbox/plan/feature-auth-refactor-database-v1.md````

## Outputs

- A complete implementation plan at `<workspace_root>/plan/<purpose>-<component>-<version>.md`
- A concise verification note when the task benefits from one

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)
>
> 1. Use only evidence from the current workspace and the user request
> 2. Change only the implementation plan sections directly affected by new require

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)The skills listed below in the "Skills Required" section mirror the YAML front-matter `skills` declaration and indicate which Hermes skills must be available for this prompt to execute successfully. The Hermes agent will verify skill availability before running this prompt.| Skill | Purpose |
| --- | --- |
| `context-map` | Pre-change map of plan-related files and dependencies |
| `writing-plans` | Author structured implementation plans |
| `plans-and-specs` | Plan and spec namespace management |

## Phases

> **Goal:** Read the current workspace state and determine whether to create or up
>
> 1. Read the request and identify the exact scope

## Actions Summary

1. Read the request and workspace state
2. Determine create vs. update mode
3. Write or update the implementation plan with standard sections
4. Apply the correct status badge
5. Verify all sections are present and accurate

## Template References

Detailed templates in `templates/update-implementation-plan/`:- `phases.md`- `rules.md`

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

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`update-avm-modules-in-bicep.prompt.md`](update-avm-modules-in-bicep.prompt.md)
- [`update-docs-on-code-change.prompt.md`](update-docs-on-code-change.prompt.md)
- [`update-llms.prompt.md`](update-llms.prompt.md)
- [`update-markdown-file-index.prompt.md`](update-markdown-file-index.prompt.md)
- [`update-oo-component-documentation.prompt.md`](update-oo-component-documentation.prompt.md)
- [`update-specification.prompt.md`](update-specification.prompt.md)