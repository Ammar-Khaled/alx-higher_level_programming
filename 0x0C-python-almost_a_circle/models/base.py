#!/usr/bon/python3
""" This module defines the `Base` class of all other classes in this project.
    The goal of it is to manage `id` attribute."""


class Base:
    """ The base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor."""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
