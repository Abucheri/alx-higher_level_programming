#!/usr/bin/python3

"""This module defines the print_square function."""


def print_square(size):
    """Prints a square made of # x-ters with a specified size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if it's a float.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
