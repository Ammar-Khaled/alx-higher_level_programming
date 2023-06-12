#!/usr/bin/python3
"""This module defines a class called 'MyList'."""


class MyList(list):
    """ a class that represents my own list type."""

    def print_sorted(self):
        """ prints the list, but sorted ascendingly sort
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
