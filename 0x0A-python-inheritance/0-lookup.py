#!/usr/bin/python3
"""a function lookup"""


def lookup(obj):
    """
    this function returns the list of available attributes and methods of
    an object

    Parameters:
    obj

    Returns:
    a list of attributes and methods of an object
    """
    return dir(obj)
