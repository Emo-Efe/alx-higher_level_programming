#!/usr/bin/python3
"""function that computes the square value of all integers of a matrix."""
def square_matrix_simple(matrix=[]):
    matrix_new = [row[:] for row in matrix]
    for idx, row in enumerate(matrix_new):
        for idx2, col in enumerate(matrix_new):
            matrix_new[idx][idx2] = row[idx2] ** 2
    return matrix_new
