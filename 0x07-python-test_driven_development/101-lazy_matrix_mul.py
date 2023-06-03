#!/usr/bin/python3
"""This module multiplies 2 matrices by using the module NumPy"""


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


    """

    import numpy as np

    return np.matmul(m_a, m_b)
