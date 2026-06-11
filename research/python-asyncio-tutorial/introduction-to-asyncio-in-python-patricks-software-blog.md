# Introduction to asyncio in Python | Patrick's Software Blog

> **Source:** https://www.patricksoftwareblog.com/introduction_to_asyncio_in_python.html
> **Retrieved:** 2026-05-31T12:17:10

---

# Introduction to asyncio in Python – Summary

## Overview
This tutorial introduces **asyncio** for asynchronous programming in Python, focusing on I/O-bound tasks like API calls. It covers core concepts, practical examples, and best practices for writing concurrent code using coroutines, `async`/`await`, and tools like `gather()`, `as_completed()`, and `Semaphore`.

> **Source**: [Patrick's Software Blog](https://www.patricksoftwareblog.com/introduction_to_asyncio_in_python.html)  
> **Code**: [GitLab Repository](https://gitlab.com/patkennedy79/asyncio_example)

---

## Key Concepts

### Concurrency in Python
Concurrency enables the **perception** of multiple tasks running simultaneously (via task switching). Three main approaches:
1. **Processes** – best for CPU-bound tasks
2. **Threads** – shared memory, GIL limitations
3. **asyncio** – ideal for I/O-bound tasks (networking, file I/O, DB access)

> 📌 **Asynchronous programming is not helpful for CPU-bound tasks** — use processes instead.

### Core asyncio Principles
- Built on **coroutines**: special functions that can suspend/resume execution.
- Runs in a **single thread** with an **event loop** managing coroutine execution.
- Uses `async def` to define coroutines and `await` to suspend until a result is ready.

```python
async def get_user_data(url, index):
    result = await get(url + str(index))
    return result.status_code
```

---

## Running Coroutines

### Basic Pattern
Always use `asyncio.run(main())` to start the event loop:

```python
async def main():
    await wait_in_seconds(2)

if __name__ == '__main__':
    asyncio.run(main())
```

### Sequential vs Concurrent Execution
Using `await` on multiple coroutines **sequentially** adds up wait times:

```python
await wait_in_seconds(3)  # waits 3s
await wait_in_seconds(4)  # then waits 4s → total = 7s
```

Output:
```
Completed operation in 7.006342 seconds!
```

> ❗ `await` suspends the **current** coroutine — it does **not** run concurrently by itself.

---

## Running Coroutines Concurrently

### `asyncio.gather()`
Runs multiple coroutines concurrently; returns results **only after all complete**.

```python
await asyncio.gather(wait_in_seconds(3), wait_in_seconds(4), wait_in_seconds(5))
```
- Total time ≈ longest task (~5s)
- Results returned together after all finish

✅ Best when you need **all results at once**

### `asyncio.as_completed()`
Processes results **as they become available** (non-blocking, real-time output):

```python
coroutines = [simulated_api_call(i) for i in range(1, 6)]
for completed_coroutine in asyncio.as_completed(coroutines):
    result = await completed_coroutine
    print(result)
```

✅ **Preferred approach** for handling streaming or early results

---

## Practical Example: Fetching User Data from ReqRes API

### API Endpoint
`https://reqres.in/api/users/{id}` returns JSON user data.

### Full Async Script (with `httpx` and `as_completed`)
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

### Performance Comparison
| Approach | Execution Time |
|--------|----------------|
| **Async (as_completed)** | **0.24 seconds** |
| **Synchronous** | **1.80 seconds** |

→ **~7.5x faster** due to concurrent I/O

---

## Controlling Concurrency with Semaphore

### Why Limit Concurrency?
APIs often have **rate limits**. Launching 10 simultaneous requests may trigger throttling or bans.

### Using `asyncio.Semaphore`
Limits number of concurrent coroutines:

```python
semaphore = asyncio.Semaphore(5)  # Max 5 concurrent

async def get_user_data(..., semaphore):
    async with semaphore:
        # Only 5 coroutines can enter this block at once
        response = await client.get(...)
```

Updated `main()`:
```python
async def main():
    semaphore = asyncio.Semaphore(5)
    async with httpx.AsyncClient() as client:
        coroutines = [get_user_data(client, i, semaphore) for i in range(1, 11)]
        for completed_coroutine in asyncio.as_completed(coroutines):
            result = await completed_coroutine
            print(result)
```

✅ Prevents overwhelming external services  
✅ Maintains high performance while respecting limits

---

## Key Takeaways

### Core asyncio Rules
- `async def` → defines a coroutine
- `await` → suspends

[... summary truncated for context management ...]

---

*Extracted by web-research-pipeline v1.0.0*
