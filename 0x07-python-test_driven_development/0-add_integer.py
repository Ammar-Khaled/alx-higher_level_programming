#!/usr/bin/python3
"""This module is to add two integers"""


def add_integer(a, b=98):
    """add two integers or float

    Args:
        a: first num
        b: second num

    Returns:
        the sum of the two numbers

    Raises:
        TypeError: if a, b arn not integers or float

    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)

    return a + b
