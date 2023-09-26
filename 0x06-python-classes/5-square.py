#!/usr/bin/python3

"""Defining a Square Class."""


class Square:
    """The Square class."""

    def __init__(self, size=0):
        """Initializes a new square instance

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the value of size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size attribute with type and value validation.

        Args:
            value (int): The new size value to set

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the x-ter #. If size is 0, print an empty line."""
        for x in range(0, self.__size):
            [print("#", end="") for a in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
