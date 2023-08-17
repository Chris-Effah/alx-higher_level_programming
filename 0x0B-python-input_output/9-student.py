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

    def to_json(self):
        """
        this function retrieves a dictionary representation of Student instance

        Parameters:
        self

        Returns:
        a dictionary representation of a Student instance
        """
        attributes = {
            attr: value
            for attr, value in vars(self).items()
            if isinstance(value, (list, dict, str, int, bool))
        }
        return attributes
