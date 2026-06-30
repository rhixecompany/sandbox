---
toolsets:
  - changes
  - search/codebase
  - edit/editFiles
  - problems
  - runCommands
license: MIT
author: Hermes Agent
version: 1.0.0
title: Entity Framework Core Best Practices
name: ef-core
description: "Get best practices for Entity Framework Core"
tags:
  - ml
  - prompts
  - specification
  - typescript
  - csharp
  - documentation
  - dotnet
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - ef-core.prompt

trigger: ef-core

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - ef-core.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - ef-core.prompt

## Goal

Get best practices for Entity Framework Core.

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

## Data Context Design

- Keep DbContext classes focused and cohesive
- Use constructor injection for configuration options
- Override OnModelCreating for fluent API configuration
- Separate entity configurations using IEntityTypeConfiguration
- Consider using DbContextFactory pattern for console apps or tests

## Entity Design

- Use meaningful primary keys (consider natural vs surrogate keys)
- Implement proper relationships (one-to-one, one-to-many, many-to-many)
- Use data annotations or fluent API for constraints and validations
- Implement appropriate navigational properties
- Consider using owned entity types for value objects

## Performance

- Use AsNoTracking() for read-only queries
- Implement pagination for large result sets with Skip() and Take()
- Use Include() to eager load related entities when needed
- Consider projection (Select) to retrieve only required fields
- Use compiled queries for frequently executed queries
- Avoid N+1 query problems by properly including related data

## Migrations

- Create small, focused migrations
- Name migrations descriptively
- Verify migration SQL scripts before applying to production
- Consider using migration bundles for deployment
- Add data seeding through migrations when appropriate

## Querying

- Use IQueryable judiciously and understand when queries execute
- Prefer strongly-typed LINQ queries over raw SQL
- Use appropriate query operators (Where, OrderBy, GroupBy)
- Consider database functions for complex operations
- Implement specifications pattern for reusable queries

## Change Tracking & Saving

- Use appropriate change tracking strategies
- Batch your SaveChanges() calls
- Implement concurrency control for multi-user scenarios
- Consider using transactions for multiple operations
- Use appropriate DbContext lifetimes (scoped for web apps)

## Security

- Avoid SQL injection by using parameterized queries
- Implement appropriate data access permissions
- Be careful with raw SQL queries
- Consider data encryption for sensitive information
- Use migrations to manage database user permissions

## Testing

- Use in-memory database provider for unit tests
- Create separate testing contexts with SQLite for integration tests
- Mock DbContext and DbSet for pure unit tests
- Test migrations in isolated environments
- Consider snapshot testing for model changes

When reviewing my EF Core code, identify issues and suggest improvements that follow these best practices.


## Template References

Templates in `templates/ef-core/`:
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
