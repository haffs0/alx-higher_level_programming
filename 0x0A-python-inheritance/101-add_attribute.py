#!/usr/bin/python3
"""
This add_attribute module has one function, add_attribute(obj, key, value)
"""


def add_attribute(obj, key, value):
    """add new attribute"""
    try:
        setattr(obj, key, value)
    except (TypeError):
        print("can't add new attribute")
