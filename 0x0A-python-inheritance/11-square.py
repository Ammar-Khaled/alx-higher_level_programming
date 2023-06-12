#!/usr/bin/python3
""" This module defines a Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class for square shapes
    """

    def __init__(self, size):
        """ init function

            Args:
                size: square side size

            Raises:
                TypeError: if size is not be an integer
                ValueError: if size is less than or equal to zero
          """

        super().integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ calculate square area."""
        return super().area()

    def __str__(self):
        """ string info for object."""

        return '[Square] {}/{}'.format(self.__size, self.__size)
