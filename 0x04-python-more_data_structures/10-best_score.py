#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest_value = max(a_dictionary.keys())
    return highest_value
