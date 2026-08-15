---
name: csharp-tunit
title: csharp tunit
description: Prompt for csharp-tunit
version: "1.0.0"
tags: [backend, csharp, qa, testing, tunit]
trigger: csharp-tunit
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
name: csharp-tunit
title: TUnit Best Practices
description: Get best practices for TUnit unit testing, including data-driven tests.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- web
scripts: []
skills: []
formatter: default
plan: null
tags:
- csharp
- data
- dotnet
- prompts
- testing
- typescript
- csharp
- data
- dotnet
- frontend
- prompts
- testing
- typescript
trigger: /csharp-tunit
dependencies: []
metadata:
  hermes: {}
name: csharp-tunit
title: TUnit Best Practices
description: Get best practices for TUnit unit testing, including data-driven tests.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- web
scripts: []
skills: []
formatter: default
plan: null
tags:
- csharp
- data
- dotnet
- prompts
- testing
- typescript
- csharp
- data
- dotnet
- frontend
- prompts
- testing
- typescript
trigger: /csharp-tunit
dependencies: []
metadata:
  hermes: {}
---

## Goal

Get best practices for TUnit unit testing, including data-driven tests.

# TUnit Best PracticesYour goal is to help me write effective unit tests with TUnit, covering both standard and data-driven testing approaches.

## Project Setup

- Use a separate test project with naming convention `[ProjectName].Tests`- Reference TUnit package and TUnit.Assertions for fluent assertions- Create test classes that match the classes being tested (e.g., `CalculatorTests` for `Calculator`)- Use .NET SDK test commands: `dotnet test` for running tests- TUnit requires .NET 8.0 or higher

## Test Structure

- No test class attributes required (like xUnit/NUnit)- Use `[Test]` attribute for test methods (not `[Fact]` like xUnit)- Follow the Arrange-Act-Assert (AAA) pattern- Name tests using the pattern `MethodName_Scenario_ExpectedBehavior`- Use lifecycle hooks: `[Before(Test)]` for setup and `[After(Test)]` for teardown- Use `[Before(Class)]` and `[After(Class)]` for shared context between tests in a class- Use `[Before(Assembly)]` and `[After(Assembly)]` for shared context across test classes- TUnit supports advanced lifecycle hooks like `[Before(TestSession)]` and `[After(TestSession)]`

## Standard Tests

- Keep tests focused on a single behavior- Avoid testing multiple behaviors in one test method- Use TUnit's fluent assertion syntax with `await Assert.That()`- Include only the assertions needed to verify the test case- Make tests independent and idempotent (can run in any order)- Avoid test interdependencies (use `[DependsOn]` attribute if needed)

## Data-Driven Tests

- Use `[Arguments]` attribute for inline test data (equivalent to xUnit's `[InlineData]`)
- Use `[MethodData]` for method-based test data (equivalent to xUnit's `[MemberData]`)
- Use `[ClassData]` for class-based test data
- Create custom data sources by implementing `ITestDataSource`
- Use meaningful parameter names in data-driven tests
- Multiple `[Arguments]` attributes can be applied to the same test method

## Assertions

- Use `await Assert.That(value).IsEqualTo(expected)` for value equality
- Use `await Assert.That(value).IsSameReferenceAs(expected)` for reference equality
- Use `await Assert.That(value).IsTrue()` or `await Assert.That(value).IsFalse()` for boolean conditions
- Use `await Assert.That(collection).Contains(item)` or `await Assert.That(collection).DoesNotContain(item)` for collections
- Use `await Assert.That(value).Matches(pattern)` for regex pattern matching
- Use `await Assert.That(action).Throws<TException

> ()` or `await Assert.That(asyncAction).ThrowsAsync<TException>()` to test exceptions- Chain assertions with `.And` operator: `await Assert.That(value).IsNotNull().And.IsEqualTo(expected)`- Use`.Or` operator for alternative conditions: `await Assert.That(value).IsEqualTo(1).Or.IsEqualTo(2)`- Use`.Within(tolerance)` for DateTime and numeric comparisons with tolerance- All assertions are asynchronous and must be awaited

## Advanced Features

- Use `[Repeat(n)]` to repeat tests multiple times
- Use `[Retry(n)]` for automatic retry on failure
- Use `[ParallelLimit<T

> ]` to control parallel execution limits- Use `[Skip("reason")]` to skip tests conditionally- Use `[DependsOn(nameof(OtherTest))]` to create test dependencies- Use `[Timeout(milliseconds)]` to set test timeouts- Create custom attributes by extending TUnit's base attributes

## Test Organization

- Group tests by feature or component- Use `[Category("CategoryName")]` for test categorization- Use `[DisplayName("Custom Test Name")]` for custom test names- Consider using `TestContext` for test diagnostics and information- Use conditional attributes like custom `[WindowsOnly]` for platform-specific tests

## Performance and Parallel Execution

- TUnit runs tests in parallel by default (unlike xUnit which requires explicit configuration)- Use `[NotInParallel]` to disable parallel execution for specific tests- Use `[ParallelLimit<T

> ]` with custom limit classes to control concurrency- Tests within the same class run sequentially by default- Use `[Repeat(n)]` with `[ParallelLimit<T>]` for load testing scenarios

## Migration from x

Unit- Replace `[Fact]` with `[Test]`- Replace `[Theory]` with `[Test]` and use `[Arguments]` for data- Replace `[InlineData]` with `[Arguments]`- Replace `[MemberData]` with `[MethodData]`- Replace `Assert.Equal` with `await Assert.That(actual).IsEqualTo(expected)`- Replace `Assert.True` with `await Assert.That(condition).IsTrue()`- Replace `Assert.Throws<T

> ` with `await Assert.That(action).Throws<T>()`- Replace constructor/IDisposable with`[Before(Test)]`/`[After(Test)]`- Replace`IClassFixture<T>` with `[Before(Class)]`/`[After(Class)]`**Why TUnit over xUnit?**TUnit offers a modern, fast, and flexible testing experience with advanced features not present in xUnit, such as asynchronous assertions, more refined lifecycle hooks, and improved data-driven testing capabilities. TUnit's fluent assertions provide clearer and more expressive test validation, making it especially suitable for complex .NET projects.

## Template References

Templates in `templates/csharp-tunit/`:- `migration_from_xunit.md`

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

- [`csharp-async.prompt.md`](csharp-async.prompt.md)
- [`csharp-docs.prompt.md`](csharp-docs.prompt.md)
- [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md)
- [`csharp-mstest.prompt.md`](csharp-mstest.prompt.md)
- [`csharp-nunit.prompt.md`](csharp-nunit.prompt.md)
- [`csharp-xunit.prompt.md`](csharp-xunit.prompt.md)

