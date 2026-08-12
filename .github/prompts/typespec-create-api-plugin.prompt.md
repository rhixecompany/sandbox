---
name: typespec-create-api-plugin
title: Create TypeSpec API Plugin
description: Generate a TypeSpec API plugin with REST operations, authentication,
  and Adaptive Cards for Microsoft 365 Copilot.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- terminal
- file
scripts: []
skills: []
formatter: default
plan: null
tags:
- ai-assistant
- api
- generator
- ml
- prompts
- specification
- typescript
- ai-assistant
- api
- generator
- ml
- prompts
- specification
- typescript
trigger: /typespec-create-api-plugin
mode: agent
dependencies: []
metadata:
  hermes: {}
---

## Goal

Generate a TypeSpec API plugin with REST operations, authentication, and Adaptive Cards for Microsoft 365 Copilot.

## Context

Use when you need to typespec create api plugin for the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake

- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute

- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify

- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off

- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Requirements

> Generate TypeSpec files with:>>

### main.tsp

- Agent Definition

> **Full content:**

## Authentication Options

> Choose based on API requirements:>
>
> 1. **No Authentication** (Public APIs)
> **Full content:**

## Function Capabilities

### Confirmation Dialog

> type: "AdaptiveCard",

## Best Practices

1. **Operation Names**: Use clear, action-oriented names (listProjects, createTicket)
2. **Models**: Define TypeScript-like models for requests and responses
3. **HTTP Methods**: Use appropriate verbs (@get, @post, @patch, @delete)
4. **Paths**: Use RESTful path conventions with @route
5. **Parameters**: Use @path, @query, @header, @body appropriately
6. **Descriptions**: Provide clear descriptions for model understanding
7. **Confirmations**: Add for destructive operations (delete, update critical data)
8. **Cards**: Use for rich visual responses with multiple data items

## Workflow

Ask the user:1. What is the API base URL and purpose?2. What operations are needed (CRUD operations)?3. What authentication method does the API use?4. Should confirmations be required for any operations?5. Do responses need Adaptive Cards?Then generate:- Complete `main.tsp` with agent definition- Complete `actions.tsp` with API operations and models- Optional `cards/card.json` if Adaptive Cards are needed

## Template References

Templates in `templates/typespec-create-api-plugin/`:- `authentication_options.md`- `function_capabilities.md`- `phases.md`- `requirements.md`- `workflow.md`

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

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`typespec-api-operations.prompt.md`](typespec-api-operations.prompt.md)
- [`typespec-create-agent.prompt.md`](typespec-create-agent.prompt.md)
