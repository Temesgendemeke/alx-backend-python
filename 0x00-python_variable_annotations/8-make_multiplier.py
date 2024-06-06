#!/usr/bin/env python3
"""_summary_"""


def make_multiplier(multiplier: float) -> float:
    """make multiplier"""
    def multi(multiplier):
        """returns mulitple of given argument"""
        return multiplier * multiplier
    return multi
