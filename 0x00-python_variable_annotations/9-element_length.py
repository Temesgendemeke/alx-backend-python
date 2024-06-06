#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
"""


from typing import Sequence, Tuple


def element_length(lst: int) -> int:
    """_summary_"""
    return [(i, len(i)) for i in lst]
