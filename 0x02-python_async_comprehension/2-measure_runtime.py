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
    start_time: float = time.perf_counter()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            )

    return time.perf_counter() - start_time
