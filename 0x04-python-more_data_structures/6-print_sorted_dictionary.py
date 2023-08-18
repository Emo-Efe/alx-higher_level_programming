#!/usr/bin/python3
"""function that prints a dictionary by ordered keys."""
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary.get(i)))
