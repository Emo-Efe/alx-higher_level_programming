#!/usr/bin/python3
"""function that computes the square value of all integers of a matrix using"""


def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
