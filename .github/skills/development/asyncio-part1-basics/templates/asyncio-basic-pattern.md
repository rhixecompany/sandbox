# Asyncio Basic Pattern

## Async Function Template
```python
import asyncio

async def main():
    # Your async code here
    result = await async_operation()
    print(f"Result: {result}")

def async_operation():
    return asyncio.sleep(0, "completed")

if __name__ == "__main__":
    asyncio.run(main())
```

## Async Context Manager Template
```python
class AsyncResource:
    async def __aenter__(self):
        await self.open()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
    
    async def open(self):
        pass
    
    async def close(self):
        pass
```

## Concurrent Tasks Template
```python
async def run_concurrent():
    tasks = [
        asyncio.create_task(task1()),
        asyncio.create_task(task2()),
        asyncio.create_task(task3()),
    ]
    results = await asyncio.gather(*tasks)
    return results
```