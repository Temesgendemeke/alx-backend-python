#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
"""


from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_summary_"""
    return [(i, len(i)) for i in lst]
