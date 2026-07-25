# AsyncIO REPL Guide

## Starting the REPL

```bash
python -m asyncio
```

## Basic Usage

```python
>>> import asyncio
>>> async def hello():
...     await asyncio.sleep(1)
...     return "hello"
...
>>> await asyncio.run(coro)
# TypeError: await outside async function
>>> await coro
# TypeError: coroutine not awaited in async context
>>> await asyncio.run(coro)
RuntimeError: cannot run event loop while another is running

# CORRECT:
>>> await asyncio.run(main())
```

## Using await at Top Level

In the asyncio REPL, you can use `await` directly:

```python
>>> async def main():
...     await asyncio.sleep(1)
...     return "done"
...
>>> await main()
'done'
```

## Running Coroutines

```python
>>> async def slow():
...     await asyncio.sleep(2)
...     return "done"
...
>>> asyncio.run(slow())
'done'

# Multiple
>>> async def fast():
...     await asyncio.sleep(0.1)
...     return "fast"
...
>>> await asyncio.gather(slow(), fast())
['done', 'fast']
```

## Inspecting Tasks

```python
>>> import asyncio
>>> async def slow():
...     await asyncio.sleep(2)
...     return "done"
...
>>> task = asyncio.create_task(slow())
>>> task
<Task pending name='Task-1' coro=<slow() running at <stdin>:1>>

>>> asyncio.all_tasks()
{<Task pending name='Task-2' coro=<slow() running at <stdin>:1>>}
```

## Tips

1. **Tab completion** works for async methods
2. **Ctrl+C** cancels running coroutine
3. **Top-level await** works without `asyncio.run()`
4. **History** works with up/down arrows
5. **Exit** with `exit()` or Ctrl+D

## Debugging

```python
>>> import asyncio
>>> asyncio.get_event_loop().set_debug(True)
>>> asyncio.get_event_loop().slow_callback_duration = 0.1
```