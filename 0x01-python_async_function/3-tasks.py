#!/usr/bin/env python3
"""_summary_"""
import asyncio
from datetime import datetime

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """ retrun Task  object """
    return asyncio.Task(wait_random(max_delay))
