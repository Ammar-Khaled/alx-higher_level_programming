#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    sorted_tuples = sorted(dict(a_dictionary).items(), key=lambda t: t[1])
    return sorted_tuples[-1][0]
