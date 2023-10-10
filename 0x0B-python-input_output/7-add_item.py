#!/usr/bin/python3

"""Add args to a Python lists and save to file."""
import sys
from os.path import isfile
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_args_to_list(filename, *args):
    """Add arguments to a JSON list and save to a file.

    This function takes a filename and a variable number of
    arguments (strings) and appends them to a JSON list stored in a file.
    If the file doesn't exist, it will be created.

    Args:
        filename (str): The name of the JSON file
        to read and save the JSON list.
        *args (str): Variable number of string
        arguments to add to the JSON list.

    Returns:
        None
    """
    if isfile(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    filename = "add_item.json"
    args = sys.argv[1:]
    add_args_to_list(filename, *args)
