#!/usr/bin/python3
"""
This 6-load_from_json_file module has one function,
"""

import json


def load_from_json_file(filename):
    """load from Json file"""
    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)
