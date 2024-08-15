#!/usr/bin/env python3
"""
7-to_kv.py
"""


def to_kv(k: str, v: int | float) -> tuple[str, int]:
    """_summary_

    Args:
        k (str): _description_
        v (int | float): _description_

    Returns:
        tuple[str, int]: _description_
    """
    sqr: float = v**2
    return (k, sqr)
