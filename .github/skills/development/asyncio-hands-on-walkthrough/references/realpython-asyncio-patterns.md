# AsyncIO Part 2: Awaitables, Tasks, Futures

## Overview

Part 2 of the BBC asyncio series covers practical syntax: `async`/`await`, creating/managing Tasks, working with Futures, and the awaitable protocol.

## Core Concepts

### `async` and `await` Keywords

| Construct | Purpose |
|-----------|---------|
| `async def` | Defines a coroutine function |
| `await` | Suspends calling coroutine until awaited result returns; yields control to event loop |
| `async for` | Iterates over asynchronous iterator |
| `async with` | Asynchronous context manager |

### Rules

- `await` **only** inside `async def` (SyntaxError otherwise)
- `await f()` requires `f()` to be **awaitable** (coroutine or `__await__`)
- `async def` may use `await`, `return`, or `yield` (all optional)
- `yield from` inside `async def` → **SyntaxError** (use `await` instead)

## First Examples

### Synchronous (`countsync.py`)
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

### Asynchronous (`countasync.py`)
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

## The Event Loop

- Infinite loop monitoring coroutines
- Takes feedback on what's idle, schedules tasks
- `asyncio.run()` = get loop, run tasks, close loop
- `asyncio.get_running_loop()` = returns running loop (RuntimeError if none)
- **Pluggable**: Unix `SelectorEventLoop`, Windows `ProactorEventLoop`, third-party `uvloop`

## Important Detail

Calling coroutine directly returns coroutine object — does **not** execute it:

```python
>>> routine = main()
>>> routine
<coroutine object main at 0x1027a6150>
>>> asyncio.run(routine)
Hello...
World!
```

## Asyncio REPL (Python 3.8+)

```bash
python -m asyncio
```

```python
>>> await main()
Hello...
World!
```

Allows `await` at top level without `asyncio.run()`.

## Common Async I/O Patterns

### 1. Coroutine Chaining
```python
async def get_user_with_posts(user_id):
    user = await fetch_user(user_id)
    await fetch_posts(user)
    return user
```

### 2. `asyncio.gather()` — All Results Together
```python
results = await asyncio.gather(
    func1(), func2(), func3(),
    return_exceptions=True  # Don't cancel all on one failure
)
```

### 3. `asyncio.as_completed()` — Process As Ready
```python
coroutines = [simulated_api_call(i) for i in range(1, 6)]
for completed_coroutine in asyncio.as_completed(coroutines):
    result = await completed_coroutine
    print(result)
```

### 4. `asyncio.wait()` — Fine-Grained Control
```python
done, pending = await asyncio.wait(
    [task1, task2],
    return_when=asyncio.FIRST_COMPLETED
)
# Process done
await asyncio.gather(*pending)  # Wait for remaining
```

### 5. `asyncio.wait_for()` — Timeouts
```python
try:
    result = await asyncio.wait_for(long_operation(), timeout=2)
except asyncio.TimeoutError:
    print("Took too long!")
```

## Critical Reminders

- `await` **required** to yield control. `time.sleep()` instead of `asyncio.sleep()` **blocks thread** and defeats async.
- Always use `asyncio.sleep()` in async code.

## References

- `references/realpython-asyncio-patterns.md` — All patterns with variations
- `references/asyncio-repl-guide.md` — REPL tips and tricks
- `references/blocking-vs-async-libs.md` — Library mapping table