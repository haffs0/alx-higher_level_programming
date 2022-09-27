#!/usr/bin/python3
"""
This 8-rectangle module has one class and inherit from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """initialized data"""
    def __init__(self, width, height):
        """initial variables"""
        super().integer_validator('height', height)
        super().integer_validator('width', width)
        self.__height = height
        self.__width = width
