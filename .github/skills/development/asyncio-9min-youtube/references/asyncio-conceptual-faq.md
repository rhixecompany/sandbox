# AsyncIO Conceptual FAQ

## Common Misconceptions

### Q: Is asyncio the same as multithreading?
**A:** No. Asyncio uses a single-threaded event loop with cooperative multitasking. Threads use preemptive multitasking managed by the OS.

### Q: Does asyncio bypass the GIL?
**A:** No. Asyncio runs on a single thread and is subject to the GIL. It avoids GIL contention by yielding during I/O waits, but CPU-bound async code still blocks the event loop. Use multiprocessing for CPU-bound parallelism.

### Q: When should I use asyncio vs threading vs multiprocessing?
| Scenario | Recommended |
|----------|-------------|
| HTTP requests, web scraping | **asyncio** (aiohttp/httpx) |
| Database queries | **asyncio** (asyncpg/aiosqlite) |
| File I/O | **asyncio** (aiofiles) |
| CPU-intensive computation | **multiprocessing** |
| Legacy blocking libraries | **threading** (with `run_in_executor`) |

### Q: Can I mix sync and async code?
**A:** Yes, using `asyncio.to_thread()` (3.9+) or `loop.run_in_executor()`:
```python
# Run blocking function in thread pool
result = await asyncio.to_thread(blocking_function, arg1, arg2)

# Or with explicit executor
loop = asyncio.get_running_loop()
result = await loop.run_in_executor(None, blocking_func, arg)
```

### Q: Does asyncio provide true parallelism?
**A:** No. Asyncio provides **concurrency** (interleaved execution) on a single thread, not parallelism. For true parallelism, use `multiprocessing` or run multiple asyncio processes.

### Q: What's the difference between `await`, `create_task()`, and `gather()`?
| Construct | Behavior |
|-----------|----------|
| `await coro()` | Sequential - waits for completion |
| `create_task(coro())` | Schedules concurrently, returns Task immediately |
| `gather(coro1(), coro2())` | Runs concurrently, waits for ALL, returns results list |

### Q: Why does my async code run sequentially?
Common causes:
1. Using `await` in a loop instead of `gather()`/`create_task()`
2. Using blocking calls (`time.sleep`, `requests.get`) instead of async alternatives
3. Not awaiting the coroutine (forgetting `await`)

### Q: When should I use TaskGroup vs gather?
| Scenario | Recommended |
|----------|-------------|
| Fail fast on first error | **TaskGroup** (3.11+) |
| Continue on errors | `gather(..., return_exceptions=True)` |
| Structured concurrency needed | **TaskGroup** |
| Simple concurrent execution | `gather()` |

### Q: What's the difference between `time.sleep()` and `asyncio.sleep()`?
| Function | Behavior |
|----------|----------|
| `time.sleep(1)` | **Blocks thread** - defeats async purpose |
| `await asyncio.sleep(1)` | **Yields control** - allows other tasks to run |

### Q: How do I handle timeouts?
```python
# Per-operation timeout
try:
    result = await asyncio.wait_for(operation(), timeout=5.0)
except asyncio.TimeoutError:
    handle_timeout()

# Overall timeout (3.11+)
async with asyncio.timeout(10):  # 10 second total
    await asyncio.gather(task1(), task2())
```

### Q: How do I debug async code?
1. Enable debug mode: `asyncio.run(main(), debug=True)`
2. Set `PYTHONASYNCIODEBUG=1` environment variable
3. Use `asyncio.get_event_loop().set_debug(True)`
4. Log task creation/completion
5. Use `asyncio.all_tasks()` to inspect pending tasks