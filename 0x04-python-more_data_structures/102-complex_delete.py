#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted_keys = []

    for key, val in a_dictionary.items():
        if val == value:
            deleted_keys.append(key)

    for key in deleted_keys:
        del a_dictionary[key]
    return a_dictionary
