#!/usr/bin/python3

"""Definition of Square class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates a new Square object.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns size of square.

        Returns:
            int: size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square with type and value validation.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: Postition of square as a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with type and value validation.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple/doesn'ttwo positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of two \
                    positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of square.

        Returns:
            int: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters using position."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square."""
        result = []
        if self.__size == 0:
            return ""
        for i in range(self.__position[1]):
            result.append("")
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)
