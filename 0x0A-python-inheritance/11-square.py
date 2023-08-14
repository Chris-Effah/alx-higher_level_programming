#!/usr/bin/python3
"""An class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass of BaseGeometry"""

    def __init__(self, width, height):
        """instantiation with width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """implementing the area method"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """a subclass of Rectangle"""

    def __init__(self, size):
        """instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str() method"""
        return f"[Square] {self.__size}/{self.__size}"
