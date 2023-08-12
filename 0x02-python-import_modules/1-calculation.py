#!/usr/bin/python3
""""print sum, difference, multiple and quotient of integers"""
from calculator_1 import add, sub, mul, div

# Assigning value 10 to variable "a"
a = 10

# Assigning value 5 to variable "b"
b = 5

# performing addition using "add" function
result_add = add(a, b)

# performing sbutraction using "sub" function
result_sub = sub(a, b)

# performing multiplication using "mul" function
result_mul = mul(a, b)

# performing division using "div" function
result_div = div(a, b)

# printing the result
print("{} + {} = {}".format(a, b, result_add))

print("{} - {} = {}".format(a, b, result_sub))

print("{} * {} = {}".format(a, b, result_mul))

print("{} / {} = {}".format(a, b, result_div))
