#!/usr/bin/python3
"""
Post data using requests package
"""
import sys
import requests
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    res = requests.post(url, data=value)
    print(res.text)
