#!/usr/bin/python3
"""
This module is to define a Square object
"""


class Square:
    """An empty class to define a Square object"""
    def __init__(self, size=0, position=(0, 0)):
        """initialises a new Square instance

        Args:
            param1 (int): size of the square
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieve square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setting the position of a square
        Args:
        param1 (tuple): value to be set
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints a square with hashes"""
        if (self.size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                print(" " * self.position[0], end='')
                print("#" * self.size)

    def __str__(self) -> str:
        """define what to print in the print statement on a Square"""
        msg = ""
        if (self.size == 0):
            pass
        else:
            for i in range(self.position[1]):
                msg += "\n"
            for i in range(0, self.size):
                msg += " " * self.position[0]
                msg += "#" * self.size
                msg += "\n"
        return msg
