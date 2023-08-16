#!/usr/bin/python3
"""function - read_file"""


def read_file(filename=""):
    """
    this function reads a text file and prints it to stdout

    Parameters:
    filename - name of the file to read

    Returns:
    file read
    """
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
