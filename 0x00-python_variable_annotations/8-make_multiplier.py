#!/usr/bin/env python3
"""_summary_"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier"""
    def multi(multiplier):
        """returns mulitple of given argument"""
        return multiplier * multiplier
    return multi
