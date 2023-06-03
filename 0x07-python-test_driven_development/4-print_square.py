#!/usr/bin/python3
"""This module is to print a squar."""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer number


    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print("#" * size)


