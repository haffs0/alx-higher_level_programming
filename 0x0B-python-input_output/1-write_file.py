#!/usr/bin/python3
"""
This 1-write_file module has one function, write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """Read a file"""
    with open(filename, 'r+') as f:
        return f.write(text)
