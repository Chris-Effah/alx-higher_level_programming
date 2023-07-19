#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    for key, value in a_dictionary.items():
        mul = value * 2
        new_dict[key] = mul
    return new_dict
