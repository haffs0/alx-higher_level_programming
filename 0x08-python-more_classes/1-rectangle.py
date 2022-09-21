#!/usr/bin/python3
"""
THis 1-rectangle module has one class
"""


class Rectangle:
    """initialized data"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """change width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
