#!/usr/bin/env python3
""" 102-type_checking.py """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    This function takes a tuple and a zoom factor, and returns a new list
        with the elements of the tuple repeated according to the zoom factor.

    Parameters:
    lst (Tuple): The tuple to zoom in on.
    factor (int): The zoom factor, which determines how many times each
        element of the tuple should be repeated in the output list.

    Returns:
    List: A new list with the elements of the tuple repeated according to
        the zoom factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_2x)
