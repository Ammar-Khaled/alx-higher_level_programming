#!/usr/bin/python3
""" This module defines append_after() function"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file,
        after each line containing a specific string"""

    with open(filename, 'r', encoding='utf-8') as rf:
        lines = rf.readlines()

    with open(filename, 'w', encoding='utf-8') as wf:
        for line in lines:
            wf.write(line)
            if search_string in line:
                wf.write(new_string)
