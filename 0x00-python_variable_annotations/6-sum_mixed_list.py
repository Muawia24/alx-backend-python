#!/usr/bin/env python3
""" 6-sum_mixed_list.py """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
     type-annotated function sum_mixed_list which takes a
     list mxd_lst of integers and floats and returns
     their sum as a float.
    """
    sum_float: float = 0.
    for x in mxd_list:
        sum_float += x
    return sum_float
