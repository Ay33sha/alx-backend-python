#!/usr/bin/env python3
"""contains an asyncronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay seconds

        Args:
            max_delay(int): max_delay of the wait_random function
        Return: the number of seconds of delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
