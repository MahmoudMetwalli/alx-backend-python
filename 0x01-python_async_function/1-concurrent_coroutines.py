#!/usr/bin/env python3
'''
the wait_n coroutine
'''
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spams wait_random"""
    list_of_floats = []
    for i in range(0, n):
        list_of_floats.append(await wait_random(max_delay))
    return list_of_floats.sort()
