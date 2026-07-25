---
name: event-loop-debugging
title: "Event Loop Lifecycle Debugging"
description: "Diagnose asyncio event loop shutdown races, pending task destruction, cancellation propagation failures, and proactor-event-loop quirks on Windows. Covers Hermes MCP event loop specifically and general patterns."
version: 1.0.0
author: Alexa
license: MIT
tags: [debugging, asyncio, event-loop, windows, mcp]
---

# Event Loop Lifecycle Debugging

## When to Use

Use when the Hermes log (or stderr) contains any of:

- **"Task was destroyed but it is pending!"** — tasks survive past `loop.close()`
- **"Exception in callback BaseProactorEventLoop._start_serving"** with
  `assert self._sockets is not None` — Windows proactor socket race
- **"Exception in callback ... __del__"** with "Event loop is closed" —
  transport finalizers hitting a dead loop
- Intermittent **MCP tool failures** that correlate with event loop restarts
- **Session startup/restart cycles** where MCP servers never fully reconnect

## Investigation Pattern

### 1. Read the error messages — don't skip them

Every "Task was destroyed" message contains:
- The **task name and coroutine** (`MCPServerTask.run()`, `Event.wait()`, etc.)
- The **source line number** in the coroutine — this tells you exactly what
  `await` was blocking when the loop was closed
- A **child future** (`wait_for=<Future pending cb=[Task.task_wakeup()]>`)
  that reveals what the task was waiting on internally

**Action:** Read the surrounding code at the reported line number to understand
the lifecycle phase the task was in (parked, retrying, connected, etc.).

### 2. Correlate timestamps across occurrences

Batch the errors by timestamp:

| Pattern | Meaning |
|---------|---------|
| Errors seconds apart, same process | Single shutdown where cleanup raced |
| Errors 10–30 minutes apart | Process restarts — each restart leaves some tasks behind |
| Errors clustered around session timestamps | Per-agent-session loop restart pattern |

**Action:** For restart patterns, look at how the loop is stopped between
sessions (probe cleanup, idle stopping, explicit shutdown).

### 3. Trace the shutdown/restart path

Find the code that calls `loop.stop()` + `loop.close()` and determine whether
all tasks are cancelled before that point:

```python
# Suspect pattern — loop is closed without cancelling tasks:
loop.call_soon_threadsafe(loop.stop)
thread.join(timeout=5)
loop.close()  # <-- pending tasks get destroyed here
```

**Action:** Use `search_files` to find all callers of the loop-stopping function.

### 4. Check each class of pending task

- **MCPServerTask.run()** tasks — set `_shutdown_event` on their owning
  `MCPServerTask` and wait for them, OR cancel them.
- **Event.wait()** helper tasks — children of `_wait_for_reconnect_or_shutdown`
  or `_wait_for_lifecycle_event`; they're cleaned up when the parent task
  responds to cancellation.
- **Background refresh tasks** — any `asyncio.create_task` call that spawns
  work without tracking it in a set/collection that gets waited on shutdown.

## Common Fix Patterns

### 1. Cancel-all sweep before loop.stop()

The most robust fix: before stopping the loop, inject a coroutine that
cancels every pending task (except itself) and waits briefly:

```python
if loop.is_running():
    async def _cancel_pending():
        current = asyncio.current_task()
        pending = [
            t for t in asyncio.all_tasks(loop)
            if t is not current and not t.done()
        ]
        if not pending:
            return
        for t in pending:
            t.cancel()
        await asyncio.wait(pending, timeout=3,
                           return_when=asyncio.ALL_COMPLETED)
    try:
        future = asyncio.run_coroutine_threadsafe(_cancel_pending(), loop)
        future.result(timeout=5)
    except (asyncio.TimeoutError, Exception):
        pass
```

### 2. Suppress benign exception-handler noise

The loop's custom exception handler should suppress both:

```python
def loop_exception_handler(loop, context):
    exc = context.get("exception")
    if isinstance(exc, RuntimeError) and "Event loop is closed" in str(exc):
        return
    # Windows proactor race: IOCP notification fires after loop.close()
    # nulls Server._sockets. Match on context to avoid masking real assertion failures.
    if isinstance(exc, AssertionError) and (
        "_start_serving" in str(context.get("message", ""))
        or "_sockets" in str(exc)
    ):
        return
    loop.default_exception_handler(context)
```

### 3. Track every create_task in a set

For background tasks that should be cleaned up on shutdown:

```python
self._pending_tasks: set[asyncio.Task] = set()

def _spawn(self, coro):
    task = asyncio.create_task(coro)
    self._pending_tasks.add(task)
    task.add_done_callback(self._pending_tasks.discard)
    return task

async def shutdown(self):
    for t in list(self._pending_tasks):
        t.cancel()
    await asyncio.gather(*self._pending_tasks, return_exceptions=True)
```

## Windows Quirks

Python's `ProactorEventLoop` (the default on Windows) behaves differently
from the `SelectorEventLoop` on POSIX:

- **IOCP completion callbacks** fire independently of the asyncio task
  scheduler.  A server that was closed can still receive IOCP notifications,
  leading to `AssertionError` in `Server._attach()`.
- **`loop.close()` is not atomic** — transport finalizers scheduled by
  `__del__` may fire on the already-closed loop, raising `RuntimeError`.
- The same code that runs cleanly on Linux/Mac may produce spurious
  `AssertionError` / `RuntimeError` warnings on Windows that are safe to
  suppress in the exception handler.

## Verification

After applying fixes:

```bash
# Syntax check
python -m py_compile tools/mcp_tool.py

# Run MCP tests
pytest tests/tools/test_mcp_probe.py -x --tb=short -q
pytest tests/tools/test_mcp_bridge_single_failure.py -x --tb=short -q

# Run loop-specific tests
pytest tests/tools/test_mcp_loop_profile_override.py -x --tb=short -q
pytest tests/tools/test_mcp_poll_loop_oom_integration.py -x --tb=short -q

# Monitor logs for "Task was destroyed" during real shutdown
grep -i "Task was destroyed" $HERMES_HOME/agent.log
```

## Pitfalls

- **Cancelling all tasks can cancel the `_cancel_pending` sweeper itself.**
  Always exclude `asyncio.current_task()` — see the pattern above.
- **`asyncio.wait(pending, timeout=3)` returns when the timeout elapses,**
  even if some tasks haven't responded yet.  That's fine — any task still
  cancelling after the timeout was already notified and the remaining
  cleanup is best-effort.
- **Suppressing AssertionError is safe only in a tightly-scoped exception
  handler** like the MCP loop's handler.  Never suppress AssertionError
  in a broad/program-wide handler — it masks real logic bugs.
- **On Python 3.11+, `asyncio.CancelledError` inherits from `BaseException`,**
  not `Exception`.  Code that does `except Exception:` will NOT catch
  CancelledError.  Any code that wraps `await` and catches broadly must
  also catch CancelledError and re-raise, or the task cancellation will
  be silently swallowed and the task will never terminate.

## References

- `references/asyncio-shutdown-debugging.md` — Full transcript patterns from
  a Hermes MCP event-loop shutdown debugging session, including exact log
  messages and step-by-step trace.
