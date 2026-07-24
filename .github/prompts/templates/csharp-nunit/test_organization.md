# Test Organization

> Extracted from `csharp-nunit.prompt.md`.

## Test Organization

- Group tests by feature or component
- Use categories with `[Category("CategoryName")]`
- Use `[Order]` to control test execution order when necessary
- Use `[Author("DeveloperName")]` to indicate ownership
- Use `[Description]` to provide additional test information
- Consider `[Explicit]` for tests that shouldn't run automatically
- Use `[Ignore("Reason")]` to temporarily skip tests
