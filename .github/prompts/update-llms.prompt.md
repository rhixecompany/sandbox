---
name: update-llms
title: Update llms.txt
description: Update the llms.txt file in the repository root to reflect changes in documentation or specifications following the llms.txt specification.
trigger: /update-llms
version: 1.0.0
author: Hermes Agent
tags:
  - documentation
  - llms
  - discovery
  - ai-ready
  - maintenance
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
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: markdown
license: MIT
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
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [Primary Directive](#primary-directive)
- [Analysis and Planning Phase](#analysis-and-planning-phase)
  - [Step 1: Review Current File and Specification](#step-1:-review-current-file-and-specification)
- [Implementation Requirements](#implementation-requirements)
  - [Format Compliance](#format-compliance)
- [Execution Steps](#execution-steps)
  - [Step 1: Current State Analysis](#step-1:-current-state-analysis)
- [Quality Assurance](#quality-assurance)
  - [Format Validation](#format-validation)
  - [Content Validation](#content-validation)
  - [Specification Compliance](#specification-compliance)
- [Update Strategy](#update-strategy)
- [Documentation](#documentation)
- [Specifications](#specifications)
- [Examples](#examples)
- [Configuration](#configuration)
- [Optional](#optional)
- [Success Criteria](#success-criteria)
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
- [Primary Directive](#primary-directive)
- [Analysis and Planning Phase](#analysis-and-planning-phase)
- [Step 1: Review Current File and Specification](#step-1:-review-current-file-and-specification)
- [Implementation Requirements](#implementation-requirements)
- [Format Compliance](#format-compliance)
- [Execution Steps](#execution-steps)
- [Step 1: Current State Analysis](#step-1:-current-state-analysis)
- [Quality Assurance](#quality-assurance)
- [Format Validation](#format-validation)
- [Content Validation](#content-validation)
- [Specification Compliance](#specification-compliance)
- [Update Strategy](#update-strategy)
- [Documentation](#documentation)
- [Specifications](#specifications)
- [Examples](#examples)
- [Configuration](#configuration)
- [Optional](#optional)
- [Success Criteria](#success-criteria)
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





Update the llms.txt file in the root folder to reflect changes in documentation or specifications following the llms.txt specification at <https://llmstxt.org/>.


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

## Primary Directive

Update the existing `llms.txt` file to maintain accuracy and compliance with the llms.txt specification while reflecting current repository structure and content. The file must remain optimized for LLM consumption while staying human-readable.

## Analysis and Planning Phase

> Before updating the `llms.txt` file, you must complete a thorough analysis:>>

### Step 1: Review Current File and Specification

## Implementation Requirements

### Format Compliance

> The updated `llms.txt` file must maintain this exact structure per the specifica

## Execution Steps

### Step 1: Current State Analysis

> 1. Read the existing `llms.txt` file thoroughly

## Quality Assurance

### Format Validation

- ✅ H1 header with project name- ✅ Blockquote summary (if included)- ✅ H2 sections for file lists- ✅ Proper markdown link format- ✅ No broken or invalid links- ✅ Consistent formatting throughout

### Content Validation

- ✅ Clear, unambiguous language- ✅ Comprehensive coverage of essential files- ✅ Logical organization of content- ✅ Appropriate file descriptions- ✅ Serves as effective LLM navigation tool

### Specification Compliance

- ✅ Follows <https://llmstxt.org/> format exactly- ✅ Uses required markdown structure- ✅ Implements optional sections appropriately- ✅ File located at repository root (`/llms.txt`)

## Update Strategy

> When adding new content:>
>
> 1. Identify the appropriate section for new files
> **Full content:**

## Documentation

- [Main README](README.md): Primary project documentation and getting started guide- [Contributing Guide](CONTRIBUTING.md): Guidelines for contributing to the project- [Code of Conduct](CODE_OF_CONDUCT.md): Community guidelines and expectations

## Specifications

- [Technical Specification](spec/technical-spec.md): Detailed technical requirements and constraints- [API Specification](spec/api-spec.md): Interface definitions and data contracts

## Examples

- [Basic Example](examples/basic-usage.md): Simple usage demonstration- [Advanced Example](examples/advanced-usage.md): Complex implementation patterns

## Configuration

- [Setup Guide](docs/setup.md): Installation and configuration instructions- [Deployment Guide](docs/deployment.md): Production deployment guidelines

## Optional

- [Architecture Documentation](docs/architecture.md): Detailed system architecture
- [Design Decisions](docs/decisions.md): Historical design decision records```

## Success Criteria

The updated `llms.txt` file should:1. Accurately reflect the current repository structure and content2. Maintain compliance with the llms.txt specification3. Provide clear navigation to essential documentation4. Remove outdated or incorrect references5. Include new important files and documentation6. Maintain logical organization for easy LLM consumption7. Use clear, unambiguous language throughout8. Continue to serve both human and machine readers effectively

## Template References

Detailed templates in `templates/update-llms/`:- `analysis_and_planning_phase.md`- `execution_steps.md`- `implementation_requirements.md`- `update_strategy.md`

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
- [`update-markdown-file-index.prompt.md`](update-markdown-file-index.prompt.md)
- [`update-oo-component-documentation.prompt.md`](update-oo-component-documentation.prompt.md)
- [`update-specification.prompt.md`](update-specification.prompt.md)