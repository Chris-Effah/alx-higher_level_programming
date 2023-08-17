#!/usr/bin/python3
"""json module"""


def class_to_json(obj):
    """
    this function returns the dictionary desc with simple data structure

    Parameters:
    obj

    Returns:
    dictionary description with simple data structure
    """
    attributes = {
        attr: value
        for attr, value in vars(obj).items()
        if isinstance(value, (list, dict, str, int, bool))
    }
    return attributes
