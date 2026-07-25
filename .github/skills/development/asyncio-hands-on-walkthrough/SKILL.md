---
name: asyncio-hands-on-walkthrough
title: "Python's AsyncIO: A Hands-On Walkthrough (Real Python)"
description: "Use when learning asyncio through Real Python's comprehensive hands-on guide — covers chess analogy, async/await keywords, event loop, REPL, sync vs async comparison, common patterns (chaining, gather, as_completed, wait, timeout), and detailed explanations."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [asyncio, python, realpython, hands-on, walkthrough, chess-analogy, event-loop, repl, patterns]
---
# Python's AsyncIO: A Hands-On Walkthrough (Real Python)

## Purpose

Complete hands-on asyncio guide from Real Python — chess analogy, async/await keywords, event loop, REPL, sync vs async comparison, and all common patterns with detailed explanations.

## When to Use

- Learning asyncio by doing (not just reading)
- Understanding async/await mechanics deeply
- Mastering asyncio REPL for exploration
- All pattern variations with tradeoffs

## When NOT to Use

- Quick reference (use 9-min video)
- Conceptual only (use BBC Part 1)
- Production-only patterns

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug async syntax, deadlocks, cancellation |
| `test-driven-development` | Test async code with pytest-asyncio |

## Workflow

### Phase 1: Concurrency vs Parallelism — The Chess Analogy

> **Synchronous:** Judit Polgár plays one game at a time. 24 games × 30 min = **12 hours**
>
> **Asynchronous:** Judit moves table to table, one move each. 24 games × 2 min/round × 30 rounds = **1 hour**
>
> **Threading/Multiprocessing:** Multiple Judits playing simultaneously

**Key insight:** Async I/O gives *feeling* of concurrency using single thread — cooperative multitasking.

### Phase 2: Core Building Blocks

| Construct | Purpose |
|-----------|---------|
| `async def` | Defines a **coroutine function** |
| `await` | **Suspends** calling coroutine until awaited result returns; yields control to event loop |
| `async for` | Iterates over **asynchronous iterator** |
| `async with` | **Asynchronous context manager** |

### Phase 3: Rules

- `await` **only** inside `async def` (SyntaxError otherwise)
- `await f()` requires `f()` to be **awaitable** (coroutine or `.__await__()`)
- `async def` may use `await`, `return`, or `yield` (all optional)
- `yield from` inside `async def` → **SyntaxError** (use `await` instead)

### Phase 4: Minimal Example

```python
async def g():
    result = await f()  # Pause g() until f() returns; let event loop run other tasks
    return result
```

### Phase 5: First Example — Sync vs Async

**Synchronous (`countsync.py`):**
```python
import time
def count():
    print("One")
    time.sleep(1)
    print("Two")
    time.sleep(1)

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    main()
# Output: ~6.03 seconds
```

**Asynchronous (`countasync.py`):**
```python
import asyncio
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    asyncio.run(main())
# Output: ~2.00 seconds
```

> **Key insight:** `time.sleep()` **blocks** thread; `asyncio.sleep()` **yields** control.

### Phase 6: The Event Loop

- Infinite loop monitoring coroutines
- Takes feedback on what's idle, schedules tasks
- `asyncio.run()` = recommended way to start (gets loop, runs tasks, closes loop)
- `asyncio.get_running_loop()` = returns running loop (RuntimeError if none)
- **Pluggable:** Unix `SelectorEventLoop`, Windows `ProactorEventLoop`, third-party `uvloop` (faster)

### Phase 7: Important Detail

Calling coroutine directly returns coroutine object — does NOT execute:
```python
>>> routine = main()
>>> routine
<coroutine object main at 0x...>
>>> asyncio.run(routine)
Hello...
World!
```

### Phase 8: Asyncio REPL (Python 3.8+)

```bash
python -m asyncio
```
```python
>>> await main()
Hello...
World!
```
Allows `await` at top level without `asyncio.run()`.

### Phase 9: Common Async I/O Patterns

#### 1. Coroutine Chaining
```python
async def get_user_with_posts(user_id):
    user = await fetch_user(user_id)
    await fetch_posts(user)
    return user
```

#### 2. `asyncio.gather()` — All Results Together
```python
results = await asyncio.gather(
    func1(), func2(), func3(),
    return_exceptions=True  # Don't cancel all on one failure
)
```

#### 3. `asyncio.as_completed()` — Process As Ready
```python
coroutines = [simulated_api_call(i) for i in range(1, 6)]
for completed_coroutine in asyncio.as_completed(coroutines):
    result = await completed_coroutine
    print(result)
```

#### 4. `asyncio.wait()` — Fine-Grained Control
```python
done, pending = await asyncio.wait(
    [task1, task2],
    return_when=asyncio.FIRST_COMPLETED
)
# Process done
await asyncio.gather(*pending)  # Wait for remaining
```

#### 5. `asyncio.wait_for()` — Timeouts
```python
try:
    result = await asyncio.wait_for(long_operation(), timeout=2)
except asyncio.TimeoutError:
    print("Took too long!")
```

### Phase 10: Critical Reminders

- `await` **required** to yield control. `time.sleep()` instead of `asyncio.sleep()` **blocks thread** and defeats async.
- Always use `asyncio.sleep()` in async code.

## Pitfalls

- **Blocking calls in async** — `requests.get()`, `time.sleep()`, `sqlite3` → use `aiohttp`, `asyncio.sleep()`, `aiosqlite`
- **Gather without `return_exceptions=True`** — one error cancels all
- **Missing `await`** — coroutine never runs
- **Event loop already running** — nested `asyncio.run()` fails (use `get_running_loop()`)
- **REPL vs script** — REPL allows top-level await; scripts need `asyncio.run()`

## Verification Checklist

- [ ] Chess analogy explains concurrency vs parallelism
- [ ] All 4 keywords (`async def`, `await`, `async for`, `async with`) used
- [ ] Sync vs async timing difference demonstrated
- [ ] All 5 patterns (chaining, gather, as_completed, wait, wait_for) implemented
- [ ] Event loop pluggability understood
- [ ] REPL usage verified

## References

- `references/realpython-asyncio-patterns.md` — All patterns with variations
- `references/asyncio-repl-guide.md` — REPL tips and tricks
- `references/blocking-vs-async-libs.md` — Library mapping table

## Templates

- `templates/async-pattern-cookbook.py` — All patterns in one file
- `templates/sync-to-async-migration.md` — Migration checklist

## Scripts

- `scripts/countsync.py` — Synchronous baseline
- `scripts/countasync.py` — Asynchronous version
- `scripts/pattern-demo.py` — All patterns runnable