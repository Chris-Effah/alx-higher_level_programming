#!/usr/bin/python3
"""A class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    a class that inherits from Base

    Private instance Attributes:
    __width
    __height
    __x
    __y

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        new rectangle class initiated

        Args:
            id: rectangle identity
            width: width of the rectangle
            height: height of the rectangle
            x
            y
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
