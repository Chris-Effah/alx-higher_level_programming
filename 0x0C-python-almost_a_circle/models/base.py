#!/usr/bin/python3
"""my first class base"""
import json


class Base:
    """
    this is the 'base' classs for all classes in this project

    Private Class Attributes:
    __nb_object (int): the number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing a class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
