#!/usr/bin/env python3
'''
A test file for printing the correct output of the wait_n coroutine
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Fuction returns average time taken per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
