#!/usr/bin/python3
""" This module defines from_json_string() function."""


def from_json_string(my_str):
    """ returns an object (Python data structure) represented by a JSON string

        Args:
            my_str: json string to be converted

        Returns:
            Python object represented by a JSON string

        Raises
            Exception: if the JSON string doesn't represent an object.
    """

    import json
    return json.loads(my_str)
