#!/usr/bin/python3
""" This module defines read_file() function."""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout.

        Args:
            file_name: the path of the file to be read

        Raises
            Exception: when the file can be opened
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
