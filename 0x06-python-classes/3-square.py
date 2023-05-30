#!/usr/bin/python3
"""
This module is to define a Square object
"""


class Square:
    """An empty class to define a Square object"""
    def __init__(self, size=0):
        """initialises a new Square instance

        Args:
            param1 (int): size of the square
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
