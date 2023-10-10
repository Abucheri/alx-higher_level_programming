#!/usr/bin/python3

"""Definition for save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a text file.

    Args:
        my_obj (any): The object to be saved as JSON.
        filename (str): The name of the text file to write the
        JSON representation to.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
