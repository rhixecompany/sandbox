# AsyncIO Conceptual FAQ

## Common Misconceptions

### Q: Is asyncio the same as multithreading?
**A:** No. Asyncio uses a single-threaded event loop with cooperative multitasking. Threads use preemptive multitasking managed by the OS. Asyncio avoids GIL contention for I/O-bound tasks but cannot parallelize CPU work.

### Q: Does asyncio bypass the GIL?
**A:** No. Asyncio runs on a single thread and is subject to the GIL. It avoids GIL contention by yielding during I/O waits, but CPU-bound async code still blocks the event loop. Use `multiprocessing` for CPU-bound parallelism.

### Q: Can I use blocking libraries (requests, time.sleep) in async code?
**A:** Not recommended. Blocking calls freeze the entire event loop. Use async alternatives:
- `requests` → `aiohttp` or `httpx`
- `time.sleep` → `asyncio.sleep`
- `sqlite3` → `aiosqlite`
- `psycopg2` → `asyncpg`

### Q: When should I use asyncio vs threading vs multiprocessing?
| Scenario | Recommended |
|----------|-------------|
| HTTP APIs, web scraping, DB queries | asyncio |
| CPU-intensive computation | multiprocessing |
| Legacy blocking libraries | threading (with `run_in_executor`) |
| Mixed I/O + CPU | asyncio + multiprocessing hybrid |

### Q: Does asyncio provide true parallelism?
**A:** No. Asyncio provides **concurrency** (interleaved execution) on a single thread, not parallelism. For true parallelism, use `multiprocessing` or run multiple asyncio processes.

### Q: What's the difference between `await`, `asyncio.create_task()`, and `asyncio.gather()`?
| Construct | Behavior |
|-----------|----------|
| `await coro()` | Sequential - waits for completion before continuing |
| `create_task(coro())` | Schedules concurrently, returns Task immediately |
| `gather(coro1(), coro2())` | Runs concurrently, waits for ALL, returns results list |

### Q: Why does my async code run sequentially?
Common causes:
1. Using `await` in a loop instead of `gather`/`create_task`
2. Using blocking calls (`time.sleep`, `requests.get`) instead of async alternatives
3. Not awaiting the coroutine (forgetting `await`)

### Q: Can I mix sync and async code?
**A:** Yes, using `asyncio.run_in_executor()` or `asyncio.to_thread()` (Python 3.9+):
```python
# Run blocking function in thread pool
result = await asyncio.to_thread(blocking_function, arg1, arg2)
```

### Q: What's the event loop and can I have multiple?
**A:** One event loop per thread. Most apps use one loop. Nested loops require `asyncio.new_event_loop()` and `set_event_loop()`. Avoid multiple loops unless necessary.

### Q: How do I handle exceptions in concurrent tasks?
```python
# Option 1: gather with return_exceptions
results = await asyncio.gather(*tasks, return_exceptions=True)
for r in results:
    if isinstance(r, Exception):
        logger.error(r)

# Option 2: TaskGroup (Python 3.11+)
async with asyncio.TaskGroup() as tg:
    tg.create_task(coro1())
    tg.create_task(coro2())
# First exception cancels all others automatically
```

### Q: How do I debug async code?
1. Enable debug mode: `asyncio.run(main(), debug=True)`
2. Set `PYTHONASYNCIODEBUG=1` environment variable
3. Use `asyncio.get_event_loop().set_debug(True)`
4. Log task creation/completion with `logging`
5. Use `asyncio.all_tasks()` to inspect pending tasks

### Q: What are common performance pitfalls?
1. **Not reusing client sessions** - Create one `aiohttp.ClientSession`/`httpx.AsyncClient` and reuse
2. **No concurrency limits** - Use `Semaphore` to prevent overwhelming servers
3. **Blocking in async callbacks** - Move CPU work to `run_in_executor`
4. **Creating too many tasks** - Use `asyncio.Semaphore` or `asyncio.Queue` for backpressure
5. **Not closing resources** - Use `async with` for sessions, connections, files

### Q: When should I use TaskGroup vs gather?
| Scenario | Recommendation |
|----------|----------------|
| Need all results, failures OK | `gather(..., return_exceptions=True)` |
| Fail fast on first error | `TaskGroup` (3.11+) |
| Need structured concurrency | `TaskGroup` |
| Simple fire-and-forget | `create_task()` + `gather()` |