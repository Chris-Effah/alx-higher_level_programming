#!/usr/bin/python3
"""a function - inherits"""


def inherits_from(obj, a_class):
    """
    this function that  returns True if the object is an instance of a
    class that inherited (directly or indirectly)

    Parameters:
    obj
    a_class

    Returns:
    True if the object is an instance of a class that inherited directly or
    indirectly from the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
