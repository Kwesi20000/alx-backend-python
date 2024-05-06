#!/usr/bin/env python3

import asyncio
import random
from typing import Optional


async def wait_random(max_delay: Optional[int] = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds (inclusive).
    
    Args:
        max_delay (int, optional): Maximum delay in seconds (inclusive). Defaults to 10.
    
    Returns:
        float: Random delay between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
