#!/usr/bin/python3

"""define a class square"""


class Square:
    """initialize the size attribute"""

    def __init__(self, size=0):
        """if size attribute is not an integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
