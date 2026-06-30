---
toolsets:
  - changes
  - search/codebase
  - edit/editFiles
  - problems
  - search
license: MIT
author: Hermes Agent
version: 1.0.0
title: MSTest Best Practices (MSTest 3.x/4.x)
name: csharp-mstest
description: "Get best practices for MSTest 3.x/4.x unit testing, including modern assertion APIs and data-driven tests"
tags:
  - api
  - csharp
  - data
  - dotnet
  - prompts
  - testing
  - typescript
  - api
  - csharp
  - dotnet
  - testing
metadata:
  hermes:
    related_skills: []
    tags:
    - csharp-mstest.prompt

trigger: csharp-mstest

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - csharp-mstest.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - csharp-mstest.prompt

# MSTest Best Practices (MSTest 3.x/4.x)

Your goal is to help me write effective unit tests with modern MSTest, using current APIs and best practices.

## Project Setup

- Use a separate test project with naming convention `[ProjectName].Tests`
- Reference MSTest 3.x+ NuGet packages (includes analyzers)
- Consider using MSTest.Sdk for simplified project setup
- Run tests with `dotnet test`

## Test Class Structure

- Use `[TestClass]` attribute for test classes
- **Seal test classes by default** for performance and design clarity
- Use `[TestMethod]` for test methods (prefer over `[DataTestMethod]`)
- Follow Arrange-Act-Assert (AAA) pattern
- Name tests using pattern `MethodName_Scenario_ExpectedBehavior`

```csharp
[TestClass]
public sealed class CalculatorTests
{
    [TestMethod]
    public void Add_TwoPositiveNumbers_ReturnsSum()
    {
        // Arrange
        var calculator = new Calculator();

        // Act
        var result = calculator.Add(2, 3);

        // Assert
        Assert.AreEqual(5, result);
    }
}
```

## Test Lifecycle

> - **Prefer constructors over `[TestInitialize]`** - enables `readonly` fields an
> - Use `[TestCleanup]` for cleanup that must run even if test fails

> **Full content:** `templates/csharp-mstest/test_lifecycle.md`

## Modern Assertion APIs

> MSTest provides three assertion classes: `Assert`, `StringAssert`, and `Collecti
> ### Assert Class - Core Assertions

> **Full content:** `templates/csharp-mstest/modern_assertion_apis.md`

## Data-Driven Tests

> [DataRow(0, 0, 0, DisplayName = "Zeros")]
> [DataRow(-1, 1, 0, IgnoreMessage = "Known issue #123")]  // MSTest 3.8+

> **Full content:** `templates/csharp-mstest/data-driven_tests.md`

## TestContext

> The `TestContext` class provides test run information, cancellation support, and
> ### Accessing TestContext

> **Full content:** `templates/csharp-mstest/testcontext.md`

## Advanced Features

> ### Retry for Flaky Tests (MSTest 3.9+)
> public void FlakyTest() { }

> **Full content:** `templates/csharp-mstest/advanced_features.md`

## Common Mistakes to Avoid

> // ❌ Wrong argument order
> Assert.AreEqual(actual, expected);

> **Full content:** `templates/csharp-mstest/common_mistakes_to_avoid.md`

## Test Organization

- Group tests by feature or component
- Use `[TestCategory("Category")]` for filtering
- Use `[TestProperty("Name", "Value")]` for custom metadata (e.g., `[TestProperty("Bug", "12345")]`)
- Use `[Priority(1)]` for critical tests
- Enable relevant MSTest analyzers (MSTEST0020 for constructor preference)

## Mocking and Isolation

- Use Moq or NSubstitute for mocking dependencies
- Use interfaces to facilitate mocking
- Mock dependencies to isolate units under test


## Template References

Detailed templates in `templates/csharp-mstest/`:
- `advanced_features.md`
- `common_mistakes_to_avoid.md`
- `data-driven_tests.md`
- `modern_assertion_apis.md`
- `test_lifecycle.md`
- `testcontext.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
