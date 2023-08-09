#!/usr/bin/python3
"""
   a module that contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
       a function that divides all elements of a matrix

       first arg:
                 matrix

       second arg:
                  divisor
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("dividion by zero")

    n_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return n_matrix
