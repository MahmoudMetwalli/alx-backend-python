#!/usr/bin/env python3
"""
Async comprehension task 1
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """Comprehension task 1"""
    return [num async for num in async_generator()]
