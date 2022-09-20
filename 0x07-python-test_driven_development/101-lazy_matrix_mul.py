#!/usr/bin/python3
"""
This 101-lazy_matrix_mul module has one function, lazy_matrix_mul(m_a, m_b)
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices."""

    return (np.matmul(m_a, m_b))
