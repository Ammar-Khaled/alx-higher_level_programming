#!/usr/bin/python3
"""This module is to  divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    ans = []
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or type(matrix) != list:
        raise TypeError(type_msg)

    row_length = len(matrix[0])

    i = -1
    for row in matrix:
        if not row or type(row) != list:
            raise TypeError(type_msg)

        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        ans.append([])
        i += 1
        for e in row:
            if type(e) != int and type(e) != float:
                raise TypeError(type_msg)

            ans[i].append(round(e/div, 2))

    return ans
