#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict(a_dictionary)
    to_remove = []
    for key, v in new_dict.items():
        if value == v:
            to_remove.append(key)

    for key in to_remove:
        new_dict.pop(key)

    return new_dict
