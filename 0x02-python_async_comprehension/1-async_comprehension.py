#!/usr/bin/env python3
"""contains the coroutine `async_comprehension`"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async
        comprehension over async_generator

        Return: the 10 random number
    """
    return [num async for num in async_generator()]
