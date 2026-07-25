# TaskGroup Guide (Python 3.11+)

## Basic Usage

```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_data(1))
    task2 = tg.create_task(fetch_data(2))
# All tasks completed or first exception raised
results = [task1.result(), task2.result()]
```

## Key Differences from gather()

| Feature | gather() | TaskGroup |
|---------|----------|-----------|
| Exception handling | `return_exceptions=True` | Auto-cancels on first exception |
| Structured concurrency | No | Yes |
| Python version | 3.7+ | 3.11+ |

## Migration from gather

```python
# Old (gather)
results = await asyncio.gather(
    fetch_data(1),
    fetch_data(2),
    return_exceptions=True
)

# New (TaskGroup)
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_data(1))
    task2 = tg.create_task(fetch_data(2))
results = [task1.result(), task2.result()]
```

## Best Practices

1. Always use `async with` context manager
2. Handle exceptions at the group level
3. Use `create_task()` for concurrent execution
3. Access results via `.result()` after context exits