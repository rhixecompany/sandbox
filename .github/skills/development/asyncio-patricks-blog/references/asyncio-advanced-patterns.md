# Patrick's Blog Async Patterns

## Concurrent HTTP Requests

```python
import asyncio
import httpx

async def fetch_url(client, url):
    response = await client.get(url)
    return response.status_code, len(response.content)

async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    return results

# Semaphore for limiting concurrency
async def fetch_limited(client, url, semaphore):
    async with semaphore:
        return await fetch_url(client, url)

async def fetch_with_limit(urls, max_concurrent=10):
    semaphore = asyncio.Semaphore(max_concurrent)
    async with httpx.AsyncClient() as client:
        tasks = [fetch_limited(client, url, semaphore) for url in urls]
        return await asyncio.gather(*tasks)
```

## as_completed Pattern

```python
async def process_as_completed(urls):
    async with httpx.AsyncClient() as client:
        tasks = {asyncio.create_task(fetch_url(client, url)): url for url in urls}
        
        for completed_task in asyncio.as_completed(tasks):
            url = tasks[completed_task]
            try:
                result = await completed_task
                print(f"{url}: {result}")
            except Exception as e:
                print(f"{url}: Error - {e}")
```

## Error Handling

```python
async def robust_fetch(client, url, retries=3):
    for attempt in range(retries):
        try:
            return await client.get(url, timeout=10.0)
        except httpx.TimeoutException:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
        except httpx.HTTPStatusError as e:
            if e.response.status_code >= 500:
                await asyncio.sleep(2 ** attempt)
                continue
            raise
```

## Performance Tips

1. **Reuse AsyncClient** - Create once, use for all requests
2. **Use Semaphore** - Limit concurrent connections
3. **Handle timeouts** - Prevent hanging requests
4. **Exponential backoff** - For retries
5. **Connection pooling** - httpx handles automatically