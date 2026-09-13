---
name: update-oo-component-documentation
title: Update Oo Component Documentation
description: Update existing object-oriented component documentation following industry best practices
  and architectural documentation standards.
version: 1.0.0
license: MIT
author: Hermes Agent
trigger: /update-oo-component-documentation
toolsets:
- web
skills: []
dependencies: []
formatter: default
metadata:
  hermes:
    profile: code-architect
    mcp_servers: []
    context_size: large
  copilot:
    context_size: large
    extensions: []
    keybinding: null
  opencode:
    command: opencode /update-oo-component-documentation
    flags: {}
    help: Update existing object-oriented component documentation following industry be...
  codex:
    model_override: null
    system_prompt_id: null
    temperature: null
    max_tokens: null
tags:
- agent-type:hermes
- architecture
- documentation
- maintenance
- ml
- prompts
- specification
- typescript
scripts: []
## Goal

Update existing object-oriented component documentation following industry best practices and architectural documentation standards.

## Context

Use when you need to work on the current workspace or task.

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

## 1. Component Overview

### Purpose

/Responsibility

- OVR-001: Update component's primary responsibility
- OVR-002: Refresh scope (included/excluded functionality)
- OVR-003: Update system context and relationships

## 2. Architecture Section

- ARC-001: Update design patterns used (Repository, Factory, Observer, etc.)
- ARC-002: Refresh internal and external dependencies with current purposes
- ARC-003: Update component interactions and relationships
- ARC-004: Update visual diagrams (UML class, sequence, component)
- ARC-005: Refresh mermaid diagram showing current component structure, relationships, and dependencies

### Component Structure and Dependencies Diagram

Update the mermaid diagram to show current:

- **Component structure** - Current classes, interfaces, and their relationships- **Internal dependencies** - How components currently interact within the system- **External dependencies** - Current external libraries, services, databases, APIs- **Data flow** - Current direction of dependencies and interactions- **Inheritance/composition** - Current class hierarchies and composition relationships```mermaid[Update diagram to reflect current architecture]```````

## 3. Interface Documentation

- INT-001: Update all public interfaces and current usage patterns- INT-002: Refresh method/property reference table with current API- INT-003: Update events/callbacks/notification mechanisms| Method/Property | Purpose | Parameters | Return Type | Usage Notes || --- | --- | --- | --- | --- || [Update table with current API] |  |  |  |  |

## 4. Implementation Details

- IMP-001: Update main implementation classes and current responsibilities- IMP-002: Refresh configuration requirements and initialization patterns- IMP-003: Update key algorithms and business logic- IMP-004: Update performance characteristics and bottlenecks

## 5. Usage Examples

### Basic Usage

```
csharp// Update basic usage example to current API
```

### Advanced Usage

```csharp
// Update advanced configuration patterns to current implementation```- USE-001: Update basic usage examples- USE-002: Refresh advanced configuration patterns- USE-003: Update best practices and recommended patterns

```

## 6. Quality Attributes

- QUA-001: Update security (authentication, authorization, data protection)- QUA-002: Refresh performance (characteristics, scalability, resource usage)- QUA-003: Update reliability (error handling, fault tolerance, recovery)- QUA-004: Refresh maintainability (standards, testing, documentation)- QUA-005: Update extensibility (extension points, customization options)

## 7. Reference Information

- REF-001: Update dependencies with current versions and purposes- REF-002: Refresh configuration options reference- REF-003: Update testing guidelines and mock setup- REF-004: Refresh troubleshooting (common issues, error messages)- REF-005: Update related documentation links- REF-006: Add change history and migration notes for this update``````

## Template References

Detailed templates in `templates/update-oo-component-documentation/`:- `legacy_prompt_details.md`

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

- [`update-avm-modules-in-bicep.prompt.md`](update-avm-modules-in-bicep.prompt.md)
- [`update-docs-on-code-change.prompt.md`](update-docs-on-code-change.prompt.md)
- [`update-implementation-plan.prompt.md`](update-implementation-plan.prompt.md)
- [`update-llms.prompt.md`](update-llms.prompt.md)
- [`update-markdown-file-index.prompt.md`](update-markdown-file-index.prompt.md)
- [`update-specification.prompt.md`](update-specification.prompt.md)