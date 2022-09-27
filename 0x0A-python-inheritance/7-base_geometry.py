#!/usr/bin/python3
"""
This 7-base_geometry module has one class BaseGeometry
"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if value is integer"""
        if type(value) not in [int]:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
