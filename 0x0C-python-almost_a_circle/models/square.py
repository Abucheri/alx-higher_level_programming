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

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, which is equal to both width and height

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not within the allowed range
            (same as width and height in Rectangle).
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a custom string representation of the Square instance.

        Returns:
            str: A string in the format '[Square] (<id>) <x>/<y> - <size>'.
        """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance.

        Args:
            *args: The list of arguments (no-keyworded arguments).
            Order is important.
                1st argument should be the id attribute.
                2nd argument should be the size attribute.
                3rd argument should be the x attribute.
                4th argument should be the y attribute.
            **kwargs: The dictionary of keyworded arguments.
            Each key represents an attribute.

        Notes:
            **kwargs are only processed if *args is empty or doesn't exist.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the attributes of the Square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
