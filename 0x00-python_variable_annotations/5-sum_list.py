#!/usr/bin/env python3
""" 5-sum_list.py """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list which takes a list
    input_list of floats as argument and returns their
    sum as a float.
    """
    sum_float: float = 0.
    for x in input_list:
        sum_float += x
    return sum_float
