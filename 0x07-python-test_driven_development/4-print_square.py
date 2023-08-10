#!/usr/bin/python3
"""
a module that contains a function that prints  a square with the character #.
"""


def print_square(size):
    """
       a function that prints a  square with the character #

       Args:
            size of the square
       Returns:
               printed square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size is float and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
