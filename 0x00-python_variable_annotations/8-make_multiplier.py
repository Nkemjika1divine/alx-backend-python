#!/usr/bin/env python3
"""Returns a function that multiplies a float by a number""" 
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a multiplier"""
    func: Callable[[float], float] = lambda value: value * multiplier
    return func
