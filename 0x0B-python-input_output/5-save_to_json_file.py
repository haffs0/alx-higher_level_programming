#!/usr/bin/python3
"""
This 5-save_to_json_file module has one function,
"""

import json


def save_to_json_file(my_obj, filename):
    """save to Json file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
