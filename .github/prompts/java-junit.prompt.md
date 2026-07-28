---
name: java-junit
title: JUnit 5+ Best Practices
description: 'Get best practices for JUnit 5 unit testing, including data-driven tests.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - web
scripts: []
skills: []
formatter: default
plan: None
tags:
  - api
  - data
  - frontend
  - java
  - prompts
  - testing
  - typescript
trigger: /java-junit
dependencies: []
metadata:
  hermes: {}
---
## Goal

Get best practices for JUnit 5 unit testing, including data-driven tests.

# JUnit 5+ Best PracticesYour goal is to help me write effective unit tests with JUnit 5, covering both standard and data-driven testing approaches.

## Project Setup- Use a standard Maven or Gradle project structure.- Place test source code in `src/test/java`.- Include dependencies for `junit-jupiter-api`, `junit-jupiter-engine`, and `junit-jupiter-params` for parameterized tests.- Use build tool commands to run tests: `mvn test` or `gradle test`.

## Test Structure- Test classes should have a `Test` suffix, e.g., `CalculatorTest` for a `Calculator` class.- Use `@Test` for test methods.- Follow the Arrange-Act-Assert (AAA) pattern.- Name tests using a descriptive convention, like `methodName_should_expectedBehavior_when_scenario`.- Use `@BeforeEach` and `@AfterEach` for per-test setup and teardown.- Use `@BeforeAll` and `@AfterAll` for per-class setup and teardown (must be static methods).- Use `@DisplayName` to provide a human-readable name for test classes and methods.

## Standard Tests- Keep tests focused on a single behavior.- Avoid testing multiple conditions in one test method.- Make tests independent and idempotent (can run in any order).- Avoid test interdependencies.

## Data-Driven (Parameterized) Tests- Use `@ParameterizedTest` to mark a method as a parameterized test.- Use `@ValueSource` for simple literal values (strings, ints, etc.).- Use `@MethodSource` to refer to a factory method that provides test arguments as a `Stream`, `Collection`, etc.- Use `@CsvSource` for inline comma-separated values.- Use `@CsvFileSource` to use a CSV file from the classpath.- Use `@EnumSource` to use enum constants.

## Assertions- Use the static methods from `org.junit.jupiter.api.Assertions` (e.g., `assertEquals`, `assertTrue`, `assertNotNull`).- For more fluent and readable assertions, consider using a library like AssertJ (`assertThat(...).is...`).- Use `assertThrows` or `assertDoesNotThrow` to test for exceptions.- Group related assertions with `assertAll` to ensure all assertions are checked before the test fails.- Use descriptive messages in assertions to provide clarity on failure.

## Mocking and Isolation- Use a mocking framework like Mockito to create mock objects for dependencies.- Use `@Mock` and `@InjectMocks` annotations from Mockito to simplify mock creation and injection.- Use interfaces to facilitate mocking.

## Test Organization- Group tests by feature or component using packages.- Use `@Tag` to categorize tests (e.g., `@Tag("fast")`, `@Tag("integration")`).- Use `@TestMethodOrder(MethodOrderer.OrderAnnotation.class)` and `@Order` to control test execution order when strictly necessary.- Use `@Disabled` to temporarily skip a test method or class, providing a reason.- Use `@Nested` to group tests in a nested inner class for better organization and structure.

## Template ReferencesTemplates in `templates/java-junit/`:- `assertions.md`- `data-driven_parameterized.md`- `mocking_and_isolation.md`- `project_setup.md`- `standard_tests.md`- `test_organization.md`- `test_structure.md`

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
|---|------|-----------|
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
|-------|---------|
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


