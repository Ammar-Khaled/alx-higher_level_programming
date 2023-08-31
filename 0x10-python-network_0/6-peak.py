#!/usr/bin/python3
""" Module that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""

    if not list_of_integers:
        return None

    length = len(list_of_integers)

    if length == 0:
        return None

    if length == 1:
        return list_of_integers[0]

    start = 0
    end = length - 1
    ls = list_of_integers
    while start <= end:
        mid = (start + end) >> 1
        if (mid == 0 or ls[mid] >= ls[mid - 1]) and (mid == length - 1 or ls[mid] >= ls[mid + 1]):
            break
        elif mid > 0 and ls[mid] < ls[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1
    return ls[mid]
