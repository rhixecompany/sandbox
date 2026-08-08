---
name: csharp-async
title: 'C# Async Programming Best Practices'
description: 'Get best practices for C# async programming.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - terminal
  - file
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - csharp
  - data
  - dotnet
  - fix
  - performance
  - prompts
  - typescript
trigger: /csharp-async
dependencies: []
metadata:
  hermes: {}
---

## Goal

Get best practices for C# async programming.

# C# Async Programming Best PracticesYour goal is to help me follow best practices for asynchronous programming in C#.

## Naming Conventions

- Use the 'Async' suffix for all async methods- Match method names with their synchronous counterparts when applicable (e.g., `GetDataAsync()` for `GetData()`)

## Return Types

- Return `Task<T

> ` when the method returns a value- Return `Task` when the method doesn't return a value- Consider `ValueTask<T>` for high-performance scenarios to reduce allocations- Avoid returning `void` for async methods except for event handlers

## Exception Handling

- Use try/catch blocks around await expressions- Avoid swallowing exceptions in async methods- Use `ConfigureAwait(false)` when appropriate to prevent deadlocks in library code- Propagate exceptions with `Task.FromException()` instead of throwing in async Task returning methods

## Performance

- Use `Task.WhenAll()` for parallel execution of multiple tasks
- Use `Task.WhenAny()` for implementing timeouts or taking the first completed task
- Avoid unnecessary async/await when simply passing through task results
- Consider cancellation tokens for long-running operations

## Common Pitfalls

- Never use `.Wait()`, `.Result`, or `.GetAwaiter().GetResult()` in async code- Avoid mixing blocking and async code- Don't create async void methods (except for event handlers)- Always await Task-returning methods

## Implementation Patterns

- Implement the async command pattern for long-running operations- Use async streams (IAsyncEnumerable<T

> ) for processing sequences asynchronously- Consider the task-based asynchronous pattern (TAP) for public APIsWhen reviewing my C# code, identify these issues and suggest improvements that follow these best practices.

## Template References

Templates in `templates/csharp-async/`:- `common_pitfalls.md`- `exception_handling.md`- `implementation_patterns.md`- `performance.md`- `return_types.md`

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
