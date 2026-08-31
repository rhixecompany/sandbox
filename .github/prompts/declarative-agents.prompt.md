---
name: declarative-agents
title: Declarative Agents
description: Build declarative Microsoft 365 / Copilot agents with workflows for basic creation, advanced enterprise design, and validation & optimization.
trigger: /declarative-agents
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
Build declarative Microsoft 365 / Copilot agents with workflows for basic creation, advanced enterprise design, and validation & optimization.

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
- [Workflow 1: Basic Agent Creation](#workflow-1:-basic-agent-creation)
- [Workflow 2: Advanced Enterprise Agent Design](#workflow-2:-advanced-enterprise-agent-design)
- [Workflow 3: Validation & Optimization](#workflow-3:-validation-&-optimization)
- [Core Features Across All Workflows](#core-features-across-all-workflows)
  - [Microsoft 365 Agents Toolkit Integration](#microsoft-365-agents-toolkit-integration)
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
- [Workflow 1: Basic Agent Creation](#workflow-1:-basic-agent-creation)
- [Workflow 2: Advanced Enterprise Agent Design](#workflow-2:-advanced-enterprise-agent-design)
- [Workflow 3: Validation & Optimization](#workflow-3:-validation-&-optimization)
- [Core Features Across All Workflows](#core-features-across-all-workflows)
- [Microsoft 365 Agents Toolkit Integration](#microsoft-365-agents-toolkit-integration)
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





Complete development kit for Microsoft 365 Copilot declarative agents with three comprehensive workflows (basic, advanced, validation), TypeSpec support, and Microsoft 365 Agents Toolkit integration.


Use when you need to declarative agents for the current workspace or task.

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

## Workflow 1: Basic Agent Creation

**Perfect for**: New developers, simple agents, quick prototypesI'll guide you through:1. **Agent Planning**: Define purpose, target users, and core capabilities2. **Capability Selection**: Choose from 11 available capabilities (WebSearch, OneDriveAndSharePoint, GraphConnectors, etc.)3. **Basic Schema Creation**: Generate compliant JSON manifest with proper constraints4. **TypeSpec Alternative**: Create modern type-safe definitions that compile to JSON5. **Testing Setup**: Configure Agents Playground for local testing6. **Toolkit Integration**: use Microsoft 365 Agents Toolkit for enhanced development

## Workflow 2: Advanced Enterprise Agent Design

**Perfect for**: Complex enterprise scenarios, production deployment, advanced featuresI'll help you architect:1. **Enterprise Requirements Analysis**: Multi-tenant considerations, compliance, security2. **Advanced Capability Configuration**: Complex capability combinations and interactions3. **Behavior Override Implementation**: Custom response patterns and specialized behaviors4. **Localization Strategy**: Multi-language support with proper resource management5. **Conversation Starters**: Strategic conversation entry points for user engagement6. **Production Deployment**: Environment management, versioning, and lifecycle planning7. **Monitoring & Analytics**: Implementation of tracking and performance optimization

## Workflow 3: Validation & Optimization

**Perfect for**: Existing agents, troubleshooting, performance optimizationI'll perform:1. **Schema Compliance Validation**: Full v1.5 specification adherence checking2. **Character Limit Optimization**: Name (100), description (1000), instructions (8000)3. **Capability Audit**: Verify proper capability configuration and usage4. **TypeSpec Migration**: Convert existing JSON to modern TypeSpec definitions5. **Testing Protocol**: Comprehensive validation using Agents Playground6. **Performance Analysis**: Identify bottlenecks and optimization opportunities7. **Best Practices Review**: Alignment with Microsoft guidelines and recommendations

## Core Features Across All Workflows

### Microsoft 365 Agents Toolkit Integration

> - **VS Code Extension**: Full integration with `teamsdevapp.ms-teams-vscode-exte

## Template References

Detailed templates in `templates/declarative-agents/`:- `core_features_across_all_workf.md`

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
```
# Prompt template
Execute the workflow defined in this file.
```
