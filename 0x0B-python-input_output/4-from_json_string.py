#!/usr/bin/python3

"""Definition for from_json_string function."""
import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the JSON string
    """
    return json.loads(my_str)
