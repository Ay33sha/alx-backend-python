#!/usr/bin/env python3
"""contains measure_time function"""
import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for `wait_n`

        Args:
            n(int): number of time wait_n should be executed
            max_delay(int): max_delay

        Return: total_time/n as a float
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start_time
    return total_time/n
