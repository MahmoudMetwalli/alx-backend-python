#!/usr/bin/env python3
"""
Measuring runtimes
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures elapsed time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.time() - start
    return elapsed / n
