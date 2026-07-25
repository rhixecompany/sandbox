---
name: asyncio-geeksforgeeks
title: "AsyncIO in Python (GeeksforGeeks)"
description: "Use when learning asyncio fundamentals from GeeksforGeeks — covers async functions, event loop, sequential vs concurrent execution, create_task, gather, and async vs threading comparison."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [asyncio, python, geeksforgeeks, tutorial, concurrency, async, await, event-loop]
---
# AsyncIO in Python (GeeksforGeeks)

## Purpose

GeeksforGeeks tutorial on Python's asyncio library for concurrent programming using asynchronous iterators.

## When to Use

- Learning asyncio basics
- Understanding event loop and coroutines
- Comparing async vs threading
- Quick reference for syntax

## When NOT to Use

- Advanced patterns (TaskGroup, as_completed, semaphores)
- Production async architecture
- Debugging complex async issues

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug async syntax errors, event loop issues |
| `test-driven-development` | Test async functions |

## Workflow

### Phase 1: Overview

**asyncio** = Python library for concurrent programming using asynchronous iterators. Not multi-threading or multi-processing. Foundation for high-performance network/web servers, database connections, distributed task queues.

### Phase 2: Key Concepts

**Asynchronous Functions:**
- Defined with `async` keyword
- Use `await asyncio.sleep()` instead of `time.sleep()` for non-blocking delays
- Must be executed with `asyncio.run()`

**Example:**
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

### Phase 3: Async Event Loop

**Sequential Execution with `await`:**
```python
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
# Execution Order: one → two → three → four → five
```

**Concurrent Execution with `create_task()`:**
```python
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
# Key Insight: create_task() allows fn2 to execute during fn's await pauses
```

### Phase 4: Handling Multiple I/O-bound Tasks

**`asyncio.gather()` — Run Multiple Coroutines Concurrently:**
```python
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
- Completion order depends on sleep duration: func3 (1s) → func1 (2s) → func2 (3s)
- Ideal for simulating I/O-bound operations

### Phase 5: Key Differences — Async vs Multi-threading

| Feature | Asyncio | Multi-threading |
|---------|---------|-----------------|
| Concurrency Model | Single-threaded, cooperative | Preemptive, OS-managed |
| Best For | I/O-bound tasks | CPU-bound tasks |
| Overhead | Low (no thread creation) | Higher (thread management) |
| Control | Explicit (`await`) | Implicit (OS scheduler) |

### Phase 6: Actionable Takeaways

- Use asyncio for **I/O-bound** operations (network calls, file I/O, database queries)
- Always use `asyncio.sleep()` instead of `time.sleep()` in async code
- Use `asyncio.create_task()` for fire-and-forget concurrency
- Use `asyncio.gather()` to run multiple coroutines and wait for all results
- Remember: asyncio is **single-threaded** — it's about efficient task switching, not parallel execution

## Pitfalls

- `await` only works inside `async def` (SyntaxError otherwise)
- `time.sleep()` blocks thread → defeats async purpose
- Exception in gather cancels all unless `return_exceptions=True`
- No true parallelism for CPU work — use multiprocessing

## Verification Checklist

- [ ] Basic async function runs with asyncio.run()
- [ ] Sequential await executes in order
- [ ] create_task enables concurrent execution
- [ ] gather runs multiple coroutines concurrently
- [ ] async vs threading differences understood

## References

- `references/asyncio-syntax-quickref.md` — Syntax reference
- `references/async-vs-threading.md` — Detailed comparison