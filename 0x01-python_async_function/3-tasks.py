#!/usr/bin/env python3
"""contains task_wait_random function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates a asyncio task

        Args:
            max_delay(int): max delay time

        Return: an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
