#!/usr/bin/python3
"""
THis 4-inherits_from module has one function, inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Return True or False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
