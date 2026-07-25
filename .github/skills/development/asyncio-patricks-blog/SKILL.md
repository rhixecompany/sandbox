---
name: asyncio-patricks-blog
title: "Introduction to AsyncIO in Python (Patrick's Software Blog)"
description: "Use when learning asyncio from Patrick's Software Blog — covers concurrency models, coroutines, event loop, gather/as_completed, semaphore for rate limiting, and practical ReqRes API example with performance comparison."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [asyncio, python, patrick-software-blog, tutorial, concurrency, httpx, semaphore, as-completed]
---
# Introduction to AsyncIO in Python (Patrick's Software Blog)

## Purpose

Patrick's Software Blog tutorial on asyncio for asynchronous programming in Python — focuses on I/O-bound tasks like API calls with practical httpx examples.

## When to Use

- Learning asyncio with practical API examples
- Understanding concurrency control with semaphores
- Performance comparison sync vs async
- Python 3.11+ patterns (TaskGroup mentioned)

## When NOT to Use

- CPU-bound parallelism
- Legacy Python versions
- GUI/event-driven desktop apps

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug async rate limiting, connection pooling |
| `test-driven-development` | Test async API clients |

## Workflow

### Phase 1: Concurrency in Python

**Three approaches:**
1. **Processes** — CPU-bound tasks
2. **Threads** — Shared memory, GIL limitations
3. **asyncio** — **I/O-bound tasks** (networking, file I/O, DB access)

> 📌 **Asynchronous programming not helpful for CPU-bound tasks** — use processes instead.

### Phase 2: Core asyncio Principles

- Built on **coroutines**: special functions that can suspend/resume
- Runs in **single thread** with **event loop** managing execution
- Uses `async def` to define coroutines, `await` to suspend

```python
async def get_user_data(url, index):
    result = await get(url + str(index))
    return result.status_code
```

### Phase 3: Running Coroutines

**Basic Pattern:**
```python
async def main():
    await wait_in_seconds(2)

if __name__ == '__main__':
    asyncio.run(main())
```

**Sequential vs Concurrent:**

Sequential (slow):
```python
await wait_in_seconds(3)  # 3s
await wait_in_seconds(4)  # 4s
await wait_in_seconds(5)  # 5s
# Total = 12s
```

Concurrent with `asyncio.gather()` (fast):
```python
await asyncio.gather(
    wait_in_seconds(3),
    wait_in_seconds(4),
    wait_in_seconds(5)
)
# Total ≈ 5s (longest task)
```

### Phase 4: `asyncio.as_completed()` — Preferred for Streaming

Processes results **as they become available** (non-blocking, real-time output):

```python
coroutines = [simulated_api_call(i) for i in range(1, 6)]
for completed_coroutine in asyncio.as_completed(coroutines):
    result = await completed_coroutine
    print(result)
```

### Phase 5: Practical Example — Fetching User Data (ReqRes API)

**API:** `https://reqres.in/api/users/{id}` returns JSON user data.

**Full Async Script (with `httpx` and `as_completed`):**
```python
import asyncio
import httpx
from utilities import parse_user_data

async def get_user_data(client: httpx.AsyncClient, index: int) -> str:
    url = f'https://reqres.in/api/users/{index}'
    response = await client.get(url, timeout=2.0, follow_redirects=True)
    response.raise_for_status()
    first_name, last_name, email = parse_user_data(response.json())
    return f"User {index}: {first_name} {last_name} - {email}"

async def main():
    async with httpx.AsyncClient() as client:
        coroutines = [get_user_data(client, i) for i in range(1, 11)]
        for completed_coroutine in asyncio.as_completed(coroutines):
            result = await completed_coroutine
            print(result)
```

> 💡 Use **one `AsyncClient`** instance and pass it to coroutines (recommended by `httpx` docs)

**Performance Comparison:**
| Approach | Execution Time |
|----------|----------------|
| **Async (as_completed)** | **0.24 seconds** |
| **Synchronous** | **1.80 seconds** |

→ **~7.5x faster** due to concurrent I/O

### Phase 6: Controlling Concurrency with Semaphore

**Why Limit?** APIs have **rate limits**. Launching 10 simultaneous requests may trigger throttling/bans.

**Using `asyncio.Semaphore`:**
```python
semaphore = asyncio.Semaphore(5)  # Max 5 concurrent

async def get_user_data(..., semaphore):
    async with semaphore:
        # Only 5 coroutines enter this block at once
        response = await client.get(...)
```

**Updated `main()`:**
```python
async def main():
    semaphore = asyncio.Semaphore(5)
    async with httpx.AsyncClient() as client:
        coroutines = [get_user_data(client, i, semaphore) for i in range(1, 11)]
        for completed_coroutine in asyncio.as_completed(coroutines):
            result = await completed_coroutine
            print(result)
```

### Phase 7: Platform Detection & Error Handling

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: Set PROACTOR_EVENT_LOOP=1 for subprocess support")
    elif system == "linux":
        print("Linux: epoll-based selector is default")
    elif system == "darwin":
        print("macOS: kqueue-based selector for high connections")
    return system
```

**Error handling patterns:**
```python
import httpx
import asyncio

async def safe_request(client, url, semaphore, retries=3):
    async with semaphore:
        for attempt in range(retries):
            try:
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
            except httpx.TimeoutException:
                if attempt == retries - 1:
                    raise
                await asyncio.sleep(2 ** attempt)
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 429:
                    # Rate limited
                    await asyncio.sleep(2 ** attempt)
                    continue
                raise
```

### Phase 8: Key Takeaways

- `async def` → defines a coroutine
- `await` → suspends
- `asyncio.run()` → starts event loop
- `asyncio.gather()` → run multiple concurrently
- `asyncio.create_task()` → fire-and-forget (but await later)
- `asyncio.as_completed()` → **preferred** for streaming results
- `asyncio.wait()` → wait for specific conditions (e.g., first done)
- `asyncio.wait_for()` → add timeouts to async operations
- Async = **concurrent on a single thread**, ideal for I/O-bound work

## Pitfalls

- **Forgetting `async with httpx.AsyncClient()`** → connection leaks
- **No semaphore** → API bans
- **Blocking `time.sleep()`** → use `asyncio.sleep()`
- **Not awaiting** → coroutine never runs

## Verification Checklist

- [ ] Sequential vs concurrent timing demonstrated
- [ ] Semaphore limits concurrent requests
- [ ] AsyncClient reused across requests
- [ ] as_completed processes results in completion order
- [ ] Error handling with raise_for_status()

## References

- `references/httpx-async-patterns.md` — Advanced httpx usage
- `references/semaphore-patterns.md` — Dynamic rate limiting
- `references/asyncio-taskgroup.md` — Python 3.11+ structured concurrency

## Templates

- `templates/async-api-client.py` — Reusable async client with semaphore
- `templates/concurrent-fetcher.py` — Generic concurrent fetcher

## Scripts

- `scripts/benchmark-async-vs-sync.py` — Performance measurement
- `scripts/rate-limit-tester.py` — Semaphore behavior verification