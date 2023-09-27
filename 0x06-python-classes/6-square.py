#!/usr/bin/python3

"""Defining a Square class"""


class Square:
    """The Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square.
            position (int, int): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves value of size attribute

        Returns:
            int: Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value of size attribute with type and value validation.

        Args:
            value (int): New size value to set

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves value position attribute.

        Returns:
            tuple: Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets value of position attribute with type and value validation.

        Args:
            value (int): New position value to set

        Raises:
            TypeError: If value is not a tuple of 2 +ve integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(val, int) and val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns current square area

        Returns:
            int: Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the x-ter #.
        Use the position attribute to adjust the position of the square.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
