#!/usr/bin/python3
def magic_string(list=[]):
    list += ["Best School"]  # with each call, the list object grows in memory
    return ", ".join(list)
