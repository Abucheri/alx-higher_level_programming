#!/usr/bin/python3

"""Definition for class_to_json function."""


def class_to_json(obj):
    """Convert an instance of a class to a JSON-serializable dictionary.

    Args:
        obj (any): An instance of a class with serializable attributes
        (list, dictionary, string, integer, and boolean)

    Returns:
        dict: A dictionary describing the
        serializable attributes of the object.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
