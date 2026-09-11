---
name: research-python-asyncio-tutorial
title: Python asyncio Research Digest
description: "Use when learning or applying Python asyncio: event loop, coroutines, tasks, async/await patterns. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [python, asyncio, concurrency, research]
---

# Python asyncio Research Digest

## Overview

Wraps `research/python-asyncio-tutorial/` (7 md files: YouTube transcripts, GeeksforGeeks, Patrick's blog, hands-on walkthrough). Use when writing async Python or teaching asyncio.

## When to Use

- Designing async/await code (event loop, tasks, gather, timeouts)
- Explaining asyncio concepts from multiple angles (beginner → advanced)
- Debugging event-loop issues (blocking calls, unawaited coroutines)

## Workflow

### Phase 1: Digest

```bash
python scripts/research_python_asyncio_tutorial.py
python scripts/research_python_asyncio_tutorial.py --file "research/python-asyncio-tutorial/python-asyncio-part-1-basic-concepts-and-patterns.md"
```

### Phase 2: Apply

- Coroutines: `async def` + `await`; tasks via `asyncio.create_task`
- Concurrency with `asyncio.gather`; timeouts with `asyncio.timeout`
- Never block the loop: no `time.sleep`, use `await asyncio.sleep`
- Pick the file matching depth: basics (part 1), hands-on walkthrough, or full tutorial

### Phase 3: Verify

- Run `python -m asyncio`-style script under `python -m pytest` or direct run; confirm no "coroutine was never awaited" warnings
- Profile with a small gather test comparing sync vs async timing

## Pitfalls

- Mixing threads/blocking IO stalls the event loop — prefer loop.run_in_executor for CPU work
- Windows: ProactorEventLoop default is fine; avoid SelectorEventLoop assumptions

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Code patterns match at least one research source

## References

- `research/python-asyncio-tutorial/asyncio-in-python-full-tutorial-youtube.md`
- `research/python-asyncio-tutorial/asyncio-in-python-geeksforgeeks.md`
- `research/python-asyncio-tutorial/introduction-to-asyncio-in-python-patricks-software-blog.md`
- `research/python-asyncio-tutorial/python-asyncio-explained-in-9-minutes-youtube.md`
- `research/python-asyncio-tutorial/python-asyncio-part-1-basic-concepts-and-patterns.md`
- `research/python-asyncio-tutorial/python-tutorial-asyncio-complete-guide-to-asynchronous-progr.md`
- `research/python-asyncio-tutorial/pythons-asyncio-a-hands-on-walkthrough.md`
- Script: `scripts/research_python_asyncio_tutorial.py` | Test: `scripts/tests/test_research_python_asyncio_tutorial.py`
