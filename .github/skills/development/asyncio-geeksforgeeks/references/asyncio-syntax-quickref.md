# AsyncIO Syntax Quick Reference

## Keywords

```python
async def          # Define coroutine function
await              # Suspend until awaitable completes
async for          # Iterate over async iterator
async with         # Async context manager
```

## Creating Coroutines

```python
async def my_coro():
    return "result"

coro = my_coro()  # Returns coroutine object
await coro        # Execute and get result
```

## Running Coroutines

```python
# Main entry point
asyncio.run(main())

# With existing loop
loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
```

## Concurrent Execution

```python
# Gather - wait for all
results = await asyncio.gather(coro1(), coro2(), coro3())

# Create task (fire-and-forget)
task = asyncio.create_task(coro())

# Wait for task
result = await task

# Wait with conditions
done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)
```

## Timeouts and Cancellation

```python
# Timeout
try:
    await asyncio.wait_for(coro(), timeout=5.0)
except asyncio.TimeoutError:
    pass

# Cancel task
task.cancel()
try:
    await task
except asyncio.CancelledError:
    pass
```

## Sleep

```python
# CORRECT - async sleep
await asyncio.sleep(1.0)

# WRONG - blocks event loop
time.sleep(1)
```

## Event Loop

```python
# Get running loop
loop = asyncio.get_running_loop()

# Schedule callback
loop.call_soon(callback, arg)
loop.call_later(delay, callback, arg)
loop.call_at(when, callback, arg)
```

## Synchronization Primitives

```python
# Lock
lock = asyncio.Lock()
async with lock:
    # critical section

# Semaphore
sem = asyncio.Semaphore(3)
async with sem:
    # max 3 concurrent

# Event
event = asyncio.Event()
await event.wait()
event.set()
```