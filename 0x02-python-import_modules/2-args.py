#!/usr/bin/python3
""""prints the number of an list of the arguments"""
import sys

# Retrieving the argument passed
args = sys.argv[1:]

# Getting the numbe of the arguments
num_args = len(args)

# printing the numebr of arguments
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))

#printing each argument and position
for i, arg in enumerate(args):
    print("{}: {}".format(i + 1, arg))
