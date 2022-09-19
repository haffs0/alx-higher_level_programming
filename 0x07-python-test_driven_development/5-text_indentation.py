#!/usr/bin/python3
"""
This 5-text_indentation module has only one function, text_indentation(text)
"""


def text_indentation(text):
    """Print text after encounter with .,?and: with newline"""
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    new_string = ""
    for char in text:
        if char in [".", "'", "?", ":"]:
            new_string += char
            print(new_string.strip())
            print()
            print()
            new_string = ""
        else:
            new_string += char
