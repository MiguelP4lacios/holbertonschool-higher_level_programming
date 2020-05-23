#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Mudule
"""


def matrix_divided(matrix, div):
    """matrix_divided

    Arguments:
        matrix {[type]} -- [description]
        div {[type]} -- [description]
    """

    e1 = "matrix must be a matrix (list of lists) of integers/floats"
    e2 = "Each row of the matrix must have the same size"
    e3 = "div must be a number"
    e4 = "division by zero"

    if type(matrix) != list:
        raise TypeError(e1)
    for row in matrix:
        if type(row) != list:
            raise TypeError(e1)

    size_row = len(matrix[0])

    for row in matrix:
        if len(row) != size_row:
            raise TypeError(e2)
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(e1)
    if type(div) not in [int, float]:
        raise TypeError(e3)

    if div == 0:
        raise ZeroDivisionError(e4)

    return [[round(elem / div, 2) for elem in row]for row in matrix]
