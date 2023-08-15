#!/usr/bin/python3
"""function - add_attribute"""


def add_attribute(obj, name, value):
    """
    this function adds a new attribute to an object

    Parameters:
    obj
    name
    value

    Returns:
    added attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
