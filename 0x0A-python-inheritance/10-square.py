#!/usr/bin/python3
"""
This 10-square module has one class and inherit from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initialized data"""
    def __init__(self, size):
        """initial variables"""
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate area of a square"""
        return (self.__size ** 2)
