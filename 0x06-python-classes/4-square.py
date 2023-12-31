#!/usr/bin/python3

"""Defining the Square Class."""


class Square:
    """The Square Class."""

    def __init__(self, size=0):
        """Initializes a new instance.

        Args:
            size (int, optional): The size of the square (default is 0).

        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the value of the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size attribute with type and value validation

        Args:
            value (int): The new size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
