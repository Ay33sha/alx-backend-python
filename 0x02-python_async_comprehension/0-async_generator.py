#!/usr/bin/env python3
"""contains a coroutine async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Description: loops 10 times
            yields a random number bewteen 0 and 10
            then waits asynchronously for a second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
