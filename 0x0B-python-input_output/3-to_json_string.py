#!/usr/bin/python3
import json

"""Definition for to_json_string function."""


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj (any): The object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
