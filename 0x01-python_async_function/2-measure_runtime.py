#!/usr/bin/env python3
"""_summary_"""
import asyncio
from datetime import datetime

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = datetime.now()
    asyncio.run(wait_n(n, max_delay))
    total_time = datetime.now() - start_time
    return total_time.total_seconds() / n
