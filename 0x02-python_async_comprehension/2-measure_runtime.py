#!/usr/bin/env python3
"""
This script imports async_comprehension from a previous file
and defines a measure_runtime coroutine. It executes async_comprehension
four times in parallel using asyncio.gather and measures the runtime.
"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns the runtime of async_comprehension in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
