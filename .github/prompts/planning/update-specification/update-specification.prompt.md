---
name: update-specification
title: Update Specification
description: Update an existing solution specification optimized for Generative AI consumption based on new requirements or updates to existing code.
trigger: /update-specification
category: planning
version: 1.0.0
author: Hermes Agent
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Update an existing solution specification optimized for Generative AI consumption based on new requirements or updates to existing code.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [Best Practices for AI-Ready Specifications](#best-practices-for-ai-ready-specifications)
- [1. Purpose & Scope](#1-purpose-&-scope)
- [2. Definitions](#2-definitions)
- [3. Requirements, Constraints & Guidelines](#3-requirements-constraints-&-guidelines)
- [4. Interfaces & Data Contracts](#4-interfaces-&-data-contracts)
- [5. Acceptance Criteria](#5-acceptance-criteria)
- [6. Test Automation Strategy](#6-test-automation-strategy)
- [7. Rationale & Context](#7-rationale-&-context)
- [8. Dependencies & External Integrations](#8-dependencies-&-external-integrations)
- [9. Examples & Edge Cases](#9-examples-&-edge-cases)
- [10. Validation Criteria](#10-validation-criteria)
- [11. Related Specifications / Further Reading](#11-related-specifications-/-further-reading)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
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
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [Best Practices for AI-Ready Specifications](#best-practices-for-ai-ready-specifications)
- [1. Purpose & Scope](#1-purpose-&-scope)
- [2. Definitions](#2-definitions)
- [3. Requirements, Constraints & Guidelines](#3-requirements-constraints-&-guidelines)
- [4. Interfaces & Data Contracts](#4-interfaces-&-data-contracts)
- [5. Acceptance Criteria](#5-acceptance-criteria)
- [6. Test Automation Strategy](#6-test-automation-strategy)
- [7. Rationale & Context](#7-rationale-&-context)
- [8. Dependencies & External Integrations](#8-dependencies-&-external-integrations)
- [9. Examples & Edge Cases](#9-examples-&-edge-cases)
- [10. Validation Criteria](#10-validation-criteria)
- [11. Related Specifications / Further Reading](#11-related-specifications-/-further-reading)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Update an existing specification file for the solution, optimized for Generative AI consumption based on new requirements or updates to any existing code.


Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/rules-core.md`](templates/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.


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

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## Best Practices for AI-Ready Specifications

> - Use precise, explicit, and unambiguous language.
> - distinguish between requirements, constraints, and recommendations.
> **Full content:**

## 1. Purpose & Scope

[Provide a clear, concise description of the specification's purpose and the scope of its application. State the intended audience and any assumptions.]

## 2. Definitions

[List and define all acronyms, abbreviations, and domain-specific terms used in this specification.]

## 3. Requirements, Constraints & Guidelines

[Explicitly list all requirements, constraints, rules, and guidelines. Use bullet points or tables for clarity.]

- **REQ-001**: Requirement 1- **SEC-001**: Security Requirement 1- **[3 LETTERS]-001**: Other Requirement 1- **CON-001**: Constraint 1- **GUD-001**: Guideline 1- **PAT-001**: Pattern to follow 1

## 4. Interfaces & Data Contracts

[Describe the interfaces, APIs, data contracts, or integration points. Use tables or code blocks for schemas and examples.]

## 5. Acceptance Criteria

[Define clear, testable acceptance criteria for each requirement using Given-When-Then format where appropriate.]- **AC-001**: Given [context], When [action], Then [expected outcome]- **AC-002**: The system shall [specific behavior] when [condition]- **AC-003**: [Additional acceptance criteria as needed]

## 6. Test Automation Strategy

[Define the testing approach, frameworks, and automation requirements.]

- **Test Levels**: Unit, Integration, End-to-End- **Frameworks**: MSTest, FluentAssertions, Moq (for .NET applications)- **Test Data Management**: [approach for test data creation and cleanup]- **CI/CD Integration**: [automated testing in GitHub Actions pipelines]- **Coverage Requirements**: [minimum code coverage thresholds]- **Performance Testing**: [approach for load and performance testing]

## 7. Rationale & Context

[Explain the reasoning behind the requirements, constraints, and guidelines. Provide context for design decisions.]

## 8. Dependencies & External Integrations

> [Define the external systems, services, and architectural dependencies required>
>
> - **EXT-001**: [External system name] - [Purpose and integration type]
> **Full content:**

## 9. Examples & Edge Cases

```c

ode// Code snippet or data example demonstrating the correct application of the guidelines, including edge cases```````

```

## 10. Validation Criteria

[List the criteria or tests that must be satisfied for compliance with this specification.]

## 11. Related Specifications / Further Reading

[Link to related spec 1] [Link to relevant external documentation]

## Template References

Detailed templates in `templates/`:

## Personas

See [`templates/personas.md`](templates/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/personality.md`](templates/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/best-practices.md`](templates/best-practices.md) for cross-cutting best practices.

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

See [`templates/deps-core.md`](templates/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/skills-table-core.md`](templates/skills-table-core.md) for shared skills table.

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

## Workflow

<content>

Same-family prompts:

- [`update-avm-modules-in-bicep.prompt.md`](update-avm-modules-in-bicep.prompt.md)
- [`update-docs-on-code-change.prompt.md`](update-docs-on-code-change.prompt.md)
- [`update-implementation-plan.prompt.md`](update-implementation-plan.prompt.md)
- [`update-llms.prompt.md`](update-llms.prompt.md)
- [`update-markdown-file-index.prompt.md`](update-markdown-file-index.prompt.md)
- [`update-oo-component-documentation.prompt.md`](update-oo-component-documentation.prompt.md)
