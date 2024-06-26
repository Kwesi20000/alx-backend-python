#!/usr/bin/env python3
"""
A module for zooming in on a tuple
"""
from typing import List, Tuple, Optional


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple:
    zoomed_in: Tuple = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)  # Make the input list a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Use an integer for the factor
