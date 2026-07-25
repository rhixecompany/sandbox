# Asyncio Shutdown Debugging Reference

Full pattern from a Hermes MCP event-loop shutdown debugging session.

## Symptom Log Output

```
ERROR asyncio: Task was destroyed but it is pending!
task: <Task pending name='Task-322'
  coro=<MCPServerTask.run() running at ...mcp_tool.py:3272>
  wait_for=<Future pending cb=[Task.task_wakeup()]>>

ERROR asyncio: Task was destroyed but it is pending!
task: <Task cancelling name='Task-335'
  coro=<Event.wait() running at ...asyncio/locks.py:213>

ERROR asyncio: Exception in callback BaseProactorEventLoop._start_serving...
  File "...\proactor_events.py", line 840, in loop
  ...
  File "...\base_events.py", line 295, in _attach
    assert self._sockets is not None
```

## Step-by-Step Investigation

### Step 1: Identify which coroutines are pending

From the first error: `MCPServerTask.run()` at line 3272.  Looking at that
line in `tools/mcp_tool.py`:

```python
# Line 3272
parked = await self._wait_for_reconnect_or_shutdown(
    timeout=_PARKED_RETRY_INTERVAL  # 300 seconds
)
```

The task was **parked** (initial connect retries exhausted, wait-for-reconnect
or shutdown).  It would wait up to 300s unless the `_shutdown_event` fired.

### Step 2: Identify helper tasks

The `_wait_for_reconnect_or_shutdown` method creates two helper tasks:

```python
shutdown_task = asyncio.ensure_future(self._shutdown_event.wait())
reconnect_task = asyncio.ensure_future(self._reconnect_event.wait())
```

These are the `Event.wait()` tasks that appear as "cancelling" in the second
error.  When the parent task is cancelled, the `finally` block in
`_wait_for_reconnect_or_shutdown` should cancel them and await them — but
if the loop closes before this completes, they get destroyed.

### Step 3: Trace the shutdown call chain

```
shutdown_mcp_servers()                       # line 6178
  └─ safe_schedule_threadsafe(_shutdown(), loop)
       └─ _shutdown()                        # line 6201 (async)
            └─ asyncio.gather(server.shutdown() for each server)
                 └─ server.shutdown()         # line 3424
                      └─ _shutdown_event.set()
                      └─ _reconnect_event.set()
                      └─ await asyncio.wait_for(self._task, timeout=10)
                           └─ if timeout: task.cancel()
  └─ future.result(timeout=15)               # blocks main thread
  └─ _stop_mcp_loop()                        # line 6385
       └─ loop.call_soon_threadsafe(loop.stop)
       └─ thread.join(timeout=5)
       └─ loop.close()                       # <-- pending tasks die here
```

### Step 4: Identify the gap

Between steps 1–3, `server.shutdown()`:
1. Sets `_shutdown_event` — this should unblock the parked task.
2. Waits for `self._task` with a 10s timeout.
3. If timeout expires, cancels the task and awaits it.

If the parked task doesn't complete within 10s (the event-sett → asyncio.wait
→ return path), and the cancel-sweep doesn't happen before `_stop_mcp_loop`
runs, the task is still pending when `loop.close()` destroys it.

### Step 5: Fix

The fix in `_stop_mcp_loop()`: before `loop.stop()`, cancel all pending tasks
on the loop so the final `loop.close()` has nothing to report.

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

## Proactor AssertionError Fix

The `BaseProactorEventLoop._start_serving` function registers IOCP
completion callbacks.  After `loop.close()` nulls out the server's
`_sockets`, a late-arriving IOCP notification fires the callback which
tries to create a transport for the closed server.  This hits
`assert self._sockets is not None` in `base_events.py`.

The fix: suppress only the proactor-related `AssertionError` in the
loop's exception handler (do NOT suppress all assertion errors):

```python
def _mcp_loop_exception_handler(loop, context):
    exc = context.get("exception")
    message = context.get("message", "")
    if isinstance(exc, RuntimeError) and "Event loop is closed" in message:
        return
    if isinstance(exc, AssertionError) and (
        "_start_serving" in message
        or "_sockets" in str(exc)
    ):
        return
    loop.default_exception_handler(context)
```

## Verification Commands

```bash
# Syntax check
python -m py_compile tools/mcp_tool.py

# MCP-specific tests
pytest tests/tools/test_mcp_probe.py -x --tb=short -q
pytest tests/tools/test_mcp_bridge_single_failure.py -x --tb=short -q
pytest tests/tools/test_mcp_loop_profile_override.py -x --tb=short -q
pytest tests/tools/test_mcp_poll_loop_oom_integration.py -x --tb=short -q
```
