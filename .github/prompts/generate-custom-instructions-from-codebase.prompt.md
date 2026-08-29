---
name: generate-custom-instructions-from-codebase
title: Generate Copilot Instructions From Codebase
description: Analyzes differences between two project versions (branches, commits, or releases) and produces migration/refactor instructions for GitHub Copilot to maintain consistency during upgrades.
trigger: /generate-custom-instructions-from-codebase
version: 1.0.0
author: Hermes Agent
date: '2026-08-25'
tags:
  - github
  - copilot
  - migration
  - refactor
  - tooling
  - documentation
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
- [Configuration Variables](#configuration-variables)
- [Generated Prompt](#generated-prompt)
  - [Phase 1: Comparative State Analysis](#phase-1:-comparative-state-analysis)
- [Migration Context](#migration-context)
- [Automatic Transformation Rules](#automatic-transformation-rules)
  - [1. Mandatory Transformations](#1-mandatory-transformations)
- [File Type Specific Instructions$](#file-type-specific-instructions$)
  - [Configuration Files](#configuration-files)
  - [Main Source Files](#main-source-files)
  - [Test Files](#test-files)
- [Validation and Security](#validation-and-security)
  - [Automatic Control Points](#automatic-control-points)
  - [Manual Escalation](#manual-escalation)
- [Migration Monitoring](#migration-monitoring)
- [Typical Use Cases](#typical-use-cases)
  - [Framework Version Migration](#framework-version-migration)
  - [Technology Stack Evolution](#technology-stack-evolution)
  - [Architecture Refactoring](#architecture-refactoring)
  - [Design Pattern Modernization](#design-pattern-modernization)
- [Unique Benefits](#unique-benefits)
  - [🧠 **Artificial Intelligence Enhancement**](#🧠-**artificial-intelligence-enhancement**)
  - [🔄 **Knowledge Capitalization**](#🔄-**knowledge-capitalization**)
  - [🎯 **Context-Aware Precision**](#🎯-**context-aware-precision**)
  - [⚡ **Automated Consistency**](#⚡-**automated-consistency**)
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
- [Configuration Variables](#configuration-variables)
- [Generated Prompt](#generated-prompt)
- [Phase 1: Comparative State Analysis](#phase-1:-comparative-state-analysis)
- [Migration Context](#migration-context)
- [Automatic Transformation Rules](#automatic-transformation-rules)
- [1. Mandatory Transformations](#1-mandatory-transformations)
- [File Type Specific Instructions$](#file-type-specific-instructions$)
- [Configuration Files](#configuration-files)
- [Main Source Files](#main-source-files)
- [Test Files](#test-files)
- [Validation and Security](#validation-and-security)
- [Automatic Control Points](#automatic-control-points)
- [Manual Escalation](#manual-escalation)
- [Migration Monitoring](#migration-monitoring)
- [Typical Use Cases](#typical-use-cases)
- [Framework Version Migration](#framework-version-migration)
- [Technology Stack Evolution](#technology-stack-evolution)
- [Architecture Refactoring](#architecture-refactoring)
- [Design Pattern Modernization](#design-pattern-modernization)
- [Unique Benefits](#unique-benefits)
- [🧠 **Artificial Intelligence Enhancement**](#🧠-**artificial-intelligence-enhancement**)
- [🔄 **Knowledge Capitalization**](#🔄-**knowledge-capitalization**)
- [🎯 **Context-Aware Precision**](#🎯-**context-aware-precision**)
- [⚡ **Automated Consistency**](#⚡-**automated-consistency**)
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





Migration and code evolution instructions generator for GitHub Copilot. Analyzes differences between two project versions (branches, commits, or releases) to create precise instructions allowing Copilot to maintain consistency during technology migrations, major refactoring, or framework version upgrades.


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

## Configuration Variables

```

${MIGRATION_TYPE="Framework Version|Architecture Refactoring|Technology Migration|Dependencies Update|Pattern Changes"}<!-- Type of migration or evolution -->${SOURCE_REFERENCE="branch|commit|tag"}<!-- Source reference point (before state) -->${TARGET_REFERENCE="branch|commit|tag"}<!-- Target reference point (after state) -->${ANALYSIS_SCOPE="Entire project|Specific folder|Modified files only"}<!-- Scope of analysis -->${CHANGE_FOCUS="Breaking Changes|New Conventions|Obsolete Patterns|API Changes|Configuration"}<!-- Main aspect of changes -->${AUTOMATION_LEVEL="Conservative|Balanced|Aggressive"}<!-- Level of automation for Copilot suggestions -->${GENERATE_EXAMPLES="true|false"}<!-- Include transformation examples -->${VALIDATION_REQUIRED="true|false"}<!-- Require validation before application -->
```

## Generated Prompt

> "Analyze code evolution between two project states to generate precise migration>>

### Phase 1: Comparative State Analysis

## Migration Context

- **Type**: ${MIGRATION_TYPE}- **From**: ${SOURCE_REFERENCE}- **To**: ${TARGET_REFERENCE}- **Date**: [GENERATION_DATE]- **Scope**: ${ANALYSIS_SCOPE}

## Automatic Transformation Rules

### 1. Mandatory Transformations

>
> ${AUTOMATION_LEVEL != "Conservative" ?
> **Full content:**

## File Type Specific Instructions$

GENERATE_EXAMPLES == "true" ? "

### Configuration Files

[CONFIG_TRANSFORMATION_EXAMPLES]

### Main Source Files

[SOURCE_TRANSFORMATION_EXAMPLES]

### Test Files

[TEST_TRANSFORMATION_EXAMPLES]" : ""}

## Validation and Security

### Automatic Control Points

- Verifications to perform after each transformation
- Tests to run to validate changes
- Performance metrics to monitor
- Compatibility checks to perform

### Manual Escalation

Situations requiring human intervention:

- [COMPLEX_CASES_LIST]- [ARCHITECTURAL_DECISIONS]- [BUSINESS_IMPACTS]

## Migration Monitoring

> - Percentage of code automatically migrated
> - Number of manual validations required
> **Full content:**

## Typical Use Cases

### Framework Version Migration

Perfect for documenting the transition from Angular 14 to Angular 17, React Class Components to Hooks, or .NET Framework to .NET Core. Automatically identifies breaking changes and generates corresponding transformation rules.

### Technology Stack Evolution

Essential when replacing a technology entirely: jQuery to React, REST to GraphQL, SQL to NoSQL. Creates a complete migration guide with pattern mappings.

### Architecture Refactoring

Ideal for large refactorings like Monolith to Microservices, MVC to Clean Architecture, or Component to Composable architecture. Preserves architectural knowledge for future similar transformations.

### Design Pattern Modernization

Useful for adopting new patterns: Repository Pattern, Dependency Injection, Observer to Reactive Programming. Documents the rationale and implementation differences.

## Unique Benefits

### 🧠 **Artificial Intelligence Enhancement**

Unlike traditional migration documentation, these instructions "train" GitHub Copilot to reproduce your technology evolution decisions automatically during future code modifications.

### 🔄 **Knowledge Capitalization**

Transforms specific project experience into reusable rules, avoiding the loss of migration expertise and accelerating future similar transformations.

### 🎯 **Context-Aware Precision**

Instead of generic advice, generates instructions tailored to your specific codebase, with real before/after examples from your project evolution.

### ⚡ **Automated Consistency**

Ensures that new code additions automatically follow the new conventions, preventing architectural regression and maintaining code evolution coherence.

## Template References

Detailed templates in `templates/generate-custom-instructions-from-codebase/`:- `automatic_transformation_rules.md`- `generated_prompt.md`- `migration_monitoring.md`

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

- [`generate-docs.prompt.md`](generate-docs.prompt.md)