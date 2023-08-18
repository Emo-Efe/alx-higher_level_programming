#!/usr/bin/python
"""function that replaces all occurrences of an element by another in a new list"""


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    my_new_list = my_list[:]
    for idx, i in enumerate(my_new_list):
        if i == search:
            my_new_list[idx] = replace
    return my_new_list
