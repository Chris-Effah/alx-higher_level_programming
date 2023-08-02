#!/usr/bin/python3

"""defining a class called square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """Initialize a new square."""
        self.__size = size

    @property
    def size(self):
        """retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """define the != comparison to square instance"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other):
        """defining the > comparison to square instance"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """defining the >= comparison to square"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """defining the < comparison to square"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """define the <= comparison to square"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
