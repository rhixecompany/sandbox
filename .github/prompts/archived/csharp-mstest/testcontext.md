# TestContext

> Extracted from `csharp-mstest.prompt.md`.

## TestContext

The `TestContext` class provides test run information, cancellation support, and output methods. See [TestContext documentation](https://learn.microsoft.com/dotnet/core/testing/unit-testing-mstest-writing-tests-testcontext) for complete reference.

### Accessing TestContext

```csharp
// Property (MSTest suppresses CS8618 - don't use nullable or = null!)
public TestContext TestContext { get; set; }

// Constructor injection (MSTest 3.6+) - preferred for immutability
[TestClass]
public sealed class MyTests
{
    private readonly TestContext _testContext;

    public MyTests(TestContext testContext)
    {
        _testContext = testContext;
    }
}

// Static methods receive it as parameter
[ClassInitialize]
public static void ClassInit(TestContext context) { }

// Optional for cleanup methods (MSTest 3.6+)
[ClassCleanup]
public static void ClassCleanup(TestContext context) { }

[AssemblyCleanup]
public static void AssemblyCleanup(TestContext context) { }
```

### Cancellation Token

Always use `TestContext.CancellationToken` for cooperative cancellation with `[Timeout]`:

```csharp
[TestMethod]
[Timeout(5000)]
public async Task LongRunningTest()
{
    await _httpClient.GetAsync(url, TestContext.CancellationToken);
}
```

### Test Run Properties

```csharp
TestContext.TestName              // Current test method name
TestContext.TestDisplayName       // Display name (3.7+)
TestContext.CurrentTestOutcome    // Pass/Fail/InProgress
TestContext.TestData              // Parameterized test data (3.7+, in TestInitialize/Cleanup)
TestContext.TestException         // Exception if test failed (3.7+, in TestCleanup)
TestContext.DeploymentDirectory   // Directory with deployment items
```

### Output and Result Files

```csharp
// Write to test output (useful for debugging)
TestContext.WriteLine("Processing item {0}", itemId);

// Attach files to test results (logs, screenshots)
TestContext.AddResultFile(screenshotPath);

// Store/retrieve data across test methods
TestContext.Properties["SharedKey"] = computedValue;
```
