#!/usr/bin/python3
def remove_char_at(str, n):

    # if index is out of range remove nothing
    if n < 0 or n > len(str) - 1:
        return str

    str = list(str)
    str[n] = ''
    ans = ''
    for i in range(len(str)):
        ans += str[i]
    return ans
