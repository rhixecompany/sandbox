# Blocking vs Async Libraries Mapping

## HTTP Clients

| Blocking | Async Alternative |
|----------|-------------------|
| `requests` | `httpx`, `aiohttp` |
| `urllib` | `httpx`, `aiohttp` |

## Database

| Blocking | Async Alternative |
|----------|-------------------|
| `sqlite3` | `aiosqlite` |
| `psycopg2` | `asyncpg` |
| `pymongo` | `motor` |
| `redis-py` | `redis.asyncio` |

## File I/O

| Blocking | Async Alternative |
|----------|-------------------|
| `open()` | `aiofiles` |
| `pathlib` | `aiofiles` |

## Web Frameworks

| Blocking | Async Alternative |
|----------|-------------------|
| `Flask` | `FastAPI`, `Starlette`, `Quart` |
| `Django` | `Django Channels`, `Starlette` |
| `requests` | `httpx`, `aiohttp` |

## Testing

| Blocking | Async Alternative |
|----------|-------------------|
| `unittest` | `pytest-asyncio` |
| `requests-mock` | `pytest-asyncio` + `httpx` mock |

## Common Patterns

```python
# WRONG - blocks event loop
import requests
response = requests.get(url)

# CORRECT - async HTTP
import httpx
async with httpx.AsyncClient() as client:
    response = await client.get(url)

# WRONG - blocks event loop
import sqlite3
conn = sqlite3.connect("db.sqlite")
conn.execute("SELECT * FROM users")

# CORRECT - async DB
import aiosqlite
async with aiosqlite.connect("db.sqlite") as db:
    async with db.execute("SELECT * FROM users") as cursor:
        rows = await cursor.fetchall()

# WRONG - blocks event loop
with open("file.txt") as f:
    content = f.read()

# CORRECT - async file I/O
import aiofiles
async with aiofiles.open("file.txt") as f:
    content = await f.read()
```

## Migration Checklist

- [ ] Replace `requests` with `httpx` or `aiohttp`
- [ ] Replace `sqlite3` with `aiosqlite`
- [ ] Replace `psycopg2` with `asyncpg`
- [ ] Replace `redis` with `redis.asyncio`
- [ ] Replace file I/O with `aiofiles`
- [ ] Replace `time.sleep()` with `asyncio.sleep()`
- [ ] Replace `threading.Lock` with `asyncio.Lock`
- [ ] Replace `threading.Semaphore` with `asyncio.Semaphore`
- [ ] Add `pytest-asyncio` for testing
- [ ] Use `asyncio.run()` instead of manual loop management