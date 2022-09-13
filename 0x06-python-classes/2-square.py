#!/usr/bin/python3
"""A square class with private attribute instance"""


class Square:
    """creates a square class object."""

    def __init__(self, size=0):
        """Initializes the data."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
