#!/usr/bin/python3
"""A square class with private attribute instance"""


class Square:
    """creates a square class object."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the data."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """get the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """change value of position"""
        if(type(value) is not tuple or len(value) is not 2 or
           type(value[0]) is not int or
           type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(value[0] < 0 or value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """print #"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.position[1]):
                print()
            for i in range(self.__size):
                print("{}".format(self.__position[0] * " "), end="")
                print(self.__size * "#")

    def __str__(self):
        """stdout"""
        if(self.size == 0):
            return ''
        newlines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = "#" * self.size
        return newlines + '\n'.join(spaces + hashes for x in range(self.size))
