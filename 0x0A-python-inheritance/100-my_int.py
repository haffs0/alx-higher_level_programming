#!/usr/bin/python3
"""
This 100-my_int module has one class inherit from int
"""


class MyInt(int):
    """MyInt inherit from int class"""
    def __eq__(self, value):
        """Override == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
