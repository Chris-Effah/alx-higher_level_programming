#!/usr/bin/python3
"""a function that adds integer"""


def add_integer(a, b=98):
    """
    function that adds two integers

    Args:
        first arg: first number
        second arg: second number

    Returns:
        int: result of addition

    Raises:
        TypeError: if a or b are not integers or floats.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
