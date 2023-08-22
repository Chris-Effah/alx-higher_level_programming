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
            id: rectangle identity
            width: width of the rectangle
            height: height of the rectangle
            x:x coordinnate
            y: y coordinate
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        public getter

        Parameters:
        self

        Returns:
        obtained property of the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        public setter

        Parameters:
        self
        value

        Returns:
        set value of the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        public getter

        Parameters:
        self

        Returns:
        property of height attribute obtained
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        public setter

        Parameters:
        self
        value

        Returns:
        set value of the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        public getter

        Parameters:
        self

        Returns:
        property of x attribute obtained
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        public setter

        Parameters:
        self
        value

        Returns:
        set value of the x attribute
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        public getter

        Paramters:
        self

        Returns:
        property of y obtained
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        public setter

        Parameters:
        self
        value

        Returns:
        set value of attribute y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        public method for the area of a rectangle

        args:
        self

        returns:
        area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        public method to print the character # in stdout

        Parameters:
        self

        Returns:
        printed character #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def to_dictionary(self):
        """
        method to convert args of the rectangle class to a dict

        Parameters:
        self

        Return:
        dictionary representation of rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
