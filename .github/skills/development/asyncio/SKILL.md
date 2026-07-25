---
name: asyncio
title: "Python AsyncIO — Complete Learning & Reference Guide"
description: "Master asyncio for I/O-bound concurrency in Python. Covers event loop, coroutines, tasks, TaskGroup, gather, as_completed, wait/for, synchronization primitives (Lock, Semaphore, Event, Condition), structured concurrency, debugging, testing, and production patterns — all unified from NeuralNine, Tech With Tim, Real Python, GeeksforGeeks, BBC, and Patrick's Software Blog tutorials."
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - asyncio
  - python
  - concurrency
  - async
  - await
  - event-loop
  - taskgroup
  - synchronization
metadata:
  hermes:
    tags:
      - asyncio
      - python
      - concurrency
      - async
      - await
      - event-loop
      - taskgroup
      - synchronization
    related_skills:
      - systematic-debugging
      - test-driven-development
---

# Python AsyncIO — Complete Learning & Reference Guide

**Unified skill** consolidating: `asyncio-9min-youtube`, `asyncio-complete-guide`, `asyncio-full-tutorial`, `asyncio-geeksforgeeks`, `asyncio-hands-on-walkthrough`, `asyncio-part1-basics`, `asyncio-patricks-blog`.

Use this single skill for **all asyncio learning, reference, and production patterns**. Subsections below are labeled by source tutorial for traceability.

---

## When to Use

- Learning asyncio from scratch → start with **Conceptual Foundation (BBC/NeuralNine)**
- Comprehensive tutorial with animated explanations → **Tech With Tim (Complete Guide)**
- Hands-on practice with all patterns → **Real Python (Hands-On Walkthrough)**
- Quick 9-minute refresher → **NeuralNine (9-min YouTube)**
- Practical API patterns with httpx/semaphore → **Patrick's Software Blog**
- GeeksforGeeks syntax reference → **GeeksforGeeks**
- Production patterns: TaskGroup, semaphores, timeouts, error handling

---

## Conceptual Foundation (BBC Part 1 / NeuralNine)

### Concurrency vs Parallelism in Python

| Approach | Best For | GIL Impact |
|----------|----------|------------|
| **Multiprocessing** | CPU-bound tasks | Bypasses GIL (separate processes) |
| **Multi-threading** | Limited GIL control | Threads share GIL |
| **AsyncIO** | **I/O-bound with idle time** | Single thread, cooperative multitasking |

> **Key Insight**: AsyncIO is NOT about multithreading or bypassing GIL. It's about **efficiently using a single CPU core** during I/O waits by switching between coroutines.

### Core Architecture

```
Event Loop (scheduler)
    ↓ manages
Tasks (wrapped coroutines)
    ↓ wraps
Coroutines (async def functions that can yield via await)
```

- **Event Loop**: Central scheduler in each thread; manages list of Tasks
- **Task**: Wraps a coroutine; maintains own stack and execution state
- **Coroutine**: Function defined with `async def`; can `await` to yield control
- **Control Transfer**: Only happens at explicit `await` points — event loop **cannot preempt**

### CPU-bound vs I/O-bound

| Type | Characteristics | Example |
|------|----------------|---------|
| **CPU-bound** | Continuously uses CPU | Image processing, calculations |
| **I/O-bound** | Frequently waits for external responses | HTTP requests, DB queries, file reads |

**AsyncIO's purpose**: Allow other tasks to run while one task waits for I/O — maximizing single-core efficiency.

---

## Syntax & Core Mechanics (NeuralNine / GeeksforGeeks / Real Python)

### Defining & Running Coroutines

```python
import asyncio

async def io_task(name: str, delay: float, iterations: int):
    for i in range(iterations):
        print(f"{name} - Iteration {i}")
        await asyncio.sleep(delay)  # Yields control

# Entry point — ALWAYS use asyncio.run()
asyncio.run(io_task("demo", 1.0, 3))
```

### Sequential vs Concurrent

