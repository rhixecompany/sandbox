# AsyncIO Advanced Patterns - Real Python

## Coroutine Chaining

```python
async def get_user_with_posts(user_id):
    user = await fetch_user(user_id)
    await fetch_posts(user)
    return user
```

## gather() - All Results Together

```python
results = await asyncio.gather(
    func1(), func2(), func3(),
    return_exceptions=True  # Don't cancel on error
)
```

## as_completed() - Process As Ready

```python
coroutines = [simulated_api_call(i) for i in range(1, 6)]
for completed_coroutine in asyncio.as_completed(coroutines):
    result = await completed_coroutine
    print(result)
```

## wait() - Fine-Grained Control

```python
done, pending = await asyncio.wait(
    [task1, task2],
    return_when=asyncio.FIRST_COMPLETED
)
# Process done
await asyncio.gather(*pending)  # Wait for remaining
```

## wait_for() - Timeouts

```python
try:
    result = await asyncio.wait_for(long_operation(), timeout=2)
except asyncio.TimeoutError:
    print("Took too long!")
```

## Critical Reminders

- `await` **required** to yield control. `time.sleep()` instead of `asyncio.sleep()` **blocks thread** and defeats async.
- Always use `asyncio.sleep()` in async code.