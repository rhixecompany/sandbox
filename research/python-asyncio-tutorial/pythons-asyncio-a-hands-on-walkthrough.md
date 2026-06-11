# Python's asyncio: A Hands-On Walkthrough

> **Source:** https://realpython.com/async-io-python
> **Retrieved:** 2026-05-31T12:17:10

---

# Python's `asyncio`: A Hands-On Walkthrough — Comprehensive Summary

## Overview

Python's `asyncio` library enables concurrent code using `async` and `await` keywords. It is a **single-threaded, single-process** technique using **cooperative multitasking** to efficiently manage multiple I/O-bound tasks within a single thread. It is **not** threading or multiprocessing — it is a standalone concurrency model.

---

## Key Concepts

### Concurrency vs. Parallelism
- **Async I/O is concurrency, not parallelism.** It gives a *feeling* of concurrency using a single thread.
- **Threading** and **multiprocessing** are alternative concurrency models in Python (`threading`, `multiprocessing`, `concurrent.futures`).
- Async I/O is more closely aligned with threading than multiprocessing but is distinct from both.

### The Chess Analogy (Miguel Grinberg)
> **Synchronous**: Judit Polgár plays one game at a time. 24 games × 30 min = **12 hours**.
>
> **Asynchronous**: Judit moves from table to table, making one move at each. 24 games × 2 min per round × 30 rounds = **1 hour**.
>
> There's only one Judit. Playing asynchronously cuts time from 12 hours to 1 hour.

### Core Building Blocks
- **Awaitable objects** — most often coroutines
- **Event loop** — schedules and executes coroutines asynchronously
- **Coroutines** — functions defined with `async def` that can suspend and resume execution

---

## `async` and `await` Keywords

### Definitions
| Construct | Purpose |
|---|---|
| `async def` | Defines a coroutine function |
| `await` | Suspends execution of the calling coroutine until the awaited result is returned; yields control to the event loop |
| `async for` | Iterates over an asynchronous iterator |
| `async with` | Asynchronous version of `with` for async context managers |

### Rules
- `await` can **only** be used inside `async def` functions (raises `SyntaxError` otherwise).
- `await f()` requires `f()` to be an **awaitable** (a coroutine or an object with `.__await__()`).
- `async def` may use `await`, `return`, or `yield` (all optional).
- `yield from` inside `async def` raises `SyntaxError`.

### Minimal Example
```python
async def g():
    result = await f()  # Pause g() until f() returns; let something else run
    return result
```

---

## First Example: Synchronous vs. Asynchronous

### Synchronous Version (`countsync.py`)
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
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```
**Output:** ~6.03 seconds

### Asynchronous Version (`countasync.py`)
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
    import time
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```
**Output:** ~2.00 seconds

> **Key insight:** `time.sleep()` is a **blocking** call; `asyncio.sleep()` is **non-blocking** and yields control to the event loop.

---

## The Event Loop

- The event loop is an infinite loop that monitors coroutines, takes feedback on what's idle, and schedules tasks.
- **`asyncio.run()`** is the recommended way to start the event loop in modern Python. It gets the loop, runs tasks, and closes the loop.
- **`asyncio.get_running_loop()`** returns the running loop instance (raises `RuntimeError` if none is running).
- The event loop is **pluggable** — you can swap implementations:
  - Unix default: `SelectorEventLoop`
  - Windows default: `ProactorEventLoop`
  - Third-party: [uvloop](https://github.com/MagicStack/uvloop) (faster alternative)

### Important Detail
Calling a coroutine directly returns a coroutine object — it does **not** execute it:
```python
>>> routine = main()
>>> routine
<coroutine object main at 0x1027a6150>
>>> asyncio.run(routine)
Hello...
World!
```

---

## The `asyncio` REPL (Python 3.8+)

```bash
$ python -m asyncio
```
Allows using `await` directly at the top level without `asyncio.run()`:
```python
>>> await main()
Hello...
World!
```

---

## Common Async I/O Patterns

### 1. Coroutine Chaining

Coroutines can be **chained** — one coroutine awaits another and passes its result to the next.

```python
async def get_user_with_posts(user_id):
    user = await fetch_user(user_id)
    await fetch_posts(user)

async def fetch_user(user_id):
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)
    return {"id": user_id, "name": f"User{user_id}"}

async def fetch_posts(user):
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)
    posts = [f"Post {i} by {user['name']}" for i in range(1, 3)]
    return

[... summary truncated for context management ...]

---

*Extracted by web-research-pipeline v1.0.0*
