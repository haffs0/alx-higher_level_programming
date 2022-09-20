#!/usr/bin/python3
"""
This 100-matrix_mul module has two function, dot(), matrix_mul()
"""


def matrix_mul(m_a, m_b):
    """Return multiplication of two matrix"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    len_m_a = len(m_a[0])
    len_m_b = len(m_b[0])

    for row in m_a:
        if len_m_a != len(row):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if len_m_b != len(row):
            raise TypeError("each row of m_b must be of the same size")

    col_ma = len(m_a[0])
    row_mb = len(m_b)

    if col_ma != row_mb:
        raise ValueError("m_a and m_b can't be multiplied")

    transpose_m = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        transpose_m.append(new_row)

    matrix_mul = []
    for row in m_a:
        new_row = []
        for col in transpose_m:
            prod = 0
            for i in range(len(transpose_m[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        matrix_mul.append(new_row)

    return (matrix_mul)
