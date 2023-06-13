#!/usr/bin/python3
""" This module defines Student class."""


class Student:
    """ represents Student object"""

    def __init__(self, first_name, last_name, age):
        """ init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance."""
        dict = self.__dict__.copy()

        if type(attrs) == list:
            for element in attrs:
                if type(element) != str:
                    return dict

            new_dict = {}
            for i in range(len(attrs)):
                for attr in dict:
                    if attr == attrs[i]:
                        new_dict[attr] = dict[attr]
            return new_dict

        return dict
