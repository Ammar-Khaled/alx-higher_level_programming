#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print(element, end='')
            if element != row[-1]:
                print(' ', end='')
        print()
                
        