#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0

    for elem in my_list[:x]:
        if isinstance(elem, int):
            print("{:d}".format(elem), end="")
            num_printed += 1
    print()
    return num_printed
