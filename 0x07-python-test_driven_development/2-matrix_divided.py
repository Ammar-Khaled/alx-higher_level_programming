#!/usr/bin/python3
"""This module is to  divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix."""

    ans =[]

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])

    i = -1
    for l in matrix:
        if type(l) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        if len(l) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        
        ans.append([])
        i += 1
        for e in l:
            if type(e) != int and type(e) != float:
               raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
            ans[i].append(round(e/div, 2))

    return ans

