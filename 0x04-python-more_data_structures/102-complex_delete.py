#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_remove = []
    for key, v in a_dictionary.items():
        if value == v:
            to_remove.append(key)

    for key in to_remove:
        a_dictionary.pop(key)

    return a_dictionary
