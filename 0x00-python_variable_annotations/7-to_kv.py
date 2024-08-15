#!/usr/bin/env python3
"""
7-to_kv.py
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, int]:
    """_summary_

    Args:
        k (str): _description_
        v (int | float): _description_

    Returns:
        tuple[str, int]: _description_
    """
    sqr: float = v**2
    return (k, sqr)
