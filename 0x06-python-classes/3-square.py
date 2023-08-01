#!/usr/bin/python3

"""defining a class square"""


class Square:

    """initializing a size attribute"""
    def __init__(self, size=0):

        """if size is not an integer"""
        if not isinstance(size, int):
            """raising a type error"""
            raise TypeError("size must be an integer")
        """if size is greater than zero"""
        if size < 0:
            """raising a value error"""
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
