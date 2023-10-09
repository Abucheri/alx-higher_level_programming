#!/usr/bin/python3

"""Class definition that inherits from the list module."""


class MyList(list):
    """Custom list class that inherits built-in list class."""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))
