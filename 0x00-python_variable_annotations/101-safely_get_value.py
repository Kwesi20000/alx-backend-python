#!/usr/bin/env python3
"""This module contains a function to safely get a value from a dictionary."""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Returns:
        Union[Any, T]: value for the key in the mapping,
        or the default value if the key is not in the mapping
    """
    if key in dct:
        return dct[key]
    else:
        return default
