#!/usr/bin/python3
"""
this module contain one function, add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """Return the addition of a and b."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) in [float]:
        a = int(a)
    if type(b) in [float]:
        b = int(b)
    return (a + b)
