#!/usr/bin/python3
"""a module that contains a function that prints a text with 2 new lines"""


def text_indentation(text):
    """a function that prints a text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    buffer = ""


    for char in text:
        buffer += char
        if char in punctuations:
            print(buffer.strip())
            print()
            buffer = ""
    print(buffer.strip())
