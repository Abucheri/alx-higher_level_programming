#!/usr/bin/python3

"""Defines a Square Class."""


class Square:
    """The Square Class."""

    def __init__(self, size=0):
        """Instantiantes a new Square instance.

        Args:
            size (int, optional): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            float or int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value validation.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns current area.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of this square is less than."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of this square is less than or equal to."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of this square is greater than."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of this square is greater than or equal to."""
        return self.area() >= other.area()

    def __str__(self):
        """Return a string representation of the square."""
        return "Square({})".format(self.__size)
