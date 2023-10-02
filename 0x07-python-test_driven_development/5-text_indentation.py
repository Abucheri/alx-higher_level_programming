#!/usr/bin/python3

"""This module defines the text_indentation function."""


def text_indentation(text):
    """Prints input text with two new lines after each of ".", "?" and ":".

    Args:
        text (str): Input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1
    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
