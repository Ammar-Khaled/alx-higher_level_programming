#!/usr/bin/python3
""" This module defines Student class."""


class Student:
    """ represents Student object"""

    def __init__(self, first_name, last_name, age):
        """ init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves attrs from the dictionary representation
            of a Student instance."""
        full_dict = self.__dict__.copy()

        if type(attrs) == list:
            for element in attrs:
                if type(element) != str:
                    return full_dict

            new_dict = {}
            for attr in full_dict:
                if attr in attrs:
                    new_dict[attr] = full_dict[attr]
            return new_dict

        return full_dict
