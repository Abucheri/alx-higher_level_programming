#!/usr/bin/python3

"""Definition of append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to insert after each found line.

    Returns:
        None
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
