#!/usr/bin/python3
""" This module defines a Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class for rectangle shapes
    """

    def __init__(self, width, height):
        """ init function

            Args:
                width: rectangle width
                height: rectangle height

            Raises:
                TypeError: if width or height is not be an integer
                ValueError: if width or height is less than or equal to zero
          """

        super().integer_validator('width', width)
        super().integer_validator('height', height)

        self.__width = width
        self.__height = height
