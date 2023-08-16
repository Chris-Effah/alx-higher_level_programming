#!/usr/bin/python3
"""function - write_file"""


def write_file(filename="", text=""):
    """
    this function writes a string to a text file

    Parameters:
    filename - name of the file
    text - text to write to the file

    Returns:
    updated file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        num_of_chars_written = file.write(text)
        return num_of_chars_written
