#!/usr/bin/python3

"""This module defines the add_integer function for adding 2 integers"""


def add_integer(a, b=98):
    """Add 2 integers or floats.

    Args:
        a (int or float): First input.
        b (int or float): Secong input.

    Returns:
        int: Sum of a and b as an integer.

    Raises:
        TypeError: If a or b isn't an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
