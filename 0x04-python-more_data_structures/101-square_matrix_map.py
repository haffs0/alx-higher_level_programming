#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: [m * m for m in x], matrix))
