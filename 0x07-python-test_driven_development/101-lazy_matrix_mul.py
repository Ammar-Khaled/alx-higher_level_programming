#!/usr/bin/python3
"""This module multiplies 2 matrices by using the module NumPy"""


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy"""

    import numpy as np

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    return np.dot(m_a, m_b)

