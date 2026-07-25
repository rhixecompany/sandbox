---
name: asyncio-complete-guide
title: "Python AsyncIO Complete Guide (Tech With Tim)"
description: "Use when learning asyncio comprehensively from Tech With Tim's YouTube tutorial — covers event loop, coroutines, tasks, gather, TaskGroup, futures, synchronization primitives (Lock, Semaphore, Event), with animated explanations."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [asyncio, python, techwithtim, tutorial, complete, taskgroup, lock, semaphore, event, futures]
---
# Python AsyncIO Complete Guide (Tech With Tim)

## Purpose

Comprehensive asyncio tutorial from Tech With Tim YouTube video — covers event loop, coroutines, tasks, gather, TaskGroup, futures, synchronization primitives with animated explanations.

## When to Use

- Full asyncio learning path
- Understanding TaskGroup (Python 3.11+)
- Learning synchronization primitives
- Animated visual learners

## When NOT to Use

- Quick reference (use 9-min video)
- Conceptual only (use BBC Part 1)
- Production-only patterns

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug deadlocks, race conditions, TaskGroup errors |
| `test-driven-development` | Test async code with pytest-asyncio |

## Workflow

### Phase 1: Overview

**Source:** Tech With Tim YouTube — "Asyncio in Python - Full Tutorial"
**Target:** Python 3.11+
**Style:** Animated explanations + live coding

### Phase 2: Key Concepts

#### Event Loop
- Central scheduler
- Manages coroutines/tasks
- Single-threaded cooperative multitasking

#### Coroutines (`async def`)
- Pausable functions
- `await` yields control
- Must be awaited or wrapped in Task

#### Tasks
- Wrapper for coroutines
- Scheduled on event loop
- `asyncio.create_task(coro())` for concurrency

### Phase 3: Concurrent Execution Patterns

**`asyncio.gather()`** — All results at once:
```python
results = await asyncio.gather(
    fetch_data(1),
    fetch_data(2),
    fetch_data(3)
)
```

**`asyncio.TaskGroup` (Python 3.11+)** — Structured concurrency:
```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_data(1))
    task2 = tg.create_task(fetch_data(2))
# Auto-cancels on exception, waits for all
```

> **Best Practice:** Use `TaskGroup` over `gather()` for robust error handling.

### Phase 4: Futures

- Low-level promise of future result
- Rarely used directly in app code
- Common in library internals

```python
future = loop.create_future()
asyncio.create_task(set_future_result(future))
result = await future
```

### Phase 5: Synchronization Primitives

| Primitive | Purpose | Example |
|-----------|---------|---------|
| **Lock** | Mutual exclusion | `async with lock:` |
| **Semaphore** | Limit concurrent access | `async with sem:` (max N) |
| **Event** | Signal between tasks | `event.set()`, `await event.wait()` |
| **Condition** | Complex wait/notify | `async with cond:` |

**Lock Example:**
```python
lock = asyncio.Lock()
async def modify_shared():
    async with lock:
        # Critical section
        await asyncio.sleep(1)
```

**Semaphore Example (throttling):**
```python
sem = asyncio.Semaphore(2)  # Max 2 concurrent
async def limited_fetch():
    async with sem:
        return await fetch()
```

**Event Example:**
```python
event = asyncio.Event()
async def waiter():
    await event.wait()
    print("Event received!")
async def setter():
    await asyncio.sleep(1)
    event.set()
```

### Phase 6: Practical Example — Fetching User Data

```python
import asyncio
import httpx

async def fetch_user(client, user_id):
    response = await client.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        # Concurrent with TaskGroup
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch_user(client, i)) for i in range(1, 11)]
        users = [task.result() for task in tasks]
    return users
```

### Phase 7: Key Takeaways

- Event loop = scheduler
- Coroutines = pausable functions
- Tasks = scheduled coroutines
- `TaskGroup` = preferred structured concurrency
- Futures = low-level promises
- Lock/Semaphore/Event = coordination tools
- Async = concurrent I/O, not parallel CPU

## Pitfalls

- **TaskGroup exception handling** — one failure cancels all (by design)
- **Lock contention** — design for minimal critical sections
- **Semaphore starvation** — ensure release properly
- **Event missed** — if set before wait, waiter never wakes (use Condition for guaranteed notify)

## Verification Checklist

- [ ] Event loop role understood
- [ ] Coroutine vs Task vs Future distinguished
- [ ] gather vs TaskGroup tradeoffs clear
- [ ] All 4 synchronization primitives used correctly
- [ ] httpx AsyncClient pattern applied

## References

- `references/techwithtim-asyncio-patterns.md` — All code patterns
- `references/taskgroup-migration.md` — Migrating from gather to TaskGroup

## Templates

- `templates/async-http-client.py` — Reusable async client with semaphore
- `templates/taskgroup-pattern.py` — Structured concurrency template

## Scripts

- `scripts/asyncio-demo.py` — Full runnable demo
- `scripts/primitive-tester.py` — Test lock/semaphore/event behavior