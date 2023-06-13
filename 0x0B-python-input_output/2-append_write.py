#!/usr/bin/python3
""" This module defines append_write() function."""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8).

        Args:
            file_name: the path of the file to be read
            text: the string to be written

        Returns:
            the number of characters added.

        Raises
            Exception: when the file can't be opened
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
