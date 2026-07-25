#!/usr/bin/env python3
"""
Reusable async HTTP client with semaphore-based concurrency limiting.
"""

import asyncio
import httpx
from typing import Optional

class AsyncAPIClient:
    def __init__(self, base_url: str, max_concurrent: int = 10, timeout: float = 30.0):
        self.base_url = base_url
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.timeout = httpx.Timeout(timeout)
        self.client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self.client = httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.aclose()

    async def get(self, path: str, params: dict = None) -> httpx.Response:
        async with self.semaphore:
            response = await self.client.get(path, params=params)
            response.raise_for_status()
            return response

    async def post(self, path: str, json: dict = None) -> httpx.Response:
        async with self.semaphore:
            response = await self.client.post(path, json=json)
            response.raise_for_status()
            return response