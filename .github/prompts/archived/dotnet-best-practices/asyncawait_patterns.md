# Async/Await Patterns

> Extracted from `dotnet-best-practices.prompt.md`.

## Async/Await Patterns

- Use async/await for all I/O operations and long-running tasks
- Return Task or Task<T> from async methods
- Use ConfigureAwait(false) where appropriate
- Handle async exceptions properly
