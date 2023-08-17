#!/usr/bin/python3
"""json module"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    this function adds all arguments to a Python list, and save them to a file

    Parameters:
    void

    Returns:
    a file with a python list
    """
    arguments = sys.argv[1:]
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []
    data.extend(arguments)

    save_to_json_file(data, "add_item.json")


if __name__ == "__main__":
    main()
