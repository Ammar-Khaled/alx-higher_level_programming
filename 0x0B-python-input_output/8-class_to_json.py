#!/usr/bin/python3
""" This module defines class_to_json() function."""


def class_to_json(obj):
    """  retuns the dictionary description of an obj

        Args:
            obj: an object to be serialised

        Returns:
            the dictionary description with simple data structure
            (list, dictionary, string, integer and boolean)
            for JSON serialization of an object.
    """

    dict = {}

    if hasattr(obj, '__dict__'):
        dict = obj.__dict__.copy()

    return dict
