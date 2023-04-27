#!/usr/bin/env python3
"""contains to_kv function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """is a to key value stored in a tuple

        Args:
            v(int|float): any floating number
            k(str): a string describing v
        Return: a tuple with the k and value
    """
    return (k, v * v)
