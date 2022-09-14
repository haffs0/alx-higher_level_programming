#!/usr/bin/python3
"""A square class with private attribute instance"""


class Square:
    """creates a square class object."""

    def __init__(self, size=0):
        """Initialize the data."""
        self.__size = size

    @property
    def size(self):
        """get the value of private variable size"""
        return self.__size

    @size.setter
    def size(self, value):
        """change the value of size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of a square"""
        return (self.__size ** 2)

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __eq__(self, other):
        """equal to """
        return self.area() == other.area()

    def __le__(self, other):
        """less than or equal"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater or equal"""
        return self.area() >= other.area()

    def __ne__(self, other):
        """noot equal"""
        return self.area() != other.area()
