---
name: aspnet-minimal-api-openapi
title: ASP.NET Minimal API with OpenAPI
description: Create ASP.NET Minimal API endpoints with proper OpenAPI documentation.
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
  - api
  - documentation
  - prompts
  - specification
  - typescript
  - csharp
  - dotnet
trigger: /aspnet-minimal-api-openapi
dependencies: []
metadata:
  hermes: {}
---

## Goal

Create ASP.NET Minimal API endpoints with proper OpenAPI documentation.

# ASP.NET Minimal API with OpenAPIYour goal is to help me create well-structured ASP.NET Minimal API endpoints with correct types and comprehensive OpenAPI/Swagger documentation.

## API Organization

- Group related endpoints using `MapGroup()` extension- Use endpoint filters for cross-cutting concerns- Structure larger APIs with separate endpoint classes- Consider using a feature-based folder structure for complex APIs

## Request and Response Types

- Define explicit request and response DTOs/models- Create clear model classes with proper validation attributes- Use record types for immutable request/response objects- Use meaningful property names that align with API design standards- Apply `[Required]` and other validation attributes to enforce constraints- Use the ProblemDetailsService and StatusCodePages to get standard error responses

## Type Handling

- Use strongly-typed route parameters with explicit type binding- Use `Results<T1, T2

> ` to represent multiple response types- Return `TypedResults` instead of `Results` for strongly-typed responses- Leverage C# 10+ features like nullable annotations and init-only properties

## OpenAPI Documentation

- Use the built-in OpenAPI document support added in .NET 9- Define operation summary and description- Add operationIds using the `WithName` extension method- Add descriptions to properties and parameters with `[Description()]`- Set proper content types for requests and responses- Use document transformers to add elements like servers, tags, and security schemes- Use schema transformers to apply customizations to OpenAPI schemas

## Template References

Templates in `templates/aspnet-minimal-api-openapi/`:- `api_organization.md`- `openapi_documentation.md`- `request_and_response_type.md`- `type_handling.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
|| ------- | ----------- ||
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

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

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
|| --- | ------ | ----------- ||
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
|| ------- | --------- ||
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
