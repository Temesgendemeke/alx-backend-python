#!/usr/bin/env python3
"""_summary_"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier"""
    def multi(m: float) -> float:
        """returns mulitple of given argument"""
        return m * m
    return multi
