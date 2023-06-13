#!/usr/bin/python3
""" This module defines pascal_triangle(n)"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal's triangle of n."""

    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    lists = []
    lists.append([1])
    for i in range(1, n):
        lists.append([])
        lists[i].append(1)
        for j in range(1, i):
            lists[i].append(lists[i-1][j-1] + lists[i-1][j])
        lists[i].append(1)

    return lists
