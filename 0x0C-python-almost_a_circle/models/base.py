#!/usr/bin/python3

"""Definition of the Base class."""
import json


class Base:
    """This is the Base class for managing unique identifiers
    (ids) in the project.

    Attributes:
        __nb_objects (int): A private class attribute that tracks the number
        of instances created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class.

        Args:
            id (int, optional): The unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries
            to convert to JSON.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
