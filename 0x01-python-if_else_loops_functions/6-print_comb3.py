#!/usr/bin/python3
for i in range(9):  # 0 1 2 3 .. 8
    j = i + 1
    while j <= 9:  # i+1 ... 9
        if i == 8 and j == 9:
            print('{}{}'.format(i, j))
        else:
            print('{}{}'.format(i, j), end=', ')
        j = j + 1