```python
# SEQUENTIAL (slow) — ~12 seconds
async def sequential():
    await io_task("A", 1, 5)
    await io_task("B", 2, 3)
    await io_task("C", 0.5, 8)

# CONCURRENT with gather (fast) — ~4.5 seconds
async def concurrent_gather():
    await asyncio.gather(
        io_task("A", 1, 5),
        io_task("B", 2, 3),
        io_task("C", 0.5, 8)
    )
```

### Critical Rules

| Rule | Correct | Wrong |
|------|---------|-------|
| Sleep | `await asyncio.sleep(1)` | `time.sleep(1)` — blocks thread |
| Await | Only inside `async def` | Top-level without `asyncio.run()` |
| Run | `asyncio.run(main())` | `asyncio.run(main)` (missing parens) |

---

## Concurrency Patterns (All Sources)

### 1. `asyncio.gather()` — All Results Together

```python
results = await asyncio.gather(
    fetch_data(1),
    fetch_data(2),
    fetch_data(3),
    return_exceptions=True  # Don't cancel all on one failure
)
```

**Best for**: When you need all results before proceeding.

---

### 2. `asyncio.TaskGroup` (Python 3.11+) — Structured Concurrency **PREFERRED**

```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_data(1))
    task2 = tg.create_task(fetch_data(2))
    task3 = tg.create_task(fetch_data(3))
# Auto-waits for all; cancels siblings on exception
users = [task.result() for task in [task1, task2, task3]]
```

> **Best Practice (Tech With Tim)**: Use `TaskGroup` over `gather()` for robust error handling and automatic lifecycle management.

---

### 3. `asyncio.create_task()` — Fire & Forget (Background Tasks)

```python
task = asyncio.create_task(background_work())
print("Continuing immediately...")
await task  # Wait here when you need the result
```

**Best for**: Starting work early, awaiting later.

---

### 4. `asyncio.as_completed()` — Process Results As They Arrive

```python
coroutines = [fetch_user(i) for i in range(1, 11)]
for completed in asyncio.as_completed(coroutines):
    result = await completed
    print(result)  # Process immediately
```

**Best for**: Streaming/real-time output, progress UIs.

---

### 5. `asyncio.wait()` — Fine-Grained Control

```python
done, pending = await asyncio.wait(
    [task1, task2, task3],
    return_when=asyncio.FIRST_COMPLETED
)
# Process done tasks
await asyncio.gather(*pending)  # Wait for rest
```

**Return conditions**: `FIRST_COMPLETED`, `FIRST_EXCEPTION`, `ALL_COMPLETED` (default).

---

### 6. `asyncio.wait_for()` — Timeouts

```python
try:
    result = await asyncio.wait_for(slow_operation(), timeout=2.0)
except asyncio.TimeoutError:
    print("Operation timed out!")
```

---

## Synchronization Primitives (Tech With Tim / Real Python / Patrick's Blog)

| Primitive | Purpose | Use Case |
|-----------|---------|----------|
| **Lock** | Mutual exclusion | Protect shared state |
| **Semaphore** | Limit concurrent access | API rate limiting, throttling |
| **Event** | Signal between tasks | One-time notification |
| **Condition** | Complex wait/notify | Producer-consumer patterns |

### Lock — Mutual Exclusion

```python
lock = asyncio.Lock()

async def modify_shared():
    async with lock:
        # Critical section — only one task at a time
        await asyncio.sleep(1)
```

### Semaphore — Concurrency Limiting (Patrick's Blog / Real Python)

```python
semaphore = asyncio.Semaphore(5)  # Max 5 concurrent

async def limited_fetch(url):
    async with semaphore:
        return await fetch(url)

# API rate limiting example
async def main():
    semaphore = asyncio.Semaphore(5)
    async with httpx.AsyncClient() as client:
        tasks = [limited_fetch(client, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)
```

---

### Event — One-Time Signal

