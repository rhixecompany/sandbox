#!/usr/bin/env python3
"""
Benchmark async vs sync HTTP requests.
"""

import asyncio
import time
import httpx
import requests

URLS = [f"https://httpbin.org/delay/1" for _ in range(10)]

async def async_fetch_all(urls):
    async with httpx.AsyncClient(timeout=30.0) as client:
        async def fetch(url):
            response = await client.get(url)
            return response.status_code
        
        return await asyncio.gather(*[fetch(url) for url in urls])

def sync_fetch_all(urls):
    results = []
    for url in urls:
        response = requests.get(url, timeout=30)
        results.append(response.status_code)
    return results

async def main():
    print("Benchmarking async vs sync HTTP requests...")
    print(f"Fetching {len(URLS)} URLs with 1s delay each\n")
    
    # Async benchmark
    start = time.perf_counter()
    await async_fetch_all(URLS)
    async_time = time.perf_counter() - start
    print(f"Async (gather): {async_time:.2f}s")
    
    # Sync benchmark
    start = time.perf_counter()
    sync_fetch_all(URLS)
    sync_time = time.perf_counter() - start
    print(f"Sync (sequential): {sync_time:.2f}s")
    
    print(f"\nSpeedup: {sync_time/async_time:.1f}x faster with async")
    print(f"Async should be ~{len(URLS)}x faster for I/O-bound work")

if __name__ == "__main__":
    asyncio.run(main())