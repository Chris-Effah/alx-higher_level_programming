#!/usr/bin/python3
"""function - append_write"""


def append_write(filename="", text=""):
    """
    this function appends text to a file

    Parameters:
    filename - name off the file
    text - text to append to the file

    Returns:
    updated file
    """
    with open(filename, "a", encoding="utf-8") as file:
        content = file.write(text)
        return content
