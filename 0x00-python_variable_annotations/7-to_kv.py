#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
"""


import typing


def to_kv(k: str, v: typing.Union(int, float)) -> tuple:
    """_summary_

    Args:
        k (str): _description_
        v (typing.Union): _description_

    Returns:
        tuple: _description_
    """
    return (k, float(v))
