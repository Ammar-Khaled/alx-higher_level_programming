#!/usr/bin/python3
""" This module defines save_to_json_file() function."""


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation.

        Args:
            my_obj: object
            filename: file name

        Raises
            Exception: if the object can't be serialized.
    """

    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
