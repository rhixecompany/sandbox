# Return Types

> Extracted from `csharp-async.prompt.md`.

## Return Types

- Return `Task<T>` when the method returns a value
- Return `Task` when the method doesn't return a value
- Consider `ValueTask<T>` for high-performance scenarios to reduce allocations
- Avoid returning `void` for async methods except for event handlers
