#!/usr/bin/python3
""" This module defines a function that adds a new attribute
    to an object if it is possible."""


def add_attribute(obj, attr_name, attr_value):
    """ adds a new attribute to an object if it is possible.

        Args:
            obj: an object
            attr_name: attribute name
            attr_value: attribute value

        Raises:
            TypeError: if the object can't have new attribute
    """

    if type(obj) in [int, float, complex, str, tuple, frozenset]:
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
