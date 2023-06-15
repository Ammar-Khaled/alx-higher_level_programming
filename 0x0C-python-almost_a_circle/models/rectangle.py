#!/usr/bon/python3
""" This module defines the `Rectangle` class."""

Base = __import__('base').Base


class Rectangle(Base):
    """ The Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #."""
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """ returns string representation of the rectangle."""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """ assigns an argument to each attribute."""
        if len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
