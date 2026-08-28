---
name: csharp-mstest
title: C# MSTest Framework
description: Author robust unit tests using MSTest with modern assertion APIs, data-driven tests, lifecycle hooks, and TestContext access for .NET projects.
version: 1.0.0
author: Hermes Agent
tags:
- csharp
- dotnet
- testing
- mstest
- unit-test
- automation
- backend
- best-practices
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
## Table of Contents

## Goal

## Context

## Phases



# Table of Contents

- [Goal](#goal)
- [Project Setup](#project-setup)
- [Test Class Structure](#test-class-structure)
- [Test Lifecycle](#test-lifecycle)
- [Modern Assertion APIs](#modern-assertion-apis)
  - [Assert Class](#assert-class)
- [Data-Driven Tests](#data-driven-tests)
- [Test](#test)
  - [Accessing TestContext](#accessing-testcontext)
- [Advanced Features](#advanced-features)
  - [Retry for Flaky Tests (MSTest 3.9+)](#retry-for-flaky-tests-mstest-39+)
- [Common Mistakes to Avoid](#common-mistakes-to-avoid)
- [Test Organization](#test-organization)
- [Mocking and Isolation](#mocking-and-isolation)
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



- [Goal](#goal)
- [Project Setup](#project-setup)
- [Test Class Structure](#test-class-structure)
- [Test Lifecycle](#test-lifecycle)
- [Modern Assertion APIs](#modern-assertion-apis)
- [Assert Class](#assert-class)
- [Data-Driven Tests](#data-driven-tests)
- [Test](#test)
- [Accessing TestContext](#accessing-testcontext)
- [Advanced Features](#advanced-features)
- [Retry for Flaky Tests (MSTest 3.9+)](#retry-for-flaky-tests-mstest-39+)
- [Common Mistakes to Avoid](#common-mistakes-to-avoid)
- [Test Organization](#test-organization)
- [Mocking and Isolation](#mocking-and-isolation)
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





Get best practices for MSTest 3.x/4.x unit testing, including modern assertion APIs and data-driven tests.

## MSTest Best Practices (MSTest 3.x/4.x)Your goal is to help me write effective unit tests with modern MSTest, using current APIs and best practices.

## Project Setup

- Use a separate test project with naming convention `[ProjectName].Tests`- Reference MSTest 3.x+ NuGet packages (includes analyzers)- Consider using MSTest.Sdk for simplified project setup- Run tests with `dotnet test`

## Test Class Structure

- Use `[TestClass]` attribute for test classes- **Seal test classes by default** for performance and design clarity- Use `[TestMethod]` for test methods (prefer over `[DataTestMethod]`)- Follow Arrange-Act-Assert (AAA) pattern- Name tests using pattern `MethodName_Scenario_ExpectedBehavior````csharp[TestClass]public sealed class CalculatorTests{ [TestMethod] public void Add_TwoPositiveNumbers_ReturnsSum() { // Arrange var calculator = new Calculator(); // Act var result = calculator.Add(2, 3); // Assert Assert.AreEqual(5, result); }}```

## Test Lifecycle

> - **Prefer constructors over `[TestInitialize]`** - enables `readonly` fields an
> - Use `[TestCleanup]` for cleanup that must run even if test fails
> **Full content:**

## Modern Assertion APIs

> MSTest provides three assertion classes: `Assert`, `StringAssert`, and `Collecti>>

### Assert Class

- Core Assertions

> **Full content:**

## Data-Driven Tests

> [DataRow(0, 0, 0, DisplayName = "Zeros")]
> [DataRow(-1, 1, 0, IgnoreMessage = "Known issue #123")] // MSTest 3.8+
> **Full content:**

## Test

Context> The `TestContext` class provides test run information, cancellation support, and>>

### Accessing TestContext

> **Full content:**

## Advanced Features

### Retry for Flaky Tests (MSTest 3.9+)

> public void FlakyTest() { }

## Common Mistakes to Avoid

> // ❌ Wrong argument order
> Assert.AreEqual(actual, expected);
> **Full content:**

## Test Organization

- Group tests by feature or component- Use `[TestCategory("Category")]` for filtering- Use `[TestProperty("Name", "Value")]` for custom metadata (e.g., `[TestProperty("Bug", "12345")]`)- Use `[Priority(1)]` for critical tests- Enable relevant MSTest analyzers (MSTEST0020 for constructor preference)

## Mocking and Isolation

- Use Moq or NSubstitute for mocking dependencies- Use interfaces to helps mocking- Mock dependencies to isolate units under test

## Template References

Detailed templates in `templates/csharp-mstest/`:- `advanced_features.md`- `common_mistakes_to_avoid.md`- `data-driven_tests.md`- `modern_assertion_apis.md`- `test_lifecycle.md`- `testcontext.md`

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

- [`csharp-async.prompt.md`](csharp-async.prompt.md)
- [`csharp-docs.prompt.md`](csharp-docs.prompt.md)
- [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md)
- [`csharp-nunit.prompt.md`](csharp-nunit.prompt.md)
- [`csharp-tunit.prompt.md`](csharp-tunit.prompt.md)
- [`csharp-xunit.prompt.md`](csharp-xunit.prompt.md)