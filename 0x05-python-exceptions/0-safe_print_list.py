#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numbers_to_printed = 0
    try:
        while numbers_to_printed < x:
            print(my_list[numbers_to_printed], end="")
            numbers_to_printed += 1
    except IndexError:
        pass
    finally:
        print()
    return numbers_to_printed
