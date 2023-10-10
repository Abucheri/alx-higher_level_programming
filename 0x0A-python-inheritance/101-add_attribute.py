#!/usr/bin/python3

"""Function definition for adding attributes to an object."""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attr (str): The name of the attribute.
        value (any): The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
