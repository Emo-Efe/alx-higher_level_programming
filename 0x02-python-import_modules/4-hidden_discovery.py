#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """"print all names defined in hidden_4 module"""

    # Retrieving the list of all defined names by hidden_4 module
    names = dir(hidden_4)

    # iterating over the names 
    for name in names:
        if not names.startswith("__"):
            print(name)
