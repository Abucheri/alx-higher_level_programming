#!/usr/bin/python3

"""Class definition for Student."""


class Student:
    """Defines a student by first_name, last_name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
