#!/usr/bin/python3
"""function - to_json_string"""

import json

def to_json_string(my_obj):
    """
    this function returns the JSON representation of an object (string)

    Parameter:
    my_obj

    Returns:
    returns the JSON representation of an object
    """
    return json.dumps(my_obj)
