#!/usr/bin/python3
"""
This 8-class_to_json module has one function, class_to_json(obj)
"""


def class_to_json(obj):
    """class to json"""
    return obj.__dict__
