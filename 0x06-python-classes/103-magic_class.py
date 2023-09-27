#!/usr/bin/python3

"""Defining the MagicClass"""

import math


class MagicClass:
    """The Magic Class for finnding srea and circumference."""

    def __init__(self, radius=0):
        """Instantiates a MagicClass instance.

        Args:
            radius (int or float): The radius.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area.

        Return:
            int or float: The area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference.

        Returns:
            int or float: The circumference.
        """
        return 2 * math.pi * self.__radius
