#!/usr/bin/python3
"""
   a module that contains a function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """
       a function that prints My name is <first name> <last name>

       Args:
            first_name
            last_name
       Returns:
               the printed name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name
    if last_name:
        full_name += " " + last_name
    print("My name is", full_name)
