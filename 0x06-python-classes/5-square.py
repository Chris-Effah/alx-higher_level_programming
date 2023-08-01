#!/usr/bin/python3


"""defining a class called square"""


class Square:
    def __init__(self, size=0):
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
        return self.__size ** 2

    def my_print(self):
        for _ in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()