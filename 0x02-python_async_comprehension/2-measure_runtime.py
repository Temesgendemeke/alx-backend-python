#!/usr/bin/env python3
"""measure_runtime"""
import asyncio
from datetime import datetime
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measure_runtime"""
    start_time = datetime.now()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    elpased_time = (datetime.now() - start_time).total_seconds()
    return elpased_time
