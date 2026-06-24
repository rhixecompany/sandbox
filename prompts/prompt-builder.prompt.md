---
license: MIT
author: Hermes Agent
version: 1.0.0
title: prompt-builder
name: prompt-builder
trigger: /prompt-builder
description: >-
  Guide users through creating high-quality .prompt.md files with proper structure, tools, and best practices.
tags: []
  [hermes, copilot, opencode, writing-skills, scaffolding, template]
dependencies:
  - skill:writing-plans
  - skill:writing-skills
  - skill:/context-map
  - skill:/prompt-engineering
skills:
  - writing-plans — Structured prompt authoring
  - writing-skills — Crafting and optimizing prompts and instructions
---

# prompt-builder

> Guide users through creating high-quality GitHub Copilot prompts with proper structure, tools, and best practices.

## Goal

Guide users through creating high-quality `.prompt.md` files by systematically gathering requirements and generating a complete, production-ready prompt file.

## Context

Use when the user wants to create or improve a `.prompt.md` prompt file. In `ask` and `agent` modes, the workflow asks exactly one focused question for each of the 9 topic areas (9 questions total) across identity, persona, task, context, instructions, output, tools, configuration, and validation. In `edit` mode, use the existing draft as the primary source and ask only targeted gap questions where needed.

**Critical rules (must appear within the first 15% of execution):**
- Never overwrite existing `.prompt.md` files without user confirmation
- Always follow patterns from the 4 reference prompts listed in the Reference Patterns section of this prompt
- Generate prompts optimized for AI consumption (token-efficient, structured)

## Inputs

- User's answers to 9 discovery questions (gathered interactively)
- Existing prompt files in this repository for pattern reference
- Workspace context for domain-specific customization

## Outputs

- A complete `.prompt.md` file with frontmatter, persona, task, instructions, context, output, and quality sections
- A confirmation of the generated file path

## Rules

1. **Discovery first** — Gather all requirements through the 9-area questionnaire before generating
2. **Pattern-driven** — Follow patterns from the 4 reference prompts listed in the Reference Patterns section
3. **Context preflight** — Run `/context-map` before generation to map inputs, dependencies, and affected files
4. **Persona-specific** — Define a clear role with expertise level, domain knowledge, and qualifications
5. **Tool-aware** — Select appropriate tools based on the task:
   - **Code analysis/reading:** `codebase`, `search`
   - **File modification:** `editFiles`
   - **External APIs:** `fetch`
   - **Command execution:** `runCommands`
   - **Testing:** `runCommands` (test runner) + `editFiles`
   - **Documentation:** `codebase`, `search`, `editFiles`
6. **Validation included** — Every generated prompt must include success criteria and validation steps
7. **Never overwrite** — Do not overwrite existing `.prompt.md` files without user confirmation
8. **Discovery gap handling** — If a user's answer to any topic is missing, contradictory, or insufficient, ask a single targeted follow-up question before proceeding to Phase 2. Do not proceed to generation with unresolved gaps.

## Modes

| Mode | Behavior | Use when |
| --- | --- | --- |
| `ask` | Ask 9 discovery questions to iteratively refine the prompt | You need to explore and understand scope first |
| `edit` | Edit an existing prompt using guided questions | You already have a draft and want to improve it |
| `agent` | Create a prompt for a specific agent or workflow | You're building a new command/agent interaction |

Phase execution by mode:
- `ask` — run all 3 phases in full
- `edit` — run Phase 1 as targeted gap discovery based on the existing draft, then run Phases 2 and 3
- `agent` — run all 3 phases in full, and restrict tool selection in Phase 2 to agent-appropriate tools

## Skills Required

| Skill | Purpose |
| --- | --- |
| `context-map` | Preflight mapping of reference prompts and affected files |
| `writing-plans` | Structured prompt authoring and section organization |
| `writing-skills` | Crafting and optimizing prompts and instructions |
| `prompt-engineering` | Research-backed prompt optimization before handoff |

## Phases

> ### Phase 1: Discovery
> **Goal:** Gather all requirements through systematic questioning.

> **Full content:** `templates/prompt-builder/phases.md`

## Best Practices Integration

Based on analysis of existing prompts, ensure the generated prompt includes:

- ✅ **Clear Structure:** Well-organized sections with logical flow (see `architecture-blueprint-generator.prompt.md`)
- ✅ **Specific Instructions:** Actionable, unambiguous directions (see `create-implementation-plan.prompt.md`)
- ✅ **Proper Context:** All necessary information for task completion (see `playwright-generate-test.prompt.md`)
- ✅ **Tool Integration:** Appropriate tool selection for the task (see `create-github-action-workflow-specification.prompt.md`)
- ✅ **Error Handling:** Guidance for edge cases and failures (see all reference patterns)
- ✅ **Output Standards:** Clear formatting and structure requirements (see `architecture-blueprint-generator.prompt.md`)
- ✅ **Validation:** Criteria for measuring success (see all reference patterns)
- ✅ **Maintainability:** Easy to update and extend (see `create-implementation-plan.prompt.md`)

## Reference Patterns

Generated prompts follow patterns from existing high-quality prompts:
- [`playwright-generate-test.prompt.md`](.github/prompts/playwright-generate-test.prompt.md) — Code generation scaffold
- [`create-github-action-workflow-specification.prompt.md`](.github/prompts/create-github-action-workflow-specification.prompt.md) — Structured specification
- [`architecture-blueprint-generator.prompt.md`](.github/prompts/architecture-blueprint-generator.prompt.md) — Comprehensive blueprint
- [`create-implementation-plan.prompt.md`](.github/prompts/create-implementation-plan.prompt.md) — Implementation plan

## Actions Summary

1. Ask exactly one focused question per topic area (9 questions total, one per row in the Discovery table); in `edit` mode, ask only targeted gap questions based on the existing draft
2. Compile answers into a structured prompt
3. Generate frontmatter (description, agent mode, tools, model)
4. Write persona, task, instructions, input, output, and quality sections
5. Verify against repository patterns and best practices
6. Return the final `.prompt.md` file path


## Template References

Detailed templates in `templates/prompt-builder/`:
- `phases.md`
