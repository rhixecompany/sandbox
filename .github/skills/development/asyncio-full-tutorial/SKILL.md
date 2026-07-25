---
name: asyncio-full-tutorial
title: "AsyncIO in Python Full Tutorial (Tech With Tim)"
description: "Use when learning asyncio comprehensively from Tech With Tim's YouTube tutorial — covers event loop, coroutines, tasks, gather, TaskGroup, futures, synchronization primitives, and practical API fetching example."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [asyncio, python, tutorial, youtube, tech-with-tim, concurrency, async, await]
---
# AsyncIO in Python Full Tutorial (Tech With Tim)

## Purpose

Complete asyncio learning path from Tech With Tim's YouTube tutorial — covers all core concepts with practical examples for Python 3.11+.

## When to Use

- Learning asyncio from scratch
- Understanding event loop, tasks, TaskGroup
- Building concurrent I/O applications
- Python 3.11+ async patterns

## When NOT to Use

- CPU-bound parallelism (use multiprocessing)
- Legacy Python <3.7
- Quick reference only (use 9-min summary)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug async deadlocks, cancellation, exception handling |
| `test-driven-development` | Test async code with pytest-asyncio |

## Workflow

### Phase 1: Key Concepts

**Concurrency in Python — 3 Approaches:**
| Approach | Best For | GIL Impact |
|----------|----------|------------|
| Multiprocessing | CPU-bound tasks | Bypasses GIL |
| Multi-threading | Limited GIL control | Limited by GIL |
| **AsyncIO** | **I/O-bound with idle time** | Single thread, cooperative |

**AsyncIO Mechanics:** Event loop switches between coroutines during `await` — single thread, cooperative multitasking.

### Phase 2: Core Mechanics

**1. Coroutines (`async def`)**
```python
async def io_task(name, delay, iterations):
    for i in range(iterations):
        print(f"{name} - Iteration {i}")
        await asyncio.sleep(delay)  # Yields control
```

**2. Running Async Code**
```python
asyncio.run(main())  # Creates and manages event loop
# IMPORTANT: Call main() with parentheses inside asyncio.run()
```

**3. Concurrent Execution with `asyncio.gather()`**
```python
await asyncio.gather(
    io_task("A", 1, 5),
    io_task("B", 2, 3),
    io_task("C", 0.5, 8)
)
# Result: All tasks run interleaved (~4.5s total), not sequential (~11s)
```

**4. Sequential vs Concurrent**
- Sequential (slow): `await a(); await b(); await c()`
- Concurrent (fast): Use `gather()` or `create_task()`

### Phase 3: Advanced Patterns

**Background Tasks with `create_task()`**
```python
task = asyncio.create_task(background_task())
print("Continuing immediately...")
await task  # Wait here until done
print("Final statement")
```

**Waiting with Conditions: `asyncio.wait()`**
```python
done, pending = await asyncio.wait(
    [task1, task2],
    return_when=asyncio.FIRST_COMPLETED
)
# Process done tasks
await asyncio.gather(*pending)  # Wait for remaining
```

**Timeouts with `asyncio.wait_for()`**
```python
try:
    result = await asyncio.wait_for(long_operation(), timeout=2)
except asyncio.TimeoutError:
    print("Took too long!")
```

### Phase 4: Critical Rules

- **Use `await`** to return control to event loop during I/O waits
- **Never use `time.sleep()`** in async code — use `asyncio.sleep()`
- `asyncio.gather()` = run multiple tasks concurrently
- `asyncio.create_task()` = fire-and-forget (but await later)
- `asyncio.wait()` = wait for specific conditions (e.g., first done)
- `asyncio.wait_for()` = add timeouts to async operations
- Async is **not parallel** — it's **concurrent on a single thread**, ideal for I/O-bound work

## Common Issues

### 1. Blocking Calls in Async Code
```python
# BAD - blocks event loop
import time
time.sleep(1)

# GOOD - yields control
await asyncio.sleep(1)
```

### 2. Missing await
```python
# BAD - coroutine never runs
asyncio.create_task(do_work())

# GOOD
await asyncio.create_task(do_work())
```

### 3. Exception Handling in gather
```python
# BAD - one failure cancels all
await asyncio.gather(task1(), task2())

# GOOD - handle gracefully
results = await asyncio.gather(task1(), task2(), return_exceptions=True)
for r in results:
    if isinstance(r, Exception):
        logger.error(r)
```

- **Blocking calls in async** → Use async libraries (aiohttp, aiosqlite)
- **Forgetting `await`** → Coroutine never executes
- **Exception in gather** → Cancels others unless `return_exceptions=True`
- **TaskGroup (3.11+)** preferred over gather for error handling

## Verification Checklist

- [ ] Event loop runs without blocking
- [ ] Concurrent tasks complete in ~max time not sum
- [ ] Semaphore limits concurrency correctly
- [ ] Timeouts trigger on slow operations
- [ ] Async client reused (single AsyncClient instance)

## References

- `references/asyncio-api-patterns.md` — aiohttp, httpx, asyncpg patterns
- `references/asyncio-debugging.md` — Debugging async code
- `references/taskgroup-guide.md` — Python 3.11+ TaskGroup

## Templates

- `templates/async-api-client.py` — Reusable async HTTP client
- `templates/semaphore-pattern.py` — Concurrency limiting template

## Scripts

- `scripts/benchmark-async-vs-sync.py` — Performance comparison