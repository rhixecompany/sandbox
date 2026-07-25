# AsyncIO TaskGroup Migration Guide

## From gather() to TaskGroup

### Old (gather)
```python
results = await asyncio.gather(
    fetch_data(1),
    fetch_data(2),
    return_exceptions=True
)

for i, result in enumerate(results):
    if isinstance(result, Exception):
        print(f"Task {i} failed: {result}")
    else:
        print(f"Task {i} succeeded: {result}")
```

### New (TaskGroup - Python 3.11+)
```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_data(1))
    task2 = tg.create_task(fetch_data(2))

# If we reach here, all succeeded
results = [task1.result(), task2.result()]
```

## Key Differences

| Feature | gather() | TaskGroup |
|---------|----------|-----------|
| Exception handling | `return_exceptions=True` | Auto-cancels on first exception |
| Structured concurrency | No | Yes |
| Python version | 3.7+ | 3.11+ |

## Migration Pattern

```python
# BEFORE
async def old_main():
    tasks = [fetch_user(i) for i in range(10)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [r for r in results if not isinstance(r, Exception)]

# AFTER
async def new_main():
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch_user(i)) for i in range(10)]
    return [task.result() for task in tasks]
```

## Error Handling

```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(risky_operation())
    task2 = tg.create_task(safe_operation())

# If risky_operation fails:
# 1. safe_operation is cancelled
# 2. Exception propagates
# 3. No manual cleanup needed
```

## Exception Groups (Python 3.11+)

```python
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(fail_1())
        tg.create_task(fail_2())
except* ValueError as eg:
    for exc in eg.exceptions:
        print(f"ValueError: {exc}")
except* TypeError as eg:
    for exc in eg.exceptions:
        print(f"TypeError: {exc}")
```