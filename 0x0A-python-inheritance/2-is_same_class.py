#!/usr/bin/python3
"""function - is_same_class"""


def is_same_class(obj, a_class):
    """
    this function returns True if the object is exactly an instance of the
    specified class

    Parameters:
    obj
    a_class

    Returns:
    True
    """
    return (type(obj) is a_class)
