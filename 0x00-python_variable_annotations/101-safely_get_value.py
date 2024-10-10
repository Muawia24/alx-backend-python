#!/usr/bin/env python3
""" 101-safely_get_value.py """
from typing import TypeVar, Union, Any, Mapping


T = TypeVar('T')
auto = Union[T, None]
ret = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: auto = None) -> ret:
    """
    This function gets the value for a given key in a mapping, or returns
        a default value if the key is not in the mapping.

    Parameters:
    dct (Mapping): The mapping to get the value from.
    key (Any): The key to look up in the mapping.
    default (Union[T, None]): The default value to return if the key is not
        in the mapping.

    Returns:
    Union[Any, T]: The value for the key in the mapping, or the default
        value if the key is not in the mapping.
    """
    if key in dct:
        return dct[key]
    else:
        return default
