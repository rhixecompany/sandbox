# Asyncio in Python - Full Tutorial - YouTube

> **Source:** https://www.youtube.com/watch?v=Qb9s3UiMSTA
> **Retrieved:** 2026-05-31T12:17:10

---

# Asyncio in Python - Full Tutorial | Tech With Tim

## Overview
This comprehensive tutorial covers Python's `asyncio` library for asynchronous programming, focusing on efficiency in handling I/O-bound tasks like network requests and file operations. The video targets Python 3.11+ and emphasizes practical understanding of core concurrency concepts.

---

## Key Concepts

### 1. **Event Loop**
- Central hub that manages and distributes asynchronous tasks.
- Tasks circle the loop; each gets a turn to execute or pause if waiting (e.g., for I/O).
- When a task `await`s, it yields control back to the loop, allowing other tasks to run.
- Ensures efficient utilization of the program flow without blocking.

> "Think of it as a central hub with tasks circling around it waiting for their turn to be executed."

---

### 2. **Coroutines**
- Defined using `async def`.
- Calling an async function returns a **coroutine object**, which must be **awaited** to execute.
- Use `asyncio.run(coroutine())` to start the event loop and run the top-level coroutine.

#### Example:
```python
import asyncio

async def main():
    print("Start of main coroutine")

asyncio.run(main())
```

> ⚠️ **Important**: A coroutine does **not** start executing until it is awaited or wrapped in a task.

#### `await` Keyword
- Can only be used inside async functions.
- Pauses execution until the awaited coroutine completes.

---

### 3. **Tasks**
- Schedule coroutines to run **concurrently**.
- Created via `asyncio.create_task(coroutine())`.
- Allow overlapping of I/O waits — while one task sleeps/awaits, another can proceed.
- Enable true concurrency for I/O-bound operations without multi-threading.

#### Example:
```python
async def fetch_data(id, delay):
    print(f"Fetching data {id}")
    await asyncio.sleep(delay)
    print(f"Data fetched {id}")
    return f"Data {id}"

async def main():
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    result1 = await task1
    result2 = await task2
    print(result1, result2)

asyncio.run(main())
```

> ✅ **Performance Benefit**: Tasks run concurrently → total time ≈ max(delay), not sum(delays).

#### `asyncio.gather()`
- Simplifies running multiple coroutines concurrently.
- Returns results in order.
- **Limitation**: Poor error handling — does **not** cancel other tasks if one fails.

```python
results = await asyncio.gather(
    fetch_data(1, 2),
    fetch_data(2, 3),
    fetch_data(3, 1)
)
```

#### `asyncio.TaskGroup` (Preferred)
- Introduced in Python 3.11.
- Provides **automatic error handling**: if one task fails, others are cancelled.
- Uses async context manager syntax.

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data(1, 2))
        task2 = tg.create_task(fetch_data(2, 3))
    # All tasks complete here
    print(task1.result(), task2.result())
```

> ✅ **Best Practice**: Use `TaskGroup` over `gather()` for robust error handling.

---

### 4. **Futures**
- Low-level construct representing a **promise of a future result**.
- Rarely used directly in application code; more common in library internals.
- A `Future` is awaited until its result is set by another coroutine/task.

#### Example:
```python
async def set_future_result(future):
    await asyncio.sleep(2)
    future.set_result("Done")

async def main():
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    asyncio.create_task(set_future_result(future))
    result = await future
    print(result)
```

> 🔍 **Key Insight**: Unlike tasks, futures don’t wrap coroutines — they represent a value that will be available later.

---

### 5. **Synchronization Primitives**

#### **Lock**
- Ensures only **one coroutine** accesses a critical section at a time.
- Prevents race conditions on shared resources (e.g., files, databases).

```python
lock = asyncio.Lock()

async def modify_resource():
    async with lock:
        # Critical section
        await asyncio.sleep(1)
        print("Resource modified")
```

> 🛑 **Use Case**: When two coroutines writing to the same file could corrupt data.

#### **Semaphore**
- Limits access to a resource to **N concurrent coroutines**.
- Useful for throttling (e.g., limiting API requests).

```python
sem = asyncio.Semaphore(2)  # Allow 2 at a time

async def access_resource():
    async with sem:
        await asyncio.sleep(1)
        print("Accessed resource")
```

> 📉 **Use Case**: Prevent overwhelming a server with 10,000 simultaneous requests.

#### **Event**
- Simple boolean flag for synchronization.
- One coroutine waits (`event.wait()`); another sets it (`event.set()`).

```python
event = asyncio.Event()

async def waiter():
    await event.wait()
    print("Event set!")

async def setter():
    await asyncio.sleep(2)
    event.set()
```

> ✅ **Use Case**: Signal completion of initialization before proceeding.

> 💡 **Note**: `Condition` primitive exists but was not covered.

---

#

[... summary truncated for context management ...]

---

*Extracted by web-research-pipeline v1.0.0*
