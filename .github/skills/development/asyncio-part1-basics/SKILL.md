---
name: asyncio-part1-basics
title: "Python AsyncIO Part 1 – Basic Concepts and Patterns (BBC)"
description: "Use when learning asyncio concepts from BBC's cloudfit-public-docs — focuses on what asyncio is/isn't, CPU-bound vs I/O-bound, subroutines vs coroutines, and event loop architecture without code examples."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [asyncio, python, concepts, bbc, cloudfit, event-loop, tasks, coroutines, conceptual]
---
# Python AsyncIO Part 1 – Basic Concepts and Patterns (BBC)

## Purpose

Conceptual foundation for Python's asyncio from BBC's cloudfit docs — what it is, what it isn't, and core architecture without syntax.

## When to Use

- Understanding asyncio purpose before learning syntax
- Explaining asyncio to stakeholders
- Architecture decisions (async vs threads vs processes)
- Prerequisites for Part 2 (awaitables, tasks, futures)

## When NOT to Use

- Learning syntax (use Part 2 or other tutorials)
- Writing code (no code examples in this part)
- Debugging async code

## Skills Required

| Skill | Purpose |
|-------|---------|
| `writing-plans` | Plan async architecture for I/O-bound services |

## Workflow

### Phase 1: Core Insight

**Asyncio is NOT about multithreading or bypassing GIL.** It's about **efficiently using a single CPU core** during I/O-bound operations.

### Phase 2: CPU-bound vs I/O-bound

| Type | Characteristics | Example |
|------|----------------|---------|
| **CPU-bound** | Continuously uses CPU | Complex calculations, image processing |
| **I/O-bound** | Frequently waits for external responses | HTTP requests, file reads, database queries |

> **Asyncio's Purpose:** Allows other tasks to run while one task waits for I/O — maximizing single-core efficiency.

### Phase 3: Subroutines vs Coroutines

| Model | Behavior |
|-------|----------|
| **Subroutine** | Functions run start-to-finish; each call independent |
| **Coroutine** | Functions can **yield control** back to caller and **resume from where they left off** on next call |

Python supports coroutines via:
- **Generators** (historical)
- **Asyncio coroutines** (modern, natural syntax for non-blocking code)

> Coroutines enable **cooperative multitasking**: control bounces between tasks only when one yields.

### Phase 4: AsyncIO Architecture — Event Loop, Tasks, and Coroutines

**Key Components:**
- **Event Loop**: Central scheduler in each thread; manages list of **Tasks**
- **Task**: Wraps a coroutine; maintains own **stack and execution state**
- **Coroutine**: Function that can **yield control** when waiting for I/O

**How It Works:**
1. Only **one Task executes at a time**
2. When Task hits I/O wait, it **yields control** to Event Loop
3. Event Loop **pauses that Task** and **wakes another ready Task**
4. When awaited I/O completes, original Task **resumes from where it left off**

> ⚠️ **Important:** Event Loop **cannot forcibly interrupt** a running coroutine. Control transfers only when coroutine **explicitly yields**.

### Phase 5: Why This Matters

- **Efficiency**: Avoids idle CPU time during I/O waits
- **Scalability**: Handles thousands of concurrent connections without threads
- **Simplicity**: Avoids thread-safety issues (no shared-state concurrency)
- **Ideal For**: Web APIs, network services, any I/O-bound workload

> "Anything dealing with HTTP or other internet traffic protocols is almost guaranteed to be IO bound."

### Phase 6: Platform Considerations

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        # Windows: ProactorEventLoop by default (Python 3.8+)
        print("Windows - using ProactorEventLoop")
    elif system == "linux":
        # Linux: SelectorEventLoop (efficient epoll)
        print("Linux - using SelectorEventLoop")
    elif system == "darwin":
        # macOS: KqueueSelector (handles high FD count)
        print("macOS - using KqueueSelector")
    return system
```

> **Windows note:** Python 3.8+ uses ProactorEventLoop by default for asyncio. Subprocess handling differs from Unix — use `asyncio.create_subprocess_exec` with care.

### Phase 7: Common Errors & Resolution

```python
# RuntimeError: This event loop is already running
# Fix: Use asyncio.run() instead of get_event_loop().run_forever()
asyncio.run(main())

# RuntimeError: Cannot close a running event loop
# Fix: Ensure all tasks complete before closing
async def cleanup():
    tasks = asyncio.all_tasks()
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)

# TypeError: object NoneType can't be used in 'await' expression
# Fix: Use async def and await only on coroutines/awaitables
```

### Phase 8: What's Next

Part 2 covers practical syntax: `async`/`await`, creating/managing Tasks, working with Futures and Awaitables.

## Pitfalls

- Expecting parallelism (it's cooperative, single-threaded)
- Using for CPU-bound work (use multiprocessing instead)
- Assuming event loop can preempt (it can't; must yield)

## Verification Checklist

- [ ] Can explain why asyncio ≠ threading/multiprocessing
- [ ] Can distinguish CPU-bound vs I/O-bound
- [ ] Understands coroutine yield/resume model
- [ ] Knows event loop role and limitation

## References

- `references/asyncio-conceptual-faq.md` — Common misconceptions
- `references/part2-awaitables-tasks-futures.md` — Link to Part 2
- `references/asyncio-debugging.md` — Debugging asyncio code

## Templates

- `templates/asyncio-basic-pattern.md` — Template for async functions

## Scripts

- `scripts/asyncio-pitfalls.py` — Common asyncio pitfalls demo