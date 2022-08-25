#!/usr/bin/python3

import sys

argvs = sys.argv
argv_len = len(argvs)

if __name__ == "__main__":
    if argv_len == 1:
        print("0 arguments.")
    else:
        if argv_len == 2:
            print("{} argument:".format(argv_len - 1))
        else:
            print("{} arguments:".format(argv_len - 1))

        for index in range(1, argv_len):
            print("{}: {}".format(index, argvs[index]))
