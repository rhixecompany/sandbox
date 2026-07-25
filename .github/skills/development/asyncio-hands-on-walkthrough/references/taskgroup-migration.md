# TaskGroup Migration Guide (Python 3.11+)

## Why Migrate?

| gather() | TaskGroup |
|----------|-----------|
| `return_exceptions=True` needed for error handling | Automatic error handling, cancels all on first failure |
| No structured concurrency | Structured concurrency guaranteed |
| Python 3.7+ | Python 3.11+ |
| Manual cleanup needed | Automatic cleanup on exit |

## Migration Patterns

### Simple gather → TaskGroup

```python
# OLD
results = await asyncio.gather(
    fetch_data(1),
    fetch_data(2),
    fetch_data(3),
    return_exceptions=True
)

# NEW
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_data(1))
    task2 = tg.create_task(fetch_data(2))
    task3 = tg.create_task(fetch_data(3))

results = [task1.result(), task2.result(), task3.result()]
```

### gather with return_exceptions=True → TaskGroup

```python
# OLD - continues on error
results = await asyncio.gather(
    risky_task(1),
    risky_task(2),
    return_exceptions=True
)

# NEW - stops on first error
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(risky_task(1))
    task2 = tg.create_task(risky_task(2))

results = [task1.result(), task2.result()]
# If any fails, ALL cancelled, exception raised
```

### To preserve "continue on error" behavior:

```python
async with asyncio.TaskGroup() as tg:
    tasks = [tg.create_task(safe_task(i)) for i in range(10)]

results = []
for task in tasks:
    try:
        results.append(task.result())
    except Exception as e:
        results.append(e)  # Capture error, continue
```

## Key Differences

| Aspect | gather() | TaskGroup |
|--------|----------|-----------|
| Error on first failure | No (with return_exceptions) | Yes (cancels all) |
| Structured concurrency | No | Yes |
| Exception chaining | Manual | Automatic |
| Cleanup | Manual | Automatic |
| Python version | 3.7+ | 3.11+ |

## Migration Checklist

- [ ] Replace `asyncio.gather()` with `async with asyncio.TaskGroup()`
- [ ] Change `await asyncio.gather(...)` to `tg.create_task()` calls
- [ ] Access results via `.result()` after context exits
- [ ] Update exception handling for fail-fast behavior
- [ ] Test cancellation behavior (TaskGroup cancels all on first error)
- [ ] Update tests for new error semantics

## Compatibility Wrapper

```python
# For gradual migration
async def safe_gather(*coros, return_exceptions=False):
    if hasattr(asyncio, 'TaskGroup'):
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(c) for c in coros]
        if return_exceptions:
            return [t.result() if not t.exception() else t.exception() for t in tasks]
        return [t.result() for t in tasks]
    else:
        return await asyncio.gather(*coros, return_exceptions=return_exceptions)
```