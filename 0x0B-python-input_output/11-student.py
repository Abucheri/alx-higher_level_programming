#!/usr/bin/python3

"""Student class definition."""


class Student:
    """Defines a student by first_name, last_name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve
            (default is None).

        Returns:
            dict: A dictionary containing the specified attributes
            and their values.
        """
        if attrs is None:
            return self.__dict__
        return ({attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)})

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary with attribute names as keys and values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
