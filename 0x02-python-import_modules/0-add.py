#!/usr/bin/python3
from add_0 import add

#Assigning a value 1 to variable "a"
a = 1

#Assigning a value 2 to variable "b"
b = 2

# Calling the "add" function from "add_0" with module "a" $ "b"
result = add(a, b)

# Printing the formated string and giving the result
print("{} + {} = {}".format(a, b, result))
