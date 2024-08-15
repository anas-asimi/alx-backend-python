#!/usr/bin/env python3
"""
6-sum_mixed_list.py
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_summary_

    Args:
        mxd_lst (list[int, float]): _description_

    Returns:
        float: _description_
    """
    n: float = 0
    for x in mxd_lst:
        n += x
    return n
