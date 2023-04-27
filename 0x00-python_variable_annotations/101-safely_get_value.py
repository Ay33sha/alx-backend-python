#!/usr/bin/env python3
"""contains the safely_get_value"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """safely get a value from a dictionary(works more like dict get method)

        Args:
            dct(dict): a dictionary
            key(any type): any type
            default(generic T|None): default value to return if key not in dct

        Return: value in dct or default if the key not in dct
    """
    if key in dct:
        return dct[key]
    else:
        return default
