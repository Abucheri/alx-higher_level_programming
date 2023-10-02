#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defining unittests for the max_integer([..]) function."""

    def test_positive_integers(self):
        """Testing for positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_mixed_integers(self):
        """Testing for mixed integer values"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Testing for empty parameter."""
        self.assertIsNone(max_integer([]))

    def test_negative_integers(self):
        """Testing for negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_ordered_list(self):
        """Testing for ordered lists."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Testing for unordered lists."""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_first_index(self):
        """Testing maximum value at first index."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_list_with_one_value(self):
        """Testing a list with one value."""
        self.assertEqual(max_integer([8]), 8)

    def test_float_value(self):
        """Testing for a float value."""
        self.assertEqual(max_integer([1.53, 9.7, -9.13, 15.2, 20.5]), 20.5)

    def test_mixed_number_values(self):
        """Testing for int and float values mixture."""
        self.assertEqual(max_integer([1.53, 97, -9, 15, 20.5]), 97)

    def test_for_string(self):
        """Testing for string values."""
        self.assertEqual(max_integer("Hello"), 'o')

    def test_list_of_strings(self):
        """Testing a list containing strings."""
        self.assertEqual(max_integer(["Hello", "World"]), "World")

    def test_empty_string_value(self):
        """Testing for an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == "__main__":
    unittest.main()
