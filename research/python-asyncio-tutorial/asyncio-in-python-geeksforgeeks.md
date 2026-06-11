# asyncio in Python - GeeksforGeeks

> **Source:** https://www.geeksforgeeks.org/python/asyncio-in-python
> **Retrieved:** 2026-05-31T12:17:10

---

# Summary: asyncio in Python - GeeksforGeeks

## Overview

**asyncio** is a Python library for **concurrent programming** using asynchronous iterators. It is **not** multi-threading or multi-processing. It serves as the foundation for many Python asynchronous frameworks used in high-performance network/web servers, database connections, and distributed task queues.

---

## Key Concepts

### Asynchronous Functions
- Defined using the `async` keyword
- Use `await asyncio.sleep()` instead of `time.sleep()` for non-blocking delays
- Must be executed using `asyncio.run()`

### Example: Basic Async Function
```python
import asyncio

async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

asyncio.run(fn())
```

---

## Async Event Loop

### Sequential Execution with `await`
When one async function `await`s another, it waits for completion before continuing:

```python
import asyncio

async def fn():
    print("one")
    await asyncio.sleep(1)
    await fn2()  # Waits for fn2 to complete
    print('four')
    await asyncio.sleep(1)
    print('five')

async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")

asyncio.run(fn())
```

**Execution Order:** `one` → `two` → `three` → `four` → `five`

### Concurrent Execution with `asyncio.create_task()`
To achieve true concurrency, use `asyncio.create_task()` to schedule tasks that run during idle time:

```python
import asyncio

async def fn():
    task = asyncio.create_task(fn2())  # Schedule fn2 concurrently
    print("one")
    print('four')
    await asyncio.sleep(1)
    print('five')

async def fn2():
    print("two")
    await asyncio.sleep(1)
    print("three")

asyncio.run(fn())
```

**Key Insight:** `create_task()` allows `fn2` to execute whenever there's free time (e.g., during `await` pauses), enabling parallel-like behavior.

---

## Handling Multiple I/O-bound Tasks

Use `asyncio.gather()` to run multiple coroutines concurrently:

```python
import asyncio

async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")

async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")

async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")

async def main():
    await asyncio.gather(func1(), func2(), func3())
    print("Main Ended..")

asyncio.run(main())
```

**Behavior:**
- All functions start concurrently
- Completion order depends on sleep duration: `func3` (1s) → `func1` (2s) → `func2` (3s)
- Ideal for simulating I/O-bound operations

---

## Key Differences: Async vs Multi-threading

| Feature | Asyncio | Multi-threading |
|---------|---------|-----------------|
| Concurrency Model | Single-threaded, cooperative | Preemptive, OS-managed |
| Best For | I/O-bound tasks | CPU-bound tasks |
| Overhead | Low (no thread creation) | Higher (thread management) |
| Control | Explicit (`await`) | Implicit (OS scheduler) |

---

## Actionable Takeaways

- Use `asyncio` for **I/O-bound** operations (network calls, file I/O, database queries)
- Always use `asyncio.sleep()` instead of `time.sleep()` in async code
- Use `asyncio.create_task()` for fire-and-forget concurrency
- Use `asyncio.gather()` to run multiple coroutines and wait for all results
- Remember: asyncio is **single-threaded** — it's about efficient task switching, not parallel execution

---

*Extracted by web-research-pipeline v1.0.0*
