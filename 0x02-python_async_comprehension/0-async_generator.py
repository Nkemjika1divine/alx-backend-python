#!/usr/bin/env python3
"""Asynchronous generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator
    Yields a number between 0 and 10 after waiting for 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        number = random.random() * 10
        yield number
