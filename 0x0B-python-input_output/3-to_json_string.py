#!/usr/bin/python3
""" This module defines to_json_string() function."""


def to_json_string(my_obj):
    """ gets the JSON representation of an object (string).

        Args:
            my_obj: string object to be converted

        Returns:
            JSON string representation of an object

        Raises
            Exception: if the object can't be serialized.
    """

    import json
    return json.dumps(my_obj)
