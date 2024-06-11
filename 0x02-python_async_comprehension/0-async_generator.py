#!/usr/bin/env python3
"""async_generator"""
import random
import asyncio


async def async_generator():
    """async_generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
