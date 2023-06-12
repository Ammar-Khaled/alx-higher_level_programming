#!/usr/bin/python3
""" This module defines a function that checks for
    the type of an object.
"""


def is_kind_of_class(obj, a_class):
    """ checks if an object is of some type.

        Args:
            obj: an object
            a_class: a class

        Returns:
            True: if the object is an instance of the specified class
            or an instance of a derived class of it
            False: otherwise
    """

    return isinstance(obj, a_class)
