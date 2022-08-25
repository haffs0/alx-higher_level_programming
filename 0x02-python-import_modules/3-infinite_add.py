#!/usr/bin/python3

import sys

argvs = sys.argv[1:]
total = 0
if __name__ == "__main__":
    if len(argvs) >= 1:

        for argv in argvs:
            total += int(argv)

        print(total)
    else:
        print(total)
