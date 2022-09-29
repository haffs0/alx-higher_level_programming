#!/usr/bin/python3
"""
This is rectangle module has one class Rectangle that inherit from Base
"""


class Rectangle(Base):
    """Initialized data"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return the value of width"""
        return self.__width
