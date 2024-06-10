#!/usr/bin/env python3
"""_summary"""


import random
import asyncio


async def wait_random(max_delay=10):
    """_summary_

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        _type_: _description_
    """
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)