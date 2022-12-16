#!/usr/bin/python3
"""
Fetch data using urllib package
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        req_id = response.headers["X-Request-Id"]
        print(req_id)
