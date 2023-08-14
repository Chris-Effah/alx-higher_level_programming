#!/usr/bin/python3
"""An class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass of BaseGeometry"""

    def __init__(self, width, height):
        """instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
