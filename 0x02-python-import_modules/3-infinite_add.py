#!/usr/bin/python3
""""Prints the result of addition of all argument """
import sys

# Retrieving arguments passed
args = sys.argv[1:]

# Initializing the variable to store the argument
sum_of_args = 0

# iterating over the arguments & adding to sum
for arg in args:
    sum_of_args += int(arg)

print(sum_of_args)
