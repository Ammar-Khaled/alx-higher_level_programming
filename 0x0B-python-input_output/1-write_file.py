#!/usr/bin/python3
""" This module defines write_file() function."""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8).

        Args:
            file_name: the path of the file to be read
            text: the string to be written

        Returns:
            the number of characters written.

        Raises
            Exception: when the file can;t be opened
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
