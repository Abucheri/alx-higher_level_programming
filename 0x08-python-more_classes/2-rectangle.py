#!/usr/bin/python3

"""This is a rectangle definition with area and perimeter."""


class Rectangle:
    """Defines a rectangle with width, height, area and perimeter."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            width (int): Width of the new rectangle (default os 0).
            height (int): Height of new rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of rectabgle.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: The area value.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of a rectangle.

        Returns:
            int: The perimeter value.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
