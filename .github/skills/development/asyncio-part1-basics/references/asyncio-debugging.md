# AsyncIO Debugging Guide

## Common Issues

### 1. Blocking Calls in Async Code
```python
# BAD - blocks event loop
import time
time.sleep(1)

# GOOD - yields control
await asyncio.sleep(1)
```

### 2. Forgetting await
```python
# BAD - coroutine never runs
asyncio.create_task(do_work())

# GOOD
await asyncio.create_task(do_work())
# or
task = asyncio.create_task(do_work())
await task
```

### 3. Exception Handling in gather
```python
# BAD - one failure cancels all
await asyncio.gather(task1(), task2())

# GOOD - handle exceptions gracefully
results = await asyncio.gather(task1(), task2(), return_exceptions=True)
for r in results:
    if isinstance(r, Exception):
        logger.error(r)
```

## Debugging Tools

### AsyncIO Debug Mode
```python
asyncio.run(main(), debug=True)
```

### Logging Coroutine Creation
```python
import asyncio
asyncio.get_event_loop().set_debug(True)
```

### Task Inspection
```python
all_tasks = asyncio.all_tasks()
for task in all_tasks:
    print(task.get_name(), task.get_coro())
```