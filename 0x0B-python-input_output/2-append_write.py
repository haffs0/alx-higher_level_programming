#!/usr/bin/python3
"""
This 2-append_write module has one function, append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """Read a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
