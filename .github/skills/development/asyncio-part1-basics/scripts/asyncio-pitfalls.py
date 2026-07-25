#!/usr/bin/env python3
"""
Common asyncio pitfalls and how to fix them.
"""

import asyncio
import sys

# Pitfall 1: Blocking the event loop
async def pitfall_blocking():
    print("❌ BAD: time.sleep() blocks event loop")
    import time
    # time.sleep(1)  # BLOCKS - don't do this
    
    print("✅ GOOD: asyncio.sleep() yields control")
    await asyncio.sleep(1)

# Pitfall 2: Not awaiting coroutines
async def pitfall_not_awaiting():
    print("❌ BAD: calling coroutine without await creates dangling coroutine")
    # This creates a coroutine object but doesn't run it
    coro = my_helper()
    print(f"   Dangling coroutine: {coro!r}")
    
    print("✅ GOOD: always await coroutines")
    await my_helper()

async def my_helper():
    return 42

# Pitfall 3: Forgetting to close resources
async def pitfall_resources():
    print("✅ GOOD: use async with for resource cleanup")
    # Create a mock context manager
    class AsyncResource:
        async def __aenter__(self):
            print("   Resource opened")
            return self
        async def __aexit__(self, *args):
            print("   Resource closed")
    
    async with AsyncResource():
        print("   Using resource...")

# Pitfall 4: Running sync code in async
def sync_http_call():
    """This blocks the event loop."""
    import urllib.request
    return urllib.request.urlopen("https://httpbin.org/delay/1").read()

async def async_http_call():
    """This does not block the event loop."""
    import httpx
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/delay/1")
        return response.content

if __name__ == "__main__":
    async def main():
        await pitfall_blocking()
        await pitfall_not_awaiting()
        await pitfall_resources()
        print("\n✅ All pitfalls demonstrated")
    
    asyncio.run(main())