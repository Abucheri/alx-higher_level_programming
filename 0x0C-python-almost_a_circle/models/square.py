#!/usr/bin/python3

"""Definition of the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class, which inherits from the Rectangle class.

    Attributes:
        size (int): The size of the square, which is equal to both
        width and height.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.

    Raises:
        TypeError: If size, x, or y is not an integer.
        ValueError: If size, x, or y is not within the allowed range.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of the Square class

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            Default is 0.
            y (int, optional): The y-coordinate of the square's position.
            Default is 0.
            id (int, optional): The unique identifier for the instance.
            If not provided, it will be automatically assigned based on the
            current number of objects created (__nb_objects).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a custom string representation of the Square instance.

        Returns:
            str: A string in the format '[Square] (<id>) <x>/<y> - <size>'.
        """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width
        )
