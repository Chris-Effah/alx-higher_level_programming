#!/usr/bin/python3

"""defining a MagicClass that does exactly the same as a Python bytecode"""

import math


class MagicClass:
    """represents a circle"""

    def __init___(self, radius=0):
        """initialzing a new magicclass"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """returning the radius of a MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return the circumference"""
        return (2 * math.pi * self.__radius)
