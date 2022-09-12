#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        (a, b) = args
        result = fct(a, b)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return (result)
