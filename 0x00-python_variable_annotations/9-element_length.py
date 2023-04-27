#!/usr/bin/env python3
"""contains element_length function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """

        Args:
            lst(list): list containing iterables

        Return: list of tuples containing the element and len of the element
    """
    return [(i, len(i)) for i in lst]
