#!/usr/bin/python3
"""A module of a function that adds two integer
test cases written for this function
"""


def add_integer(a, b=98):
    """Function that adds two integers
        Returns the sum of the integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
