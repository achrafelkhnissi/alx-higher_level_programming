#!/usr/bin/python3


"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n


    Arguments:
        n {int} -- [size of triangle]

    Returns:
        list -- [list of lists of integers representing Pascal's triangle of n]
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
