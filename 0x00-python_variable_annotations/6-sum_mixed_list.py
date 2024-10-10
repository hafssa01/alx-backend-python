#!/usr/bin/env python3
"""
This module defines a function that takes a list of floats and integers and
returns their sum as a float.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of elements of mxd_lst as a float."""
    return float(sum(mxd_lst))
