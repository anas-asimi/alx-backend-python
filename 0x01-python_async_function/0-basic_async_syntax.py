#!/usr/bin/env python3
"""
0-basic_async_syntax.py
"""
from random import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random
    Args:
        max_delay (int): _description_
    """
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay
