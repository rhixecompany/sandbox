#!/usr/bin/env python3
"""
Concurrency limiting with asyncio.Semaphore.
"""

import asyncio
from typing import List, Callable, Any

async def limited_gather(
    coroutines: List[Callable],
    max_concurrent: int,
    *args,
    **kwargs
) -> List[Any]:
    """
    Run coroutines with limited concurrency.
    
    Args:
        coroutines: List of coroutine functions to run
        max_concurrent: Maximum number of concurrent executions
        *args, **kwargs: Arguments passed to each coroutine
    
    Returns:
        List of results in same order as input coroutines
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def limited_coro(coro):
        async with semaphore:
            return await coro(*args, **kwargs)
    
    return await asyncio.gather(*[limited_coro(c) for c in coroutines])

# Alternative pattern using asyncio.as_completed for streaming results
async def limited_as_completed(
    coroutines: List[Callable],
    max_concurrent: int,
    *args,
    **kwargs
):
    """
    Run coroutines with limited concurrency, yield results as they complete.
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def limited_coro(coro):
        async with semaphore:
            return await coro(*args, **kwargs)
    
    tasks = [asyncio.create_task(limited_coro(c)) for c in coroutines]
    
    for task in asyncio.as_completed(tasks):
        yield await task