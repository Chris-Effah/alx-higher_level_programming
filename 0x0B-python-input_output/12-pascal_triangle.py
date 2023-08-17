#!/usr/bin/python3
"""pascaltriangle"""


def pascal_triangle(n):
    """a function that returns a lists of lists representing pascal's triangle
    """
    if n <= 0:
        return []

    tri = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
        tri.append(row)
    return tri
