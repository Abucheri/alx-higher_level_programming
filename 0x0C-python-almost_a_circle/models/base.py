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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of a list of
        instances to a file.

        Args:
            cls (class): The class of the instances in list_objs.
            list_objs (list): A list of instances to convert
            to JSON and save to a file.

        Note:
            The filename must be: <Class name>.json - example: Rectangle.json.
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to convert.

        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance with attributes from a dictionary.

        Args:
            cls (class): The class to create an instance of.
            dictionary (dict): A dictionary containing attribute values.

        Returns:
            obj: A new instance of the class with attributes
            from the dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances.

        Args:
            cls (class): The class for which to load instances.

        Returns:
            list: A list of instances loaded from the JSON file
        """
        filename = cls.__name__.lower() + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                if not json_data:
                    return []
                dictionaries = cls.from_json_string(json_data)
                instances = ([cls.create(**dictionary)
                             for dictionary in dictionaries])
                return instances
        except FileNotFoundError:
            return []
