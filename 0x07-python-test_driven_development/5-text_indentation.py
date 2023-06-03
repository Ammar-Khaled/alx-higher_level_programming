#!/usr/bin/python3
"""
This module is to print a text with 2 new lines after
each of these characters: ., ? and :

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """

    if type(text) != str:
        raise TypeError("text must be a string")

    text = text.strip()
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            text = text[:i].strip() + text[i] + "\n\n" + text[i+1:].strip()

    print(text)

