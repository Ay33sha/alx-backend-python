#!/usr/bin/env python3
"""contains the function/coroutine task_wait_n"""
import asyncio
from typing import TYPE_CHECKING, List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawns task_wait_random n times with the specified max_delay

        Args:
            n(int): number of times wait_randoms should be spawned
            max_delay(int): max_delay of wait_random

        Return: the list of all delays(float values) ina ascending
            order with sort()
    """
    # lst = [await wait_random(max_delay) for i in range(n)]
    lst = await asyncio.gather(
            *(task_wait_random(max_delay) for i in range(n))
            )
    return sorted(lst)
