#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        squared = []
        i = 0
        for row in matrix:
            squared.append([])
            for element in row:
                squared[i].append(element ** 2)
            i = i + 1
        return squared
