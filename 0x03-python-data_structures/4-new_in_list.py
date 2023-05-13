#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i in my_list:
        new_list.append(i)

    if 0 <= idx < len(new_list):
        new_list[idx] = element

    return (new_list)
