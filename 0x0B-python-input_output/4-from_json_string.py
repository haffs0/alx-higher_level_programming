#!/usr/bin/python3
"""
This 4-from_json_string module has one function, from_json_string(my_str)
"""

import json


def from_json_string(my_str):
    """Json string"""
    return json.loads(my_str)
