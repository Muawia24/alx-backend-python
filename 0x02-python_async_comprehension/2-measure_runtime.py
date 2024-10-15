#!/usr/bin/env python3
"""" 2-measure_runtime.py """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel
    using 'asyncio.gather'.
    measures the total runtime and return it.
    """
    start_time = time.perf_counter()

    t1 = asyncio.create_task(async_comprehension())
    t2 = asyncio.create_task(async_comprehension())
    t3 = asyncio.create_task(async_comprehension())
    t4 = asyncio.create_task(async_comprehension())

    await asyncio.gather(t1, t2, t3, t4)

    total_time = time.perf_counter() - start_time

    return total_time
