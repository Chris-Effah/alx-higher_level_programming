#!/usr/bin/python3
import json
"""json modile"""


def save_to_json_file(my_obj, filename):
    """
    this function  writes an Object to a text file, using a JSON representation

    Parameters:
    my_obj - object being written to
    filename - name of file

    Returns:
    update file
    """
    with open(filename, "w")as file:
        return json.dump(my_obj, file)
