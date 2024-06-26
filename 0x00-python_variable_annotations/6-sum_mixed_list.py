#!/usr/bin/env python3
"""This module contains a function to compute the sum of a
list of integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Compute the sum of a list of integers and floats and return it."""
    return sum(mxd_lst)
