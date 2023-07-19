#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    result = 0
    for element in my_set:
        result = result + element
    return result
