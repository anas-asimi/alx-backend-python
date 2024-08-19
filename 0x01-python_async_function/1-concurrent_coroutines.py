#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
from random import random
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> float:
    """
    wait_n
    Args:
        max_delay (int): _description_
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
