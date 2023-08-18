#!/usr/bin/python3
"""function that returns a list with all values multiplied by a number without using any loops """


def multiply_list_map(my_list=None, number=0):
    if my_list is None:
        my_list = []
    return list(map(lambda j: j * number, my_list))
