#!/usr/bin/python3
"""This module multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied


    """

    if type(m_a) != list:
        raise TypeError("m_a must be a list")

    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or m_a == [[]]:
        raise TypeError("m_a can't be empty")

    if len(m_b) == 0 or m_b == [[]]:
        raise TypeError("m_b can't be empty")

    for row_a in m_a:
        if type(row_a) != list:
            raise TypeError("m_a must be a list of lists")

        if len(row_a) == 0:
            raise TypeError("m_a can't be empty")

    for row_b in m_b:
        if type(row_b) != list:
            raise TypeError("m_b must be a list of lists")

        if len(row_b) == 0:
            raise TypeError("m_b can't be empty")

    len_row_a = len(m_a[0])
    len_row_b = len(m_b[0])

    for row_a in m_a:

        if len(row_a) != len_row_a:
            raise TypeError("each row of m_a must be of the same size")

        for e in row_a:
            if type(e) != int and type(e) != float:
                raise TypeError("m_a should contain only integers or floats")

    for row_b in m_b:
        if len(row_b) != len_row_b:
            raise TypeError("each row of m_b must be of the same size")

        for e in row_b:
            if type(e) != int and type(e) != float:
                raise TypeError("m_b should contain only integers or floats")

    # if m_a and m_b can't be multiplied
    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")

    ans_idx = -1
    ans = []

    # for each row in m_a
    for row_a in m_a:

        ans_idx += 1
        ans.append([])
        col_idx = -1

        for it in range(len(m_b[0])):
            entry = 0
            col_idx += 1
            for j in range(len(m_b)):
                entry += row_a[j] * m_b[j][col_idx]
            ans[ans_idx].append(entry)

    return ans
