#!/usr/bin/python3
"""function that returns a key with the biggest integer value."""


# Emo-Efe 
def best_score(a_dictionary):
    if not a_dictionary:
        return(None)
    return (max(a_dictionary, key=a_dictionary.get))
