#!/usr/bin/env python3
"""This module contains a function to compute the length of
elements in a list."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''This computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
