#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sorted_tuples = sorted(dict(a_dictionary).items())
        for key, value in sorted_tuples:
            print("{}: {}".format(key, value))
