#!/usr/bin/python3

"""Definition of the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class, which inherits from the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.

    Raises:
        TypeError: If width, height, x, or y is not an integer.
        ValueError: If width, height, x, or y isn't within the allowed range.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the Rectangle class

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            Default is 0.
            y (int, optional): The y-coordinate of the rectangle's position.
            Default is 0.
            id (int, optional): The unique identifier for the instance.
            If not provided, it will be automatically assigned based on the
            current number of objects created (__nb_objects)

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, height, x, or y isn't within the
            allowed range.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is not within the allowed range.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is not within the allowed range.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The x-coordinate.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is not within the allowed range.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The y-coordinate.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is not within the allowed range.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle instance.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance using the character # to represent it.
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for _ in range(self.__y):
            print("")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a custom string representation of the Rectangle instance.

        Returns:
            str: A string in the format
            '[Rectangle] (<id>) <x>/<y> - <width>/<height>'.
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Assign arguments to the attributes in the specified order.

        Args:
            *args (int): The arguments to assign in the order
            id, width, height, x, y.
            **kwargs: Key-worded arguments where each key represents
            an attribute.

        Notes:
            **kwargs is skipped if *args is not empty.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary containing the attributes of the Rectangle.
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
