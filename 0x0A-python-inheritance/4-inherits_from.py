#!/usr/bin/python3
""" This module defines a function that checks for
    the type of an object.
"""


def inherits_from(obj, a_class):
    """ checks if an object is of some type.

        Args:
            obj: an object
            a_class: a class

        Returns:
            True if the object is an instance of a class that
            inherited (directly or indirectly) from the specified class
            False: otherwise
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
