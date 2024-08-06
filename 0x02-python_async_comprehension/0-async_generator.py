#!/usr/bin/env python3
"""
Async Comprehension task 0
"""
import asyncio
import random


async def async_generator():
    """Comprehension"""
    for i in range(10):
        yield random.uniform(1, 10)
        await asyncio.sleep(1)
