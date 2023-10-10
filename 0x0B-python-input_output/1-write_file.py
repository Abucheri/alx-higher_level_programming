#!/usr/bin/python3

"""Definition for write_file function."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and
    return the number of characters written.

    Args:
        filename (str): The name of the text file to write to
        (default is an empty string).
        text (str): The string to write to the file
        (default is an empty string).

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
