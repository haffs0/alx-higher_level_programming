#!/usr/bin/python3
"""
This add_attribute module has one function, add_attribute(obj, key, value)
"""


def add_attribute(obj, key, value):
    """add new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribte")

    setattr(obj, key, value)
