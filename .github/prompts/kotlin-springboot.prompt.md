---
name: kotlin-springboot
title: Kotlin Spring Boot Best Practices
description: Provides best practices for developing applications with Spring Boot and Kotlin, including idiomatic patterns and configuration.
version: 1.0.0
author: Hermes Agent
date: '2026-08-25'
tags:
  - kotlin
  - spring-boot
  - backend
  - best-practices
  - web
  - configuration
  - idiomatic
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
- [Project Setup & Structure](#project-setup-&-structure)
- [Dependency Injection & Components](#dependency-injection-&-components)
- [Configuration](#configuration)
- [Web Layer (Controllers)](#web-layer-controllers)
- [Service Layer](#service-layer)
- [Data Layer (Repositories)](#data-layer-repositories)
- [Logging](#logging)
- [Test](#test)
- [Coroutines & Asynchronous Programming](#coroutines-&-asynchronous-programming)
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
- [Project Setup & Structure](#project-setup-&-structure)
- [Dependency Injection & Components](#dependency-injection-&-components)
- [Configuration](#configuration)
- [Web Layer (Controllers)](#web-layer-controllers)
- [Service Layer](#service-layer)
- [Data Layer (Repositories)](#data-layer-repositories)
- [Logging](#logging)
- [Test](#test)
- [Coroutines & Asynchronous Programming](#coroutines-&-asynchronous-programming)
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

Get best practices for developing applications with Spring Boot and Kotlin.

## Spring Boot with Kotlin Best PracticesYour goal is to help me write high-quality, idiomatic Spring Boot applications using Kotlin.

## Project Setup & Structure

- **Build Tool:** Use Maven (`pom.xml`) or Gradle (`build.gradle`) with the Kotlin plugins (`kotlin-maven-plugin` or `org.jetbrains.kotlin.jvm`).- **Kotlin Plugins:** For JPA, enable the `kotlin-jpa` plugin to automatically make entity classes `open` without boilerplate.
- **Starters:** Use Spring Boot starters (e.g., `spring-boot-starter-web`, `spring-boot-starter-data-jpa`) as usual.
- **Package Structure:** Organize code by feature/domain (e.g., `com.example.app.order`, `com.example.app.user`) rather than by layer.

## Dependency Injection & Components

- **Primary Constructors:** Always use the primary constructor for required dependency injection. It's the most idiomatic and concise approach in Kotlin.
- **Immutability:** Declare dependencies as `private val` in the primary constructor. Prefer `val` over `var` everywhere to promote immutability.
- **Component Stereotypes:** Use `@Service`, `@Repository`, and `@RestController` annotations just as you would in Java.

## Configuration

- **Externalized Configuration:** Use `application.yml` for its readability and hierarchical structure.
- **Type-Safe Properties:** Use `@ConfigurationProperties` with `data class` to create immutable, type-safe configuration objects.
- **Profiles:** Use Spring Profiles (`application-dev.yml`, `application-prod.yml`) to manage environment-specific configurations.
- **Secrets Management:** Never hardcode secrets. Use environment variables or a dedicated secret management tool like HashiCorp Vault or AWS Secrets Manager.

## Web Layer (Controllers)

- **RESTful APIs:** Design clear and consistent RESTful endpoints.
- **Data Classes for DTOs:** Use Kotlin `data class` for all DTOs. This provides `equals()`, `hashCode()`, `toString()`, and `copy()` for free and promotes immutability.
- **Validation:** Use Java Bean Validation (JSR 380) with annotations (`@Valid`, `@NotNull`, `@Size`) on your DTO data classes.
- **Error Handling:** Implement a global exception handler using `@ControllerAdvice` and `@ExceptionHandler` for consistent error responses.

## Service Layer

- **Business Logic:** Encapsulate business logic within `@Service` classes.
- **Statelessness:** Services should be stateless.
- **Transaction Management:** Use `@Transactional` on service methods. In Kotlin, this can be applied to class or function level.

## Data Layer (Repositories)

- **JPA Entities:** Define entities as classes. Remember they must be `open`. It's highly recommended to use the `kotlin-jpa` compiler plugin to handle this automatically.
- **Null Safety:** use Kotlin's null-safety (`?`) to define which entity fields are optional or required at the type level.
- **Spring Data JPA:** Use Spring Data JPA repositories by extending `JpaRepository` or `CrudRepository`.- **Coroutines:** For reactive applications, use Spring Boot's support for Kotlin Coroutines in the data layer.

## Logging

- **Companion Object Logger:** The idiomatic way to declare a logger is in a companion object. ```kotlin companion object { private val logger = LoggerFactory.getLogger(MyClass::class.java) }```- **Parameterized Logging:** Use parameterized messages (`logger.info("Processing user {}...", userId)`) for performance and clarity.

## Test

ing

- **JUnit 5:** JUnit 5 is the default and works seamlessly with Kotlin.
- **Idiomatic Testing Libraries:** For more fluent and idiomatic tests, consider using **Kotest** for assertions and **MockK** for mocking. They are designed for Kotlin and offer a more expressive syntax.
- **Test Slices:** Use test slice annotations like `@WebMvcTest` or `@DataJpaTest` to test specific parts of the application.
- **Testcontainers:** Use Testcontainers for reliable integration tests with real databases, message brokers, etc.

## Coroutines & Asynchronous Programming

- **`suspend` functions:** For non-blocking asynchronous code, use `suspend` functions in your controllers and services. Spring Boot has excellent support for coroutines.
- **Structured Concurrency:** Use `coroutineScope` or `supervisorScope` to manage the lifecycle of coroutines.

## Template References

Templates in `templates/kotlin-springboot/`:- `configuration.md`- `data_layer_repositories.md`- `dependency_injection__com.md`- `logging.md`- `project_setup__structure.md`- `service_layer.md`- `testing.md`- `web_layer_controllers.md`

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

- [`kotlin-mcp-server-generator.prompt.md`](kotlin-mcp-server-generator.prompt.md)