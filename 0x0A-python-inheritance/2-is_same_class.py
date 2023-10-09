#!/usr/bin/python3

"""Definition to confirm instance membership."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
