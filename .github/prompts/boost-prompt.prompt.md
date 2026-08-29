---
name: boost-prompt
title: Prompt Refinement Interrogation
description: Interactively interrogate a prompt's scope, deliverables, and constraints, then copy the refined markdown to the clipboard via Joyride.
trigger: /boost-prompt
version: 1.0.0
author: Hermes Agent
tags:
  - prompt-engineering
  - interactive
  - tool
  - refinement
  - developer-experience
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
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Skills Required](#skills-required)
- [Tools Required](#tools-required)
- [Phases](#phases)
  - [Phase 1: Interrogate](#phase-1:-interrogate)
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



- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Skills Required](#skills-required)
- [Tools Required](#tools-required)
- [Phases](#phases)
- [Phase 1: Interrogate](#phase-1:-interrogate)
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





Interactive prompt refinement workflow: interrogates scope, deliverables, and constraints, then copies final markdown to clipboard using Joyride.

## boost-prompt> Interactive prompt refinement workflow: interrogates scope, deliverables, constraints; copies final markdown to clipboard; never writes code.


Use when you need to improve a draft prompt before submitting it to an AI system. Requires the Joyride VS Code extension for clipboard operations. This prompt does NOT write code - it only refines prompts.**Critical rules (must appear within the first 15% of execution):**- DO NOT WRITE ANY CODE - this is a prompt refinement workflow only- Always ask clarifying questions before finalizing the prompt- Copy the final markdown to clipboard using Joyride after each revision

## Inputs

- A draft prompt from the user
- The current workspace context (for project exploration)
- Optional constraints or specific requirements

## Outputs

- An improved, structured prompt in markdown format
- Prompt copied to system clipboard via Joyride
- Verification that the user is satisfied with the result

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. **No code** - DO NOT write any code; this workflow is for prompt refinement only
2. **Interrogate first** - Ask specific questions to understand scope, objectives, deliverables, and constraints before refining
3. **Explore the project** - Use available tools to understand the codebase and task context
4. **Map context first** - Run `/context-map` before deep prompt refinement so file and dependency context is explicit
5. **Structured output** - Organize the prompt into clear sections or steps
6. **Clipboard delivery** - Use Joyride to copy the final markdown to the system clipboard
7. **Iterate** - After delivering, ask the user if they want changes or additions

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill | Purpose |
| --- | --- |
| `context-map` | Preflight map of relevant files and references before refinement |
| `writing-skills` | Crafting and optimizing prompts and instructions |
| `writing-plans` | Structured prompt authoring and organization (section layout, phase flow) |

## Tools Required

> **Requirement**: VS Code Joyride extension installed and active>
>
> - Install from VS Code Extensions marketplace: search "Joyride"
> **Full content:**


### Phase 1: Interrogate

> **Goal:** Understand the task scope, objectives, deliverables, and constraints.

## Actions Summary

1. Interrogate the user about scope, deliverables, and constraints
2. Explore the project workspace for context
3. Refine the prompt into structured markdown
4. Copy to clipboard via Joyride
5. Present in chat
6. Ask for feedback and iterate if needed

## Template References

Templates in `templates/boost-prompt/`:- `phases.md`- `tools_required.md`

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

- [`ai-prompt-engineering-safety-review.prompt.md`](ai-prompt-engineering-safety-review.prompt.md)
- [`comprehensive-prompt-enhancer.prompt.md`](comprehensive-prompt-enhancer.prompt.md)
- [`debugger-prompt.prompt.md`](debugger-prompt.prompt.md)
- [`tldr-prompt.prompt.md`](tldr-prompt.prompt.md)