```python
event = asyncio.Event()

async def waiter():
    await event.wait()
    print("Event received!")

async def setter():
    await asyncio.sleep(1)
    event.set()  # All waiters wake up
```

---

### Condition — Guaranteed Notify (Real Python)

```python
condition = asyncio.Condition()

async def consumer():
    async with condition:
        await condition.wait()
        print("Notified!")

async def producer():
    async with condition:
        condition.notify()
```

> **Why Condition over Event?** If `event.set()` happens before `event.wait()`, the waiter misses it. `Condition` guarantees notification within the critical section.

---

## Practical HTTP Patterns (Patrick's Blog / Tech With Tim)

### Recommended: Reuse Single `httpx.AsyncClient`

```python
import httpx
import asyncio

async def fetch_user(client: httpx.AsyncClient, user_id: int):
    response = await client.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        # Concurrent with TaskGroup (3.11+)
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch_user(client, i)) for i in range(1, 11)]
        users = [task.result() for task in tasks]
    return users
```

### Performance Comparison (Patrick's Blog)

| Approach | Time (10 users) |
|----------|-----------------|
| **Async (as_completed + Semaphore 5)** | **0.24s** |
| Synchronous | 1.80s |
| **Speedup** | **~7.5x** |

---

## Error Handling Patterns

### gather with return_exceptions

```python
results = await asyncio.gather(
    risky_operation(1),
    risky_operation(2),
    return_exceptions=True  # Returns Exception objects instead of raising
)
for r in results:
    if isinstance(r, Exception):
        logger.error(f"Failed: {r}")
    else:
        process(r)
```

### TaskGroup — Automatic Cancellation

```python
async with asyncio.TaskGroup() as tg:
    tg.create_task(critical_task())
    tg.create_task(other_task())
# If critical_task fails, other_task is CANCELLED automatically
```

### Timeout Wrapper

```python
async def with_timeout(coro, timeout_seconds):
    try:
        return await asyncio.wait_for(coro, timeout=timeout_seconds)
    except asyncio.TimeoutError:
        return None  # or raise custom exception
```

---

## Platform-Specific Notes (Patrick's Blog / BBC)

```python
import platform

def get_event_loop_policy():
    system = platform.system().lower()
    if system == "windows":
        # Python 3.8+: ProactorEventLoop by default (subprocess support)
        return "Windows - ProactorEventLoop"
    elif system == "linux":
        return "Linux - epoll (SelectorEventLoop)"
    elif system == "darwin":
        return "macOS - kqueue (KqueueSelector)"
```

**Windows Note**: Use `asyncio.create_subprocess_exec` carefully; subprocess handling differs from Unix.

---

## Debugging & Testing (Systematic Debugging / TDD)

### Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| `time.sleep()` in async | Blocks entire event loop | Use `asyncio.sleep()` |
| Missing `await` | Coroutine never executes | Always `await` or wrap in `create_task()` |
| `gather()` without `return_exceptions` | One failure cancels all | Add `return_exceptions=True` |
| Blocking I/O (requests, sqlite3) | Defeats concurrency | Use `aiohttp`, `aiosqlite`, `httpx` |

### Debugging Tools

```python
# Enable asyncio debug mode
import asyncio
asyncio.get_event_loop().set_debug(True)

# Or via env var
# PYTHONASYNCIODEBUG=1 python script.py
```

### Testing with pytest-asyncio

```python
# pytest.ini
[pytest]
asyncio_mode = auto

# test_example.py
import pytest

@pytest.mark.asyncio
async def test_concurrent_fetch():
    results = await asyncio.gather(fetch(1), fetch(2))
    assert len(results) == 2
```

---

## Quick Reference Card

