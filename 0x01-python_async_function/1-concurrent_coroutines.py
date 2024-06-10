#!/usr/bin/env python3
"""_summary_"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function that return sorted list from async function

    Args:
        n (int): number of itreation
        max_delay (int): time of delay

    Returns:
        float: sorted list of float
    """
    delay_list = []
    for i in range(n):
        delay_list.append(wait_random(max_delay))
    return sorted(await asyncio.gather(*delay_list))
