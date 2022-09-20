#!/usr/bin/python3
"""Unittest for max_integer([...])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [4, 5, 6, 7]
        self.assertEqual(max_integer(ordered), 7)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [4, 3, 9, 8]
        self.assertEqual(max_integer(unordered), 9)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_string(self):
        """Test a string."""
        string = "haffs"
        self.assertEqual(max_integer(string), 's')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["haffs", "is", "my", "nickname"]
        self.assertEqual(max_integer(strings), "nickname")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
