#!/usr/bin/python3
lower = True
for i in range(26):
    if lower:
        print('{:c}'.format(ord('z') - i), end='')
    else:
        print('{:c}'.format(ord('z') - i - 32), end='')
    lower = not lower