| Task | Code |
|------|------|
| Run async main | `asyncio.run(main())` |
| Concurrent all | `await asyncio.gather(coro1, coro2)` |
| Structured concurrency | `async with asyncio.TaskGroup() as tg:` |
| Background task | `task = asyncio.create_task(coro())` |
| Process as ready | `for done in asyncio.as_completed(coros):` |
| Wait for condition | `done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)` |
| Timeout | `await asyncio.wait_for(coro(), timeout=5)` |
| Mutual exclusion | `async with asyncio.Lock():` |
| Rate limit (N concurrent) | `async with asyncio.Semaphore(N):` |
| One-time signal | `await event.wait()` / `event.set()` |
| Guaranteed notify | `async with condition:` / `condition.notify()` |

---

## Source Attribution Map

| Section | Primary Source(s) |
|---------|-------------------|
| Conceptual Foundation | BBC Part 1, NeuralNine 9-min |
| Syntax & Core Mechanics | NeuralNine, GeeksforGeeks, Real Python |
| gather / TaskGroup | Tech With Tim, Real Python |
| create_task / as_completed / wait / wait_for | NeuralNine, Real Python, Patrick's Blog |
| Synchronization Primitives | Tech With Tim, Real Python, Patrick's Blog |
| HTTP Patterns + Semaphore | Patrick's Blog, Tech With Tim |
| Platform Notes | BBC, Patrick's Blog |
| Debugging/Testing | Systematic Debugging, TDD |

---

## Verification Checklist

- [ ] Can explain why asyncio ≠ threading/multiprocessing
- [ ] Distinguishes CPU-bound vs I/O-bound correctly
- [ ] Runs basic coroutine with `asyncio.run()`
- [ ] Uses `gather()` for all-results, `as_completed()` for streaming
- [ ] Prefers `TaskGroup` (3.11+) over `gather()` for production
- [ ] Applies `Semaphore` for rate limiting
- [ ] Uses `Lock` for shared state protection
- [ ] Understands `Event` vs `Condition` tradeoff
- [ ] Reuses single `httpx.AsyncClient` across requests
- [ ] Handles timeouts with `wait_for()`
- [ ] Uses `return_exceptions=True` for fault tolerance
- [ ] Tests async code with `pytest-asyncio`

---

## References

- `references/asyncio-conceptual-faq.md` — Common misconceptions (BBC/NeuralNine)
- `references/neuralnine-asyncio-patterns.md` — 9-min video code snippets
- `references/techwithtim-asyncio-patterns.md` — Full tutorial patterns
- `references/realpython-asyncio-patterns.md` — All patterns with variations
- `references/httpx-async-patterns.md` — Advanced httpx usage
- `references/semaphore-patterns.md` — Dynamic rate limiting
- `references/taskgroup-migration.md` — Migrating from gather to TaskGroup
- `references/async-vs-threading.md` — Detailed comparison
- `references/asyncio-syntax-quickref.md` — Syntax reference
- `references/asyncio-repl-guide.md` — REPL tips and tricks
- `references/blocking-vs-async-libs.md` — Library mapping table
- `references/asyncio-debugging.md` — Debugging asyncio code
- `references/part2-awaitables-tasks-futures.md` — BBC Part 2 link

## Templates

- `templates/async-pattern-cookbook.py` — All patterns in one file
- `templates/async-http-client.py` — Reusable async client with semaphore
- `templates/semaphore-pattern.py` — Concurrency limiting template
- `templates/taskgroup-pattern.py` — Structured concurrency template
- `templates/sync-to-async-migration.md` — Migration checklist
- `templates/asyncio-basic-pattern.md` — Template for async functions

## Scripts

- `scripts/countsync.py` — Synchronous baseline
- `scripts/countasync.py` — Asynchronous version
- `scripts/pattern-demo.py` — All patterns runnable
- `scripts/benchmark-async-vs-sync.py` — Performance comparison
- `scripts/primitive-tester.py` — Test lock/semaphore/event behavior
- `scripts/rate-limit-tester.py` — Semaphore behavior verification
- `scripts/asyncio-9min-demo.py` — NeuralNine demo
- `scripts/asyncio-demo.py` — Tech With Tim full demo
- `scripts/asyncio-pitfalls.py` — Common pitfalls demo