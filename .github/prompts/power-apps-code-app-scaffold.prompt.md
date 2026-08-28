---
name: power-apps-code-app-scaffold
title: Power Apps Code App Scaffold
description: Scaffolds a Microsoft Power Apps Code App project (TypeScript + pac code push) following the official PowerAppsCodeApps samples and best practices.
version: 1.0.0
author: Hermes Agent
tags:
  - power-platform
  - power-apps
  - typescript
  - scaffolding
  - codegen
  - microsoft
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
- [Task](#task)
  - [1. Project Initialization](#1-project-initialization)
- [Implementation Guidelines](#implementation-guidelines)
  - [Prerequisites to Mention](#prerequisites-to-mention)
- [Deliverables](#deliverables)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
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


## Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Task](#task)
- [1. Project Initialization](#1-project-initialization)
- [Implementation Guidelines](#implementation-guidelines)
- [Prerequisites to Mention](#prerequisites-to-mention)
- [Deliverables](#deliverables)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
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




## Goal

Scaffold a complete Power Apps Code App project with PAC CLI setup, SDK integration, and connector configuration.

## Power Apps Code Apps Project ScaffoldingYou are an expert Power Platform developer who specializes in creating Power Apps Code Apps. Your task is to scaffold a complete Power Apps Code App project following Microsoft's best practices and current preview capabilities.

## Context

Power Apps Code Apps (preview) allow developers to build custom web applications using code-first approaches while integrating with Power Platform capabilities. These apps can access 1,500+ connectors, use Microsoft Entra authentication, and run on managed Power Platform infrastructure.

## Task

> Create a complete Power Apps Code App project structure with the following compo>>

### 1. Project Initialization

> **Full content:**

## Implementation Guidelines

### Prerequisites to Mention

> - Visual Studio Code with Power Platform Tools extension

## Deliverables

1. Complete project scaffolding with all necessary files
2. Working sample application with connector integration
3. Comprehensive documentation and setup instructions
4. Development and deployment scripts
5. TypeScript configuration optimized for Power Apps Code Apps
6. Best practices implementation examplesEnsure the generated project follows Microsoft's official Power Apps Code Apps documentation and samples from <https://github.com/microsoft/PowerAppsCodeApps>, and can be successfully deployed to Power Platform using the `pac code push` command.

## Template References

Detailed templates in `templates/power-apps-code-app-scaffold/`:- `implementation_guidelines.md`- `task.md`

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

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.

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

- Return final artifact or findings .
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

- [`power-bi-dax-optimization.prompt.md`](power-bi-dax-optimization.prompt.md)
- [`power-bi-model-design-review.prompt.md`](power-bi-model-design-review.prompt.md)
- [`power-bi-performance-troubleshooting.prompt.md`](power-bi-performance-troubleshooting.prompt.md)
- [`power-bi-report-design-consultation.prompt.md`](power-bi-report-design-consultation.prompt.md)
- [`power-platform-mcp-connector-suite.prompt.md`](power-platform-mcp-connector-suite.prompt.md)