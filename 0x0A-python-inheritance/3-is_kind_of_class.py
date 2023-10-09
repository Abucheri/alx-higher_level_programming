#!/usr/bin/python3

"""Definition to check for instance membership."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Returns:
        True if obj is an instance of a_class or its subclasses,
        False otherwise.
    """
    return isinstance(obj, a_class)
