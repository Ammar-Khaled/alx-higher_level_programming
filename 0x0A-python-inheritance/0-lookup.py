#!/usr/bin/python3
"""This module defines a method working as dir()."""


def lookup(obj):
    """ a function that gets the list of available attributes and methods
        of an object.

        Args:
            obj: an object

        Returns:
            A list of object's attributes and methods

    """

    return dir(obj)
