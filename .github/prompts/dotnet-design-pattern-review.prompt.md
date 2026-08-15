---
name: dotnet-design-pattern-review
title: dotnet design pattern review
description: Prompt for dotnet-design-pattern-review
version: "1.0.0"
tags: [architecture, csharp, design-patterns, dotnet, review]
trigger: dotnet-design-pattern-review
metadata:
  hermes:
    profile: default
    priority: medium
    categories: []
  copilot:
    model_required: claude-opus
    context_length: medium
  opencode:
    enabled: true
    compatibility: compatible
  codex:
    enabled: false
    model_preferred: text-davinci-003

---
name: dotnet-design-pattern-review
title: .NET/C# Design Pattern Review
description: Review the C#/.NET code for design pattern implementation and suggest
  improvements.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- file
- terminal
scripts: []
skills: []
formatter: default
plan: null
tags:
- architecture
- audit
- csharp
- dotnet
- frontend
- prompts
- typescript
- architecture
- audit
- csharp
- dotnet
- frontend
- prompts
- typescript
trigger: /dotnet-design-pattern-review
dependencies: []
metadata:
  hermes: {}
name: dotnet-design-pattern-review
title: .NET/C# Design Pattern Review
description: Review the C#/.NET code for design pattern implementation and suggest
  improvements.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- file
- terminal
scripts: []
skills: []
formatter: default
plan: null
tags:
- architecture
- audit
- csharp
- dotnet
- frontend
- prompts
- typescript
- architecture
- audit
- csharp
- dotnet
- frontend
- prompts
- typescript
trigger: /dotnet-design-pattern-review
dependencies: []
metadata:
  hermes: {}
---

## Goal

Review the C#/.NET code for design pattern implementation and suggest improvements.

# .NET/C# Design Pattern ReviewReview the C#/.NET code in ${selection} for design pattern implementation and suggest improvements for the solution/project. Do not make any changes to the code, just provide a review.

## Required Design Patterns

- **Command Pattern**: Generic base classes (`CommandHandler<TOptions

> `),`ICommandHandler<TOptions>` interface, `CommandHandlerOptions` inheritance, static `SetupCommand(IHost host)` methods- **Factory Pattern**: Complex object creation service provider integration- **Dependency Injection**: Primary constructor syntax, `ArgumentNullException` null checks, interface abstractions, proper service lifetimes- **Repository Pattern**: Async data access interfaces provider abstractions for connections- **Provider Pattern**: External service abstractions (database, AI), clear contracts, configuration handling- **Resource Pattern**: ResourceManager for localized messages, separate .resx files (LogMessages, ErrorMessages)

## Review Checklist

- **Design Patterns**: Identify patterns used. Are Command Handler, Factory, Provider, and Repository patterns correctly implemented? Missing beneficial patterns?- **Architecture**: Follow namespace conventions (`{Core|Console|App|Service}.{Feature}`)? Proper separation between Core/Console projects? Modular and readable?- **.NET Best Practices**: Primary constructors, async/await with Task returns, ResourceManager usage, structured logging, strongly-typed configuration?- **GoF Patterns**: Command, Factory, Template Method, Strategy patterns correctly implemented?- **SOLID Principles**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion violations?- **Performance**: Proper async/await, resource disposal, ConfigureAwait(false), parallel processing opportunities?- **Maintainability**: Clear separation of concerns, consistent error handling, proper configuration usage?- **Testability**: Dependencies abstracted via interfaces, mockable components, async testability, AAA pattern compatibility?- **Security**: Input validation, secure credential handling, parameterized queries, safe exception handling?- **Documentation**: XML docs for public APIs, parameter/return descriptions, resource file organization?- **Code Clarity**: Meaningful names reflecting domain concepts, clear intent through patterns, self-explanatory structure?- **Clean Code**: Consistent style, appropriate method/class size, minimal complexity, eliminated duplication?

## Improvement Focus Areas

- **Command Handlers**: Validation in base class, consistent error handling, proper resource management- **Factories**: Dependency configuration, service provider integration, disposal patterns- **Providers**: Connection management, async patterns, exception handling and logging- **Configuration**: Data annotations, validation attributes, secure sensitive value handling- **AI/ML Integration**: Semantic Kernel patterns, structured output handling, model configurationProvide specific, actionable recommendations for improvements aligned with the project's architecture and .NET best practices.

## Template References

Templates in `templates/dotnet-design-pattern-review/`:- `improvement_focus_areas.md`- `required_design_patterns.md`- `review_checklist.md`

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`dotnet-best-practices.prompt.md`](dotnet-best-practices.prompt.md)
- [`dotnet-upgrade.prompt.md`](dotnet-upgrade.prompt.md)

