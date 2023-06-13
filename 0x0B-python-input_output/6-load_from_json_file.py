#!/usr/bin/python3
""" This module defines load_from_json_file() function."""


def load_from_json_file(filename):
    """ creates an Object from a JSON file

        Args:
            filename: file name

        Returns:
            Python Object encoded in the json file

        Raises
            Exception: if the JSON string doesn't represent an object.
    """

    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
