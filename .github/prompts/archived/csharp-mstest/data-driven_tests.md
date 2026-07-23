# Data-Driven Tests

> Extracted from `csharp-mstest.prompt.md`.

## Data-Driven Tests

### DataRow

```csharp
[TestMethod]
[DataRow(1, 2, 3)]
[DataRow(0, 0, 0, DisplayName = "Zeros")]
[DataRow(-1, 1, 0, IgnoreMessage = "Known issue #123")]  // MSTest 3.8+
public void Add_ReturnsSum(int a, int b, int expected)
{
    Assert.AreEqual(expected, Calculator.Add(a, b));
}
```

### DynamicData

The data source can return any of the following types:

- `IEnumerable<(T1, T2, ...)>` (ValueTuple) - **preferred**, provides type safety (MSTest 3.7+)
- `IEnumerable<Tuple<T1, T2, ...>>` - provides type safety
- `IEnumerable<TestDataRow>` - provides type safety plus control over test metadata (display name, categories)
- `IEnumerable<object[]>` - **least preferred**, no type safety

> **Note:** When creating new test data methods, prefer `ValueTuple` or `TestDataRow` over `IEnumerable<object[]>`. The `object[]` approach provides no compile-time type checking and can lead to runtime errors from type mismatches.

```csharp
[TestMethod]
[DynamicData(nameof(TestData))]
public void DynamicTest(int a, int b, int expected)
{
    Assert.AreEqual(expected, Calculator.Add(a, b));
}

// ValueTuple - preferred (MSTest 3.7+)
public static IEnumerable<(int a, int b, int expected)> TestData =>
[
    (1, 2, 3),
    (0, 0, 0),
];

// TestDataRow - when you need custom display names or metadata
public static IEnumerable<TestDataRow<(int a, int b, int expected)>> TestDataWithMetadata =>
[
    new((1, 2, 3)) { DisplayName = "Positive numbers" },
    new((0, 0, 0)) { DisplayName = "Zeros" },
    new((-1, 1, 0)) { DisplayName = "Mixed signs", IgnoreMessage = "Known issue #123" },
];

// IEnumerable<object[]> - avoid for new code (no type safety)
public static IEnumerable<object[]> LegacyTestData =>
[
    [1, 2, 3],
    [0, 0, 0],
];
```
