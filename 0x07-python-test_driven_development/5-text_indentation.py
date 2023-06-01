#!/usr/bin/python3
"""This module is to print a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints text indentation"""

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            text = text[:i+1] + "\n\n" + text[i+2:]

    print(text)

