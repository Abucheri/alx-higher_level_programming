#!/usr/bin/python3

"""Function definition for reading a file."""


def read_file(filename=""):
    """Read and print the contents of a text file to stdout.

    Args:
        filename (str): The name of the text file to read
        (default is an empty string).
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
