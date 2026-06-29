# Migration from xUnit

> Extracted from `csharp-tunit.prompt.md`.

## Migration from xUnit

- Replace `[Fact]` with `[Test]`
- Replace `[Theory]` with `[Test]` and use `[Arguments]` for data
- Replace `[InlineData]` with `[Arguments]`
- Replace `[MemberData]` with `[MethodData]`
- Replace `Assert.Equal` with `await Assert.That(actual).IsEqualTo(expected)`
- Replace `Assert.True` with `await Assert.That(condition).IsTrue()`
- Replace `Assert.Throws<T>` with `await Assert.That(action).Throws<T>()`
- Replace constructor/IDisposable with `[Before(Test)]`/`[After(Test)]`
- Replace `IClassFixture<T>` with `[Before(Class)]`/`[After(Class)]`

**Why TUnit over xUnit?**

TUnit offers a modern, fast, and flexible testing experience with advanced features not present in xUnit, such as asynchronous assertions, more refined lifecycle hooks, and improved data-driven testing capabilities. TUnit's fluent assertions provide clearer and more expressive test validation, making it especially suitable for complex .NET projects.
