# Asyncio Event-Loop Cleanup Debugging

## Symptoms

- **"Task was destroyed but it is pending!"** — logged when `loop.stop()` + `loop.close()` is called while asyncio Tasks are still alive. The callback chain is: pending `Task.__del__` → `loop.call_exception_handler()` → `logger.error("Task was destroyed but it is pending!")`.
- **`AssertionError: assert self._sockets is not None`** on Windows — `BaseProactorEventLoop._start_serving` callback fires during loop shutdown after `Server._sockets` was set to `None` by `loop.close()`.

## Root Cause

**Both errors share the same root pattern:** the event loop is stopped and closed while work is still pending on it.

For the Task-destroyed error:
```python
# BROKEN: stop + close without cancelling pending tasks
loop.stop()
loop.close()  # asyncio logs "Task was destroyed but it is pending!"
```

For the AssertionError:
```python
# DEFAULT exception handler only catches RuntimeError
def _mcp_loop_exception_handler(self, loop, context):
    exc = context.get("exception")
    if isinstance(exc, RuntimeError) and "Event loop is closed" in str(exc):
        return  # Suppress — benign teardown race
    # But AssertionError from ProactorEventLoop._start_serving
    # reaches the default handler uncaught
    loop.default_exception_handler(context)
```

## Fix Pattern: Cancel-Then-Close

### Step 1: Cancel all pending tasks before stopping

```python
async def _cancel_pending():
    """Cancel all non-completed tasks on this loop before shutdown."""
    pending = [
        t for t in asyncio.all_tasks()
        if not t.done() and t is not asyncio.current_task()
    ]
    if not pending:
        return
    for t in pending:
        t.cancel()
    # Wait briefly for CancelledError to propagate
    await asyncio.wait(pending, timeout=3.0)

def _stop_mcp_loop(self, loop):
    # Schedule cancellation on the MCP loop, then stop+close
    asyncio.run_coroutine_threadsafe(_cancel_pending(), loop).result()
    loop.stop()
    loop.close()
```

### Step 2: Extend exception handler for AssertionError

```python
def _mcp_loop_exception_handler(self, loop, context):
    exc = context.get("exception")
    # Suppress benign teardown races
    if isinstance(exc, RuntimeError) and "Event loop is closed" in str(exc):
        return
    if isinstance(exc, AssertionError) and "_sockets" in str(exc):
        return  # ProactorEventLoop._start_serving races with close()
    loop.default_exception_handler(context)
```

## Detection

```bash
# Find the "Task was destroyed" pattern in logs
grep -rn "Task was destroyed but it is pending" logs/

# Find proactor AssertionError
grep -rn "assert self._sockets is not None" --include="*.log" --include="*.py"

# Find places that stop+close without cancelling
grep -rn "loop\.stop\|loop\.close" tools/mcp_tool.py
```

## Prevention

When writing code that manages an event loop lifecycle:

1. **Always cancel pending tasks** before `loop.stop()`/`loop.close()`. A silent close kills pending tasks and logs the warning.
2. **Always suppress benign teardown exceptions** in custom exception handlers — `RuntimeError("Event loop is closed")` and `AssertionError("self._sockets is not None")` are expected during normal shutdown.
3. **Use `asyncio.run_coroutine_threadsafe()`** to schedule cleanup coroutines on the target loop from a different thread.
4. **Set a timeout** on `asyncio.wait()` during cancellation — some tasks may hang (e.g., stuck HTTP transports), and you don't want to block shutdown indefinitely.

## Related

- `skill_view("event-loop-debugging")` — Comprehensive asyncio event-loop debugging skill with additional patterns (task tracking sets, Windows quirks, verification)
- Python docs: [asyncio event loop](https://docs.python.org/3/library/asyncio-eventloop.html)
- CPython source: `asyncio/base_events.py:295` — `Server._attach()` assertion
- CPython source: `asyncio/proactor_events.py:840` — ProactorEventLoop exception path
