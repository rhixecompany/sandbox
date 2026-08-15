---
name: csharp-nunit
title: csharp nunit
description: Prompt for csharp-nunit
version: "1.0.0"
tags: []
trigger: csharp-nunit
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

---
name: csharp-nunit
title: NUnit Best Practices
description: Get best practices for NUnit unit testing, including data-driven tests.
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
- prompts
- testing
- typescript
trigger: /csharp-nunit
dependencies: []
metadata:
  hermes: {}
---

## Goal

Get best practices for NUnit unit testing, including data-driven tests.

# NUnit Best PracticesYour goal is to help me write effective unit tests with NUnit, covering both standard and data-driven testing approaches.

## Project Setup

- Use a separate test project with naming convention `[ProjectName].Tests`- Reference Microsoft.NET.Test.Sdk, NUnit, and NUnit3TestAdapter packages- Create test classes that match the classes being tested (e.g., `CalculatorTests` for `Calculator`)- Use .NET SDK test commands: `dotnet test` for running tests

## Test Structure

- Apply `[TestFixture]` attribute to test classes- Use `[Test]` attribute for test methods- Follow the Arrange-Act-Assert (AAA) pattern- Name tests using the pattern `MethodName_Scenario_ExpectedBehavior`- Use `[SetUp]` and `[TearDown]` for per-test setup and teardown- Use `[OneTimeSetUp]` and `[OneTimeTearDown]` for per-class setup and teardown- Use `[SetUpFixture]` for assembly-level setup and teardown

## Standard Tests

- Keep tests focused on a single behavior- Avoid testing multiple behaviors in one test method- Use clear assertions that express intent- Include only the assertions needed to verify the test case- Make tests independent and idempotent (can run in any order)- Avoid test interdependencies

## Data-Driven Tests

- Use `[TestCase]` for inline test data
- Use `[TestCaseSource]` for programmatically generated test data
- Use `[Values]` for simple parameter combinations
- Use `[ValueSource]` for property or method-based data sources
- Use `[Random]` for random numeric test values
- Use `[Range]` for sequential numeric test values
- Use `[Combinatorial]` or `[Pairwise]` for combining multiple parameters

## Assertions

- Use `Assert.That` with constraint model (preferred NUnit style)
- Use constraints like `Is.EqualTo`, `Is.SameAs`, `Contains.Item`
- Use `Assert.AreEqual` for simple value equality (classic style)
- Use `CollectionAssert` for collection comparisons
- Use `StringAssert` for string-specific assertions
- Use `Assert.Throws<T

> ` or `Assert.ThrowsAsync<T>` to test exceptions- Use descriptive messages in assertions for clarity on failure

## Mocking and Isolation

- Consider using Moq or NSubstitute alongside NUnit- Mock dependencies to isolate units under test- Use interfaces to facilitate mocking- Consider using a DI container for complex test setups

## Test Organization

- Group tests by feature or component- Use categories with `[Category("CategoryName")]`- Use `[Order]` to control test execution order when necessary- Use `[Author("DeveloperName")]` to indicate ownership- Use `[Description]` to provide additional test information- Consider `[Explicit]` for tests that shouldn't run automatically- Use `[Ignore("Reason")]` to temporarily skip tests

## Template References

Templates in `templates/csharp-nunit/`:- `assertions.md`- `data-driven_tests.md`- `mocking_and_isolation.md`- `project_setup.md`- `standard_tests.md`- `test_organization.md`- `test_structure.md`

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
- [`csharp-tunit.prompt.md`](csharp-tunit.prompt.md)
- [`csharp-xunit.prompt.md`](csharp-xunit.prompt.md)

