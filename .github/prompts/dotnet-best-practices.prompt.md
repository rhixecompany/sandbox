---
title: Goal
description: Prompt for goal
date: '2026-08-25'
tags:
- prompt
version: 1.0.0
author: Hermes Agent
---
# Table of Contents

- [Goal](#goal)
- [Documentation & Structure](#documentation-&-structure)
- [Design Patterns & Architecture](#design-patterns-&-architecture)
- [Dependency Injection & Services](#dependency-injection-&-services)
- [Resource Management & Localization](#resource-management-&-localization)
- [Async/Await Patterns](#async/await-patterns)
- [Test](#test)
- [Configuration & Settings](#configuration-&-settings)
- [Semantic Kernel & AI Integration](#semantic-kernel-&-ai-integration)
- [Error Handling & Logging](#error-handling-&-logging)
- [Performance & Security](#performance-&-security)
- [Code Quality](#code-quality)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
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
- [Documentation & Structure](#documentation-&-structure)
- [Design Patterns & Architecture](#design-patterns-&-architecture)
- [Dependency Injection & Services](#dependency-injection-&-services)
- [Resource Management & Localization](#resource-management-&-localization)
- [Async/Await Patterns](#async/await-patterns)
- [Test](#test)
- [Configuration & Settings](#configuration-&-settings)
- [Semantic Kernel & AI Integration](#semantic-kernel-&-ai-integration)
- [Error Handling & Logging](#error-handling-&-logging)
- [Performance & Security](#performance-&-security)
- [Code Quality](#code-quality)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
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

Ensure .NET/C# code meets best practices for the solution/project.

## .NET/C# Best PracticesYour task is to ensure .NET/C# code in ${selection} meets the best practices specific to this solution/project. This includes:

## Documentation & Structure

- Create comprehensive XML documentation comments for all public classes, interfaces, methods, and properties- Include parameter descriptions and return value descriptions in XML comments- Follow the established namespace structure: {Core|Console|App|Service}.{Feature}

## Design Patterns & Architecture

- Use primary constructor syntax for dependency injection (e.g., `public class MyClass(IDependency dependency)`)- Implement the Command Handler pattern with generic base classes (e.g., `CommandHandler<TOptions

> `)- Use interface segregation with clear naming conventions (prefix interfaces with 'I')- Follow the Factory pattern for complex object creation.

## Dependency Injection & Services

- Use constructor dependency injection with null checks via ArgumentNullException- Register services with appropriate lifetimes (Singleton, Scoped, Transient)- Use Microsoft.Extensions.DependencyInjection patterns- Implement service interfaces for testability

## Resource Management & Localization

- Use ResourceManager for localized messages and error strings- Separate LogMessages and ErrorMessages resource files- Access resources via `_resourceManager.GetString("MessageKey")`

## Async/Await Patterns

- Use async/await for all I/O operations and long-running tasks- Return Task or Task<T

> from async methods- Use ConfigureAwait(false) where appropriate- Handle async exceptions properly

## Test

ing Standards- Use MSTest framework with FluentAssertions for assertions- Follow AAA pattern (Arrange, Act, Assert)- Use Moq for mocking dependencies- Test both success and failure scenarios- Include null parameter validation tests

## Configuration & Settings

- Use strongly-typed configuration classes with data annotations- Implement validation attributes (Required, NotEmptyOrWhitespace)- Use IConfiguration binding for settings- Support appsettings.json configuration files

## Semantic Kernel & AI Integration

- Use Microsoft.SemanticKernel for AI operations- Implement proper kernel configuration and service registration- Handle AI model settings (ChatCompletion, Embedding, etc.)- Use structured output patterns for reliable AI responses

## Error Handling & Logging

- Use structured logging with Microsoft.Extensions.Logging- Include scoped logging with meaningful context- Throw specific exceptions with descriptive messages- Use try-catch blocks for expected failure scenarios

## Performance & Security

- Use C# 12+ features and .NET 8 optimizations where applicable- Implement proper input validation and sanitization- Use parameterized queries for database operations- Follow secure coding practices for AI/ML operations

## Code Quality

- Ensure SOLID principles compliance- Avoid code duplication through base classes and utilities- Use meaningful names that reflect domain concepts- Keep methods focused and cohesive- Implement proper disposal patterns for resources

## Template References

Templates in `templates/dotnet-best-practices/`:- `asyncawait_patterns.md`- `code_quality.md`- `configuration__settings.md`- `dependency_injection__ser.md`- `design_patterns__architec.md`- `documentation__structure.md`- `error_handling__logging.md`- `performance__security.md`- `resource_management__loca.md`- `semantic_kernel__ai_integ.md`- `testing_standards.md`

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

- [`dotnet-design-pattern-review.prompt.md`](dotnet-design-pattern-review.prompt.md)
- [`dotnet-upgrade.prompt.md`](dotnet-upgrade.prompt.md)