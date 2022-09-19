#!/usr/bin/python3
"""
The 4-print_square.py module supplies one function, print_square(size).
"""


def print_square(size):
    """Return a square share"""
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) in [float] and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("{}".format("#"*size))
