#!/usr/bin/python3
"""the json module"""


import json

def load_from_json_file(filename):
    """
    this function  that creates an Object from a “JSON file”

    Parameters:
    filename - name of file

    Returns:
    returns the created object from the json file
    """
    data = None
    with open(filename, "r")as file:
        data = json.load(file)
    return data
