#!/usr/bin/python3
"""
This MyList module contain one class MyList
"""


class MyList(list):
    """MyList inherit from list"""

    def print_sorted(self):
        """Print a list in ascending order"""
        print(sorted(self))
