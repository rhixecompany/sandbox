# Python Tutorial: AsyncIO - Complete Guide to Asynchronous Programming

> **Source:** <https://www.youtube.com/watch?v=oAkLSJNr5zY>
> **Retrieved:** 2026-05-31T12:17:10
> **Backend:** web-research-pipeline v1.0.0

---

## Overview

This tutorial provides a comprehensive guide to Python's `asyncio` library for asynchronous programming, featuring animated explanations of core concepts.

---

## Key Concepts

### What is AsyncIO?

Python's `asyncio` is a library for writing **concurrent code** using the `async`/`await` syntax. It enables single-threaded cooperative multitasking for I/O-bound operations.

### Concurrency vs Parallelism

| Aspect     | Concurrency (AsyncIO)        | Parallelism (Threading/Multiprocessing) |
| ---------- | ---------------------------- | --------------------------------------- |
| Threads    | Single thread                | Multiple threads/processes              |
| CPU Usage  | Efficient for I/O waits      | True parallel execution                 |
| GIL Impact | Avoids GIL contention        | Limited by GIL (threading)              |
| Use Case   | Network, file I/O, databases | CPU-intensive computation               |

---

## Core Building Blocks

### 1. Coroutines (`async def`)

```python
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```

- Defined with `async def`
- Can be paused with `await`
- Returns a coroutine object when called (not executed immediately)

### 2. Event Loop

```python
import asyncio

async def main():
    task1 = asyncio.create_task(fetch_data("url1"))
    task2 = asyncio.create_task(fetch_data("url2"))
    results = await asyncio.gather(task1, task2)

asyncio.run(main())
```

- Central scheduler managing coroutine execution
- `asyncio.run()` creates/closes loop automatically (Python 3.7+)

### 3. Tasks

```python
task = asyncio.create_task(coro())  # Schedule for concurrent execution
result = await task  # Wait for completion
```

- Wraps coroutine for concurrent execution
- Maintains own stack and execution state

---

## Essential Patterns

### Concurrent Execution with `gather()`

```python
results = await asyncio.gather(
    fetch_user(1),
    fetch_user(2),
    fetch_user(3),
    return_exceptions=True  # Don't cancel all on one failure
)
```

### As-Completed Processing

```python
tasks = [fetch_user(i) for i in range(10)]
for coro in asyncio.as_completed(tasks):
    result = await coro
    process(result)  # Handle each as it finishes
```

### Concurrency Control with Semaphore

```python
semaphore = asyncio.Semaphore(5)  # Max 5 concurrent

async def limited_fetch(url):
    async with semaphore:
        return await fetch_data(url)
```

### Timeouts

```python
try:
    result = await asyncio.wait_for(fetch_data(url), timeout=5.0)
except asyncio.TimeoutError:
    handle_timeout()
```

---

## Common Pitfalls

| Pitfall                            | Solution                                 |
| ---------------------------------- | ---------------------------------------- |
| `time.sleep()` in async code       | Use `await asyncio.sleep()`              |
| Forgetting `await` on coroutine    | Always await async functions             |
| Blocking I/O (requests, sqlite3)   | Use async libraries (aiohttp, aiosqlite) |
| Creating too many concurrent tasks | Use `Semaphore` to limit concurrency     |
| Not handling `CancelledError`      | Catch and re-raise or cleanup properly   |

---

## Animation Visualizations (from Video)

The tutorial includes animated explanations of:

1. **Event loop tick cycle** — how tasks yield and resume
2. **Coroutine state machine** — suspended/resumed/completed states
3. **Task scheduling** — `create_task` vs `gather` vs `as_completed`
4. **Semaphore gating** — visual token bucket for concurrency control

---

## Further Resources

- [Official asyncio docs](https://docs.python.org/3/library/asyncio.html)
- [Real Python asyncio walkthrough](https://realpython.com/async-io-python/)
- [Effective asyncio patterns](https://github.com/python/asyncio/blob/main/docs/source/examples.rst)

---

_Extracted by web-research-pipeline v1.0.0_
