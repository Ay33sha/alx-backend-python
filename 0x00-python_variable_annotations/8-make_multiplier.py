#!/usr/bin/env python3
"""contains the make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """defines a returns a multipler function

        Args:
            multiplier(float): any floating number

        Return: a function that returns the multiple fo the number passed"""
    def multiply(num: float) -> float:
        """multiply a number by multiplier

            Args:
                num(float): any floating number

            Return: num * multiplier(the parent function param)
        """
        return multiplier * num
    return multiply
