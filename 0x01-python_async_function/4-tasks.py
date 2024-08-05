#!/usr/bin/env python3
'''
the wait_n coroutine
'''
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spams wait_random"""
    list_of_floats = []
    for i in range(0, n):
        list_of_floats.append(await task_wait_random(max_delay))
    return sorted(list_of_floats)
