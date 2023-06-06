#!/usr/bin/python3
"""

This module containts a class that avoids
creating instance attributes dynmaically.

"""


class LockedClass:
    """ A class with a specific list of permitted instance attributes
        ,which can be dynamically created.
    """

    __slots__ = ['first_name']
    # The __slots__ attribute is a special attribute that can be used to
    # define a list of allowed instance attributes for a class.
    # Any attempt to dynamically create a new instance attribute
    # that is not in the __slots__ list will raise an AttributeError.

    def __init__(self) -> None:
        """ initiation function """
        pass
