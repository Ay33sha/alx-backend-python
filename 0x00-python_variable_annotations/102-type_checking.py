#!/usr/bin/env python3
"""contains the zoom_array function"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """zooms a tuple to an array

        Arg:
            lst(tuple): any tuple
            factor(int): any integer
        Retrun: a list with the factor number of tuples
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
