#!/usr/bin/python3
"""
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """Return the new matrix divided by div"""
    row = len(matrix[0])
    for m in matrix:
        string = "matrix must be a matrix (list of lists) of integers/floats"
        if type(m) not in [list]:
            raise TypeError(string)
        if row != len(m):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for m in matrix:
        inner_matrix = []
        for j in m:
            inner_matrix.append(round((j / div), 2))
        new_matrix.append(inner_matrix)
    return (new_matrix)
