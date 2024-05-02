#!/usr/bin/env python3
"""This module contains a function to create a tuple with a string
and the square of an int or float."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with a string and the square of an int or float."""
    return (k, float(v**2))
