#!/usr/bin/env python3
"""Wait_random function"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Performs a simple asynchronous function"""
    wait_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
