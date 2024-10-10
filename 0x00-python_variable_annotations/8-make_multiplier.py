#!/usr/bin/env python3
""" 8-make_multiplier.py """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a
    function that multiplies a float by multiplier.
    """
    def mult(multi: float) -> float:
        """
        function that multiplies a float by multiplier.
        """
        return multiplier * multi

    return mult
