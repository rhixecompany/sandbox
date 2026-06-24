# Test Lifecycle

> Extracted from `csharp-mstest.prompt.md`.

## Test Lifecycle

- **Prefer constructors over `[TestInitialize]`** - enables `readonly` fields and follows standard C# patterns
- Use `[TestCleanup]` for cleanup that must run even if test fails
- Combine constructor with async `[TestInitialize]` when async setup is needed

```csharp
[TestClass]
public sealed class ServiceTests
{
    private readonly MyService _service;  // readonly enabled by constructor

    public ServiceTests()
    {
        _service = new MyService();
    }

    [TestInitialize]
    public async Task InitAsync()
    {
        // Use for async initialization only
        await _service.WarmupAsync();
    }

    [TestCleanup]
    public void Cleanup() => _service.Reset();
}
```

### Execution Order

1. **Assembly Initialization** - `[AssemblyInitialize]` (once per test assembly)
2. **Class Initialization** - `[ClassInitialize]` (once per test class)
3. **Test Initialization** (for every test method):
   1. Constructor
   2. Set `TestContext` property
   3. `[TestInitialize]`
4. **Test Execution** - test method runs
5. **Test Cleanup** (for every test method):
   1. `[TestCleanup]`
   2. `DisposeAsync` (if implemented)
   3. `Dispose` (if implemented)
6. **Class Cleanup** - `[ClassCleanup]` (once per test class)
7. **Assembly Cleanup** - `[AssemblyCleanup]` (once per test assembly)
