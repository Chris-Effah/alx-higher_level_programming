#!/usr/bin/python3
import json

"""json module"""


def from_json_string(my_str):
    """
    this function returns an object (Python data structure) represented by
    a JSON string

    Parameters:
    my_str

    Returns:
    an object represented by a JSON string
    """
    return json.loads(my_str)
