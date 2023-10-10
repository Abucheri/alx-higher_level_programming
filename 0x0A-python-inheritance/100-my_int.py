#!/usr/bin/python3

"""Integer class definition."""


class MyInt(int):
    """A class representing an integer with inverted equality operators."""

    def __eq__(self, other):
        """Override the equality operator (==) to be inverted."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=) to be inverted."""
        return super().__eq__(other)
