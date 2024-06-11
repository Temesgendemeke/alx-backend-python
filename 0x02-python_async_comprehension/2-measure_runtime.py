#!/usr/bin/env python3

import random
import asyncio

async def async_generator():
    lists = []
    for _ in range(10):
        asyncio.sleep(1)
        lists.append(random.randrange(0, 10))
    return lists