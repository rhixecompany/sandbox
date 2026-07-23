# Advanced Features

> Extracted from `csharp-mstest.prompt.md`.

## Advanced Features

### Retry for Flaky Tests (MSTest 3.9+)

```csharp
[TestMethod]
[Retry(3)]
public void FlakyTest() { }
```

### Conditional Execution (MSTest 3.10+)

Skip or run tests based on OS or CI environment:

```csharp
// OS-specific tests
[TestMethod]
[OSCondition(OperatingSystems.Windows)]
public void WindowsOnlyTest() { }

[TestMethod]
[OSCondition(OperatingSystems.Linux | OperatingSystems.MacOS)]
public void UnixOnlyTest() { }

[TestMethod]
[OSCondition(ConditionMode.Exclude, OperatingSystems.Windows)]
public void SkipOnWindowsTest() { }

// CI environment tests
[TestMethod]
[CICondition]  // Runs only in CI (default: ConditionMode.Include)
public void CIOnlyTest() { }

[TestMethod]
[CICondition(ConditionMode.Exclude)]  // Skips in CI, runs locally
public void LocalOnlyTest() { }
```

### Parallelization

```csharp
// Assembly level
[assembly: Parallelize(Workers = 4, Scope = ExecutionScope.MethodLevel)]

// Disable for specific class
[TestClass]
[DoNotParallelize]
public sealed class SequentialTests { }
```

### Work Item Traceability (MSTest 3.8+)

Link tests to work items for traceability in test reports:

```csharp
// Azure DevOps work items
[TestMethod]
[WorkItem(12345)]  // Links to work item #12345
public void Feature_Scenario_ExpectedBehavior() { }

// Multiple work items
[TestMethod]
[WorkItem(12345)]
[WorkItem(67890)]
public void Feature_CoversMultipleRequirements() { }

// GitHub issues (MSTest 3.8+)
[TestMethod]
[GitHubWorkItem("https://github.com/owner/repo/issues/42")]
public void BugFix_Issue42_IsResolved() { }
```

Work item associations appear in test results and can be used for:

- Tracing test coverage to requirements
- Linking bug fixes to regression tests
- Generating traceability reports in CI/CD pipelines
