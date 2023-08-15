#!/usr/bin/python3
"""a class that inherits """


class MyInt(int):
    """
    class that inherits the attributes and methods of the int class

    Parameters:
    int

    Returns:
    operators
    """
    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
