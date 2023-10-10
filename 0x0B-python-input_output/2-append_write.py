#!/usr/bin/python3

"""Definition for append_write function."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF-8) and
    return the number of characters added.

    Args:
        filename (str): The name of the text file to append to
        (default is an empty string).
        text (str): The string to append to the file
        (default is an empty string).

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
