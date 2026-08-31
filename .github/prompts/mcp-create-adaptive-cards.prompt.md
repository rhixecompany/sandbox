---
name: mcp-create-adaptive-cards
title: MCP Create Adaptive Cards
description: Creates Microsoft Adaptive Cards for MCP-based plugins, defining inputs, layouts, and actions for interactive Copilot experiences.
trigger: /mcp-create-adaptive-cards
version: 1.0.0
author: Hermes Agent
date: 2026-08-25
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
Creates Microsoft Adaptive Cards for MCP-based plugins, defining inputs, layouts, and actions for interactive Copilot experiences.

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
- [Adaptive Card Types](#adaptive-card-types)
  - [Static Response Templates](#static-response-templates)
- [Response Semantics Properties](#response-semantics-properties)
  - [data_pathJSONPath query indicating where data resides in API response:](#data_pathjsonpath-query-indicating-where-data-resides-in-api-response:)
  - [propertiesMap response fields for Copilot citations:](#propertiesmap-response-fields-for-copilot-citations:)
  - [template_selectorProperty on each item indicating which template to use:](#template_selectorproperty-on-each-item-indicating-which-template-to-use:)
- [Adaptive Card Template Language](#adaptive-card-template-language)
  - [Conditional Rendering](#conditional-rendering)
- [Card Elements](#card-elements)
- [Responsive Design Best Practices](#responsive-design-best-practices)
  - [Single-Column Layouts](#single-column-layouts)
  - [Flexible Widths](#flexible-widths)
  - [Text and Images](#text-and-images)
  - [Test Across Hubs](#test-across-hubs)
- [Complete Example](#complete-example)
- [Workflow](#workflow)
- [Resources](#resources)
- [Common Patterns](#common-patterns)
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
- [Adaptive Card Types](#adaptive-card-types)
- [Static Response Templates](#static-response-templates)
- [Response Semantics Properties](#response-semantics-properties)
- [data_pathJSONPath query indicating where data resides in API response:](#data_pathjsonpath-query-indicating-where-data-resides-in-api-response:)
- [propertiesMap response fields for Copilot citations:](#propertiesmap-response-fields-for-copilot-citations:)
- [template_selectorProperty on each item indicating which template to use:](#template_selectorproperty-on-each-item-indicating-which-template-to-use:)
- [Adaptive Card Template Language](#adaptive-card-template-language)
- [Conditional Rendering](#conditional-rendering)
- [Card Elements](#card-elements)
- [Responsive Design Best Practices](#responsive-design-best-practices)
- [Single-Column Layouts](#single-column-layouts)
- [Flexible Widths](#flexible-widths)
- [Text and Images](#text-and-images)
- [Test Across Hubs](#test-across-hubs)
- [Complete Example](#complete-example)
- [Workflow](#workflow)
- [Resources](#resources)
- [Common Patterns](#common-patterns)
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





Use this prompt to handle the create adaptive cards for mcp plugins workflow.


Use when you need to create adaptive cards for mcp plugins for the current workspace or task.

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

## Adaptive Card Types

### Static Response Templates

> Use when API always returns items of the same type and format doesn't change oft

## Response Semantics Properties

### data_pathJSONPath query indicating where data resides in API response:

```json
"data_path": "$" // Root of response
"data_path": "$.results" // In results property
"data_path": "$.data.items"// Nested path
```

### propertiesMap response fields for Copilot citations:

```json
"properties": {
"title": "$.name", // Citation title
"subtitle": "$.description", // Citation subtitle
"url": "$.link" // Citation link
}
```

### template_selectorProperty on each item indicating which template to use:

```json
"template_selector": "$.displayTemplate"
```

## Adaptive Card Template Language

### Conditional Rendering

> "text": "${if(field, field, 'N/A')}" // Show field or 'N/A'

## Card Elements

> "text": "Text content",
> "size": "medium", // small, default, medium, large, extraLarge
> **Full content:**

## Responsive Design Best Practices

### Single-Column Layouts

- Use single columns for narrow viewports
- Avoid multi-column layouts when possible
- Ensure cards work at minimum viewport width

### Flexible Widths

- Don't assign fixed widths to elements
- Use "auto" or "stretch" for width properties
- Allow elements to resize with viewport
- Fixed widths OK for icons/avatars only

### Text and Images

- Avoid placing text and images in same row
- Exception: Small icons or avatars
- Use "wrap": true for text content
- Test at viewport widths

### Test Across Hubs

Validate cards in:

- Teams (desktop and mobile)- Word- PowerPoint- viewport widths (contract/expand UI)

## Complete Example

> "name": "SearchProjects",
> "description": "Search for projects with status and details",
> **Full content:**

## Workflow

Ask the user:1. What type of data does the API return?2. Are all items the same type (static) or different types (dynamic)?3. What fields should appear in the card?4. Should there be actions (e.g., "View Details")?5. Are there multiple states or categories requiring different templates?Then generate:- Appropriate response_semantics configuration- Static template, dynamic templates, or both- Proper data binding with conditional rendering- Responsive single-column layout- Test scenarios for validation

## Resources

- [Adaptive Card Designer](https://adaptivecards.microsoft.com/designer) - Visual design tool- [Adaptive Card Schema](https://adaptivecards.io/schemas/adaptive-card.json) - Full schema reference- [Template Language](https://learn.microsoft.com/en-us/adaptive-cards/templating/language) - Binding syntax guide- [JSONPath](https://www.rfc-editor.org/rfc/rfc9535) - Path query syntax

## Common Patterns

> "url": "${thumbnailUrl}",
> "$when": "${thumbnailUrl != null}"

## Template References

Detailed templates in `templates/mcp-create-adaptive-cards/`:- `adaptive_card_template_languag.md`- `adaptive_card_types.md`- `card_elements.md`- `common_patterns.md`- `complete_example.md`

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

- [`mcp-create-declarative-agent.prompt.md`](mcp-create-declarative-agent.prompt.md)
- [`mcp-deploy-manage-agents.prompt.md`](mcp-deploy-manage-agents.prompt.md)