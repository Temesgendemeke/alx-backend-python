#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """_summary_

    Args:
        dct (Mapping): _description_
        key (Any): _description_
        default (Union[T, None]): _description_

    Returns:
        Union[Any, T]: _description_
    """
    if key in dct:
        return dct[key]
    else:
        return default
