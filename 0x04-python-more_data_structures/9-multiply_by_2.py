#!/usr/bin/python3
"""function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    my_dic = {}
    for i in a_dictionary:
        my_dic[i] = a_dictionary[i] * 2
    return my_dic
