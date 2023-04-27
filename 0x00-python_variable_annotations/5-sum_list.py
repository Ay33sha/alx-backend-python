#!/usr/bin/env python3
"""contains the function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sums the elements in a list

        Args:
            input_list(list(float)): list of floating numbers

        Return: the sum of the elements in input_list
    """
    list_sum = 0.0
    for num in input_list:
        list_sum += num
    return list_sum
