#!/usr/bin/python3
"""function that computes the square value of all integers of a matrix."""


# Emo-Efe on the code

# create our special func
def square_matrix_simple(matrix=[]):
    # making use of the new func
    matrix_new = matrix.copy()
# a for loop
    for i in range(len(matrix)):
        matrix_new[i] = list(map(lambda x: x**2, matrix[i]))

# now return statement
    return (matrix_new)
