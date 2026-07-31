---

name: mcp-create-adaptive-cards

title: Create Adaptive Cards for MCP Plugins

description: mcp-create-adaptive-cards.prompt.

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

  - web

scripts: []

skills: []

formatter: default

plan: None

tags:

  - generator

  - mcp

  - ml

  - prompts

  - specification

  - typescript

  - workflow

trigger: /mcp-create-adaptive-cards

dependencies: []

metadata:

  hermes: {}

---

## Goal

Use this prompt to handle the create adaptive cards for mcp plugins workflow.

## Context

Use when you need to create adaptive cards for mcp plugins for the current workspace or task.

## Input

s

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Output

s

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

## Adaptive Card Types

### Static Response Templates

> Use when API always returns items of the same type and format doesn't change oft

## Response Semantics Properties

### data_pathJSONPath query indicating where data resides in API response:```json"data_path": "$"           // Root of response"data_path": "$.results"   // In results property"data_path": "$.data.items"// Nested path```

### propertiesMap response fields for Copilot citations:```json"properties": {  "title": "$.name",            // Citation title  "subtitle": "$.description",  // Citation subtitle  "url": "$.link"               // Citation link}```

### template_selectorProperty on each item indicating which template to use:```json"template_selector": "$.displayTemplate"```

## Adaptive Card Template Language

### Conditional Rendering

> "text": "${if(field, field, 'N/A')}"  // Show field or 'N/A'

## Card Elements

> "text": "Text content",
> "size": "medium",      // small, default, medium, large, extraLarge
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
- Test at various viewport widths

### Test Across Hubs

Validate cards in:

- Teams (desktop and mobile)- Word- PowerPoint- Various viewport widths (contract/expand UI)

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

## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

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
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

mcp-create-adaptive-cards.prompt.

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
