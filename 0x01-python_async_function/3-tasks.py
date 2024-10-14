#!/usr/bin/env python3
""" 3-tasks.py """
import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    takes an integer max_delay and returns a asyncio.Task.
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
