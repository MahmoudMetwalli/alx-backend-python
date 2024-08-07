#!/usr/bin/env python3
"""
Async Comprehension task 0
"""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[int, None, None]:
    """Comprehension"""
    for i in range(10):
        yield random.uniform(1, 10)
        await asyncio.sleep(1)
