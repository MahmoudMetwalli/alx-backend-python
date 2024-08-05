#!/usr/bin/env python3
'''
the wait_n coroutine
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spams wait_random"""
    list_of_floats = []
    for i in range(0, n):
        list_of_floats.append(await wait_random(max_delay))
    return sorted(list_of_floats)
