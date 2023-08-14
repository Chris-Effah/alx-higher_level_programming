#!/usr/bin/python3
"""a subclass"""


class MyList(list):
    """a function print_sorted"""

    def print_sorted(self):
        """
        this function that prints the list, but sorted

        Parameters:
        self

        Returns:
        a sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
