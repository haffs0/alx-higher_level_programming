#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for items in matrix:
        for item in items:
            print("{}".format(item), end=" ")
        print("")
