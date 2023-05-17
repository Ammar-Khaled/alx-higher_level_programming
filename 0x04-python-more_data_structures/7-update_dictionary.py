#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})
    # a_dictionary[key] = value also works for new keys
    return a_dictionary
