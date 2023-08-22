#!/usr/bin/python3
"""
defines a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    a class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
	new rectangle class initiated

        Args:
            id(int): rectangle identity
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): x coordinnate
            y(int): y coordinate
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """public getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """public setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """public getter"""
        return self.__height

    @height.setter
    def height(self, value):
         """public setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """public getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """public setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """public getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """public setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method for the area of a re
        return self.width * self.height

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
