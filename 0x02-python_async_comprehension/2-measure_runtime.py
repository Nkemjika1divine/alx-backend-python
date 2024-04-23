#!/usr/bin/env python3
"""Measure runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes 4 async_comprehension methods concurrently
    Return the time taken
    """
    start = time.time()
    # Run 4 Async comprehensions concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop = time.time()
    return stop - start
