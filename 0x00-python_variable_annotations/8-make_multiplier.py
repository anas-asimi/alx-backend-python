#!/usr/bin/env python3
"""
8-make_multiplier.py
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    def fun(x: float) -> float:
        return x * multiplier
    return fun
