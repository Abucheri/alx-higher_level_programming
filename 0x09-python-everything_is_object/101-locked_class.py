#!/usr/bin/python3

"""This is the LockedClass class definition."""


class LockedClass:
    """Allows only 'first_name' as a dynamically created instance attribute.

    Attributes:
        first_name (str): Allowed instance attribute for the first name.
    """
    __slots__ = ['first_name']
