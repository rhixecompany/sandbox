# Assertions

> Extracted from `csharp-nunit.prompt.md`.

## Assertions

- Use `Assert.That` with constraint model (preferred NUnit style)
- Use constraints like `Is.EqualTo`, `Is.SameAs`, `Contains.Item`
- Use `Assert.AreEqual` for simple value equality (classic style)
- Use `CollectionAssert` for collection comparisons
- Use `StringAssert` for string-specific assertions
- Use `Assert.Throws<T>` or `Assert.ThrowsAsync<T>` to test exceptions
- Use descriptive messages in assertions for clarity on failure
