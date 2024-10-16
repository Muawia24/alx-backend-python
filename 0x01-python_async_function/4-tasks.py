#!/usr/bin/env python3
""" 4-tasks.py """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values)

    The code is nearly identical to wait_n except
    task_wait_random is being called.
    """
    delays_list = [await task_wait_random(max_delay) for i in range(n)]

    return sorted(delays_list)
