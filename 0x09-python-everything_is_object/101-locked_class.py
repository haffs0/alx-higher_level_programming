#!/usr/bin/python3
"""
THis 101-locked_class module has one class, LockedClass
"""


class LockedClass:
    """prevent user from adding additional variables"""
    

    _slots__ = ["first_name"]
