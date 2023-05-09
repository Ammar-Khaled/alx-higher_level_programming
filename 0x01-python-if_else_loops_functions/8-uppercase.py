#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            print('{:c}'.format(ord(str[i]) - 32), end='')
        else:
            print(str[i], end='')
    print()
