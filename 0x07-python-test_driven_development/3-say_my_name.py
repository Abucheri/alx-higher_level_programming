#!/usr/bin/python3

"""This module defines a say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Prints a message in the format "My name is <first name> <last name>".

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name, defaults to an empty string.

    Raises:
        TypeError: If first name isn't a string.
        TypeError: If last name isn't a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
