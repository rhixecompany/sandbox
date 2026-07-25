# Async vs Threading Comparison

## Concurrency Models

### Asyncio (Cooperative Multitasking)
- **Single thread** - one execution context
- **Explicit yielding** - `await` explicitly yields control
- **Event loop** - central scheduler managing all tasks
- **No race conditions** - no preemptive interruption
- **Lower memory** - no thread stack overhead
- **Best for**: I/O-bound tasks (HTTP, DB, file I/O, web scraping)

### Multi-threading (Preemptive Multitasking)
- **Multiple threads** - each with own stack
- **Preemptive scheduling** - OS decides when to switch
- **GIL limitations** - Python threads don't run Python bytecode in parallel
- **Race conditions** - need locks, mutexes for shared data
- **Higher overhead** - thread creation, context switching
- **Best for**: CPU-bound tasks that release GIL (NumPy, C extensions), legacy blocking libraries

## When to Use Which

| Scenario | Recommended |
|----------|-------------|
| HTTP APIs, web scraping | **asyncio** (aiohttp, httpx) |
| Database queries | **asyncio** (asyncpg, aiosqlite) |
| File I/O (many small files) | **asyncio** (aiofiles) |
| CPU-intensive math | **multiprocessing** |
| Image/video processing | **multiprocessing** or threads (NumPy releases GIL) |
| Legacy blocking library | **threading** (run_in_executor) |
| GUI applications | **threading** (keep UI responsive) |

## Hybrid Approach

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)

async def run_blocking_io():
    # Run blocking function in thread pool
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, blocking_function, arg1, arg2)
    return result

# Python 3.9+ simpler syntax
result = await asyncio.to_thread(blocking_function, arg1, arg2)
```

## Performance Characteristics

| Metric | Asyncio | Threading |
|--------|---------|-----------|
| Memory per task | ~1KB | ~8MB (stack) |
| Context switch | ~1μs | ~10-100μs |
| Max concurrent | 10,000+ | ~100-1000 |
| Startup time | ~0.1ms | ~1ms |

## When NOT to Use Asyncio

1. **CPU-bound work** - no true parallelism
2. **Simple scripts** - overhead not worth it
2. **Legacy sync libraries** - unless wrapped
3. **Real-time systems** - no timing guarantees