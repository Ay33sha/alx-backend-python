#!/usr/bin/env python3
"""contains the sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums a list with both float and integer numbers
        Args:
            mxd_lst(list): list that contains integer and or float
        Return: floating sum of the numbers in mxd_lst"""
    lst_sum = 0.0
    for num in mxd_lst:
        lst_sum += num

    return lst_sum
