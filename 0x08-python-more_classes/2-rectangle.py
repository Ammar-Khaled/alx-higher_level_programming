#!/usr/bin/python3
""" This module defines a class for a Rectangle object. """


class Rectangle:
    """ This class defines a Rectangle object. """

    def __init__(self, width=0, height=0) -> None:
        """ Instantiation of Rectangle object with optional width and height

            Args:
                width: width of rectangle
                height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to get the Rectangle width"""

        return self.__width

    @property
    def height(self):
        """property to get the Rectangle height"""

        return self.__height

    @width.setter
    def width(self, value):
        """set the width of the Rectangle

        Args:
            value: the width to be set

        Raises:
            TypeError: if width is not integer
            ValueError: if width is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """set the height of the Rectangle

        Args:
            value: the height to be set

        Raises:
            TypeError: if height is not integer
            ValueError: if height is less than 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns the rectangle area"""

        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""

        if self.width == 0 or self.height == 0:
            return (0)

        return ((self.width + self.height) * 2)
