# Test Structure

> Extracted from `csharp-nunit.prompt.md`.

## Test Structure

- Apply `[TestFixture]` attribute to test classes
- Use `[Test]` attribute for test methods
- Follow the Arrange-Act-Assert (AAA) pattern
- Name tests using the pattern `MethodName_Scenario_ExpectedBehavior`
- Use `[SetUp]` and `[TearDown]` for per-test setup and teardown
- Use `[OneTimeSetUp]` and `[OneTimeTearDown]` for per-class setup and teardown
- Use `[SetUpFixture]` for assembly-level setup and teardown
