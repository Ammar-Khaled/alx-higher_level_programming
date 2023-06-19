#!/usr/bon/python3
""" This module defines the `Base` class of all other classes in this project.
    The goal of it is to manage `id` attribute."""

import json
import csv


class Base:
    """ The base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file."""

        list_dicts = []

        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dicts)

        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of dictionaries represented by the JSON string"""

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""

        # create a dummy object with dummy mandatory attributes
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        else:
            obj = cls()

        obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances read from a file."""

        try:
            f = open('{}.json'.format(cls.__name__), 'r', encoding='utf-8')
            json_string = f.read()

            list_dicts = cls.from_json_string(json_string)

            list_objs = []
            for dict in list_dicts:
                list_objs.append(cls.create(**dict))

            return list_objs
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves objects in csv file."""
        list_dicts = []

        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        with open('{}.csv'.format(cls.__name__), 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, list_dicts[0].keys())

            writer.writeheader()

            writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """ load object from csv file."""

        try:
            f = open('{}.csv'.format(cls.__name__), 'r', encoding='utf-8')

            reader = csv.DictReader(f)

            list_dicts = []
            for row in reader:
                list_dicts.append(row)

            list_objs = []
            for dict in list_dicts:
                for key, value in dict.items():
                    dict[key] = int(value)
                list_objs.append(cls.create(**dict))

            return list_objs
        except FileNotFoundError:
            return []
