#!/usr/bin/env python3
"""Element length function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
