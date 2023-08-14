#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry():
    """an area method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if not is instance(value, int):
            raise TypeError(f"{name} must be an integr")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

