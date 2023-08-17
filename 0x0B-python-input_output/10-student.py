#!/usr/bin/python3
"""My class Student"""


class Student:
    """represntation of a class student"""
    def __init__(self, first_name, last_name, age):
        """
        this function initializes public instance attributes

        Parameters:
        self
        first_name
        last_name
        age

        Returns:
        attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        this function retrieves a dictionary representation of Student instance

        Parameters:
        self
        attrs

        Returns:
        a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            attributes = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attributes[attr] = getattr(self, attr)
            return attributes
