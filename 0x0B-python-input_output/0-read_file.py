#!/usr/bin/python3
"""
This 0-read_file module has one function, read_file(filename="")
"""


def read_file(filename=""):
    """Read a file"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
