#!usr/bin/env python3
"""
Async Comprehension task 2
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Comprehension task 2"""
    tasks = [async_comprehension(), async_comprehension(),
             async_comprehension(), async_comprehension()]
    start = time.time()
    await asyncio.gather(*tasks)
    return time.time() - start
