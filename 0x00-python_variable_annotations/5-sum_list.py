#!/usr/bin/env python3
"""
5-sum_list.py
"""


def sum_list(input_list: list[float]) -> float:
    """_summary_

    Args:
        input_list (list[float]): _description_

    Returns:
        float: _description_
    """
    n: float = 0
    for x in input_list:
        n += x
    return n
