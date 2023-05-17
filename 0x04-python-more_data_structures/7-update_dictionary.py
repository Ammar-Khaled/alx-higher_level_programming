#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    updated_dict = dict(a_dictionary)
    updated_dict.update({key: value})
    # updated_dict[key] = value also works for new keys
    return updated_dict
