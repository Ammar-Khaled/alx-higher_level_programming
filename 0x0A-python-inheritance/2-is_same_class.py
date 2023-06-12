#!/usr/bin/python3
""" This module defines a function that checks for
    the type of an object.
"""


def is_same_class(obj, a_class):
    """ checks if an object is of some type.

        Args:
            obj: an object
            a_class: a class

        Returns:
            True: if the object is an instance of the specified class
            False: otherwise
    """

    return type(obj) == a_class
