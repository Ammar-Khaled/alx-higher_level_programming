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

    @property
    def size(self):
        """property to retrieve square size"""
        return self.__size

    @size.setter
    def size(self, size):
        """property setter to set square size
        Args:
            param1 (int): size to be set
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints a square with hashes"""
        if (self.size == 0):
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
