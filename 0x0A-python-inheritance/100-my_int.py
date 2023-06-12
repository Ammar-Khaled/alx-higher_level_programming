#!/usr/bin/python3
"""This module defines a class called 'MyInt'."""


class MyInt(int):
    """ a class that represents my own int type.
        Args:
            int: class int

    """

    def __eq__(self, value):
        """ behave as !=.
        Args:
            value: to be compared
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """ behave as ==.
        Args:
            value: to be compared
        """
        return super().__eq__(value)
