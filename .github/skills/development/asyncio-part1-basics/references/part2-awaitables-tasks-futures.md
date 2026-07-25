# BBC Part 2: Awaitables, Tasks, Futures

## Awaitables

Objects that can be used in `await` expression:
1. **Coroutines** - defined with `async def`
2. **Tasks** - wrapper around coroutine, scheduled on event loop
3. **Futures** - low-level awaitable, represents future result

```python
# Coroutine
async def my_coro():
    return 42

# Task - schedules coroutine
task = asyncio.create_task(my_coro())

# Future - low-level
future = asyncio.Future()
future.set_result(42)
result = await future
```

## Creating and Managing Tasks

```python
# Create task (schedules immediately)
task = asyncio.create_task(coro())

# Wait for task
result = await task

# Check status
task.done()      # True if completed
task.cancelled() # True if cancelled
task.exception() # Exception if failed

# Cancel task
task.cancel()
try:
    await task
except asyncio.CancelledError:
    print("Task was cancelled")
```

## Task Groups (Python 3.11+)

```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(coro1())
    task2 = tg.create_task(coro2())
# All tasks completed or first exception raised
```

## Futures

Low-level, rarely used directly:
```python
# Create future
future = asyncio.Future()

# Set result (from another callback/thread)
future.set_result(value)

# Set exception
future.set_exception(Exception("error"))

# Await future
result = await future
```

## asyncio.run() vs Event Loop

```python
# High-level (recommended)
asyncio.run(main())

# Low-level
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```

## Awaiting Multiple Tasks

```python
# Wait for all - gather
results = await asyncio.gather(task1, task2, task3)

# Wait for first - wait
done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)

# Wait with timeout
done, pending = await asyncio.wait(tasks, timeout=5.0)
```