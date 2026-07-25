# AsyncIO API Patterns

## aiohttp Client Session

```python
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()
```

## httpx AsyncClient

```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.get(url)
    data = response.json()
```

## asyncpg Connection Pool

```python
import asyncpg

pool = await asyncpg.create_pool(dsn)
async with pool.acquire() as conn:
    rows = await conn.fetch("SELECT * FROM users")
```