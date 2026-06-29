---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create Adaptive Cards for MCP Plugins
name: mcp-create-adaptive-cards
description: "mcp-create-adaptive-cards.prompt"
tags:
  - generator
  - mcp
  - ml
  - prompts
  - specification
  - typescript
  - workflow
  - adaptive-cards
  - documentation
  - orchestration
  - planning
  - specification
  - workflow
---

## Goal

Use this prompt to handle the create adaptive cards for mcp plugins workflow.

## Context

Use when you need to create adaptive cards for mcp plugins for the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


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

## Adaptive Card Types

> ### Static Response Templates
> Use when API always returns items of the same type and format doesn't change oft

> **Full content:** `templates/mcp-create-adaptive-cards/adaptive_card_types.md`

## Response Semantics Properties

### data_path
JSONPath query indicating where data resides in API response:
```json
"data_path": "$"           // Root of response
"data_path": "$.results"   // In results property
"data_path": "$.data.items"// Nested path
```

### properties
Map response fields for Copilot citations:
```json
"properties": {
  "title": "$.name",            // Citation title
  "subtitle": "$.description",  // Citation subtitle
  "url": "$.link"               // Citation link
}
```

### template_selector
Property on each item indicating which template to use:
```json
"template_selector": "$.displayTemplate"
```

## Adaptive Card Template Language

> ### Conditional Rendering
> "text": "${if(field, field, 'N/A')}"  // Show field or 'N/A'

> **Full content:** `templates/mcp-create-adaptive-cards/adaptive_card_template_languag.md`

## Card Elements

> "text": "Text content",
> "size": "medium",      // small, default, medium, large, extraLarge

> **Full content:** `templates/mcp-create-adaptive-cards/card_elements.md`

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
- Test at various viewport widths

### Test Across Hubs
Validate cards in:
- Teams (desktop and mobile)
- Word
- PowerPoint
- Various viewport widths (contract/expand UI)

## Complete Example

> "name": "SearchProjects",
> "description": "Search for projects with status and details",

> **Full content:** `templates/mcp-create-adaptive-cards/complete_example.md`

## Workflow

Ask the user:
1. What type of data does the API return?
2. Are all items the same type (static) or different types (dynamic)?
3. What fields should appear in the card?
4. Should there be actions (e.g., "View Details")?
5. Are there multiple states or categories requiring different templates?

Then generate:
- Appropriate response_semantics configuration
- Static template, dynamic templates, or both
- Proper data binding with conditional rendering
- Responsive single-column layout
- Test scenarios for validation

## Resources

- [Adaptive Card Designer](https://adaptivecards.microsoft.com/designer) - Visual design tool
- [Adaptive Card Schema](https://adaptivecards.io/schemas/adaptive-card.json) - Full schema reference
- [Template Language](https://learn.microsoft.com/en-us/adaptive-cards/templating/language) - Binding syntax guide
- [JSONPath](https://www.rfc-editor.org/rfc/rfc9535) - Path query syntax

## Common Patterns

> "url": "${thumbnailUrl}",
> "$when": "${thumbnailUrl != null}"

> **Full content:** `templates/mcp-create-adaptive-cards/common_patterns.md`

## Template References

Detailed templates in `templates/mcp-create-adaptive-cards/`:
- `adaptive_card_template_languag.md`
- `adaptive_card_types.md`
- `card_elements.md`
- `common_patterns.md`
- `complete_example.md`
