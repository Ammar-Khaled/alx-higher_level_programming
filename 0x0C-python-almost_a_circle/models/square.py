#!/usr/bon/python3
""" This module defines the `Square` class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns string representation for a square instance."""
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter."""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update square attributes."""
        if args is not None and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
