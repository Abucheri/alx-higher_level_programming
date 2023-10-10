#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Rectangle class definition."""


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
