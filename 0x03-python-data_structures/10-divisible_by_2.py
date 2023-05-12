#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_mul2 = []
    for i in my_list:
        if i % 2 == 0:
            is_mul2.append(True)
        else:
            is_mul2.append(False)
    return is_mul2
