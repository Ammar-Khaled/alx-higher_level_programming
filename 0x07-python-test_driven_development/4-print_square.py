#!/usr/bin/python3
"""This module is to print a squar."""


def print_square(size):
    """prints a square with the character #."""

    if type(size) != int and type(size) != float:
        raise TypeError("size must be a string")
    
    if size < 0:
        raise TypeError("size must be >= 0")
    
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print("#" * size)


