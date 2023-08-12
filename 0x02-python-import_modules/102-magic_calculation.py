#!/usr/bin/python3
def magic_claculation(a, b):
    """"performs a magic calculation"""
    
    # Importing 'add' amd 'sub' function
    add = __import__('magic_calculation_102').add
    sub =  __import__('magic_calculation_102').sub

    #Performing addition to store the result in c
    if a < b :
        c = add( a, b)

     #Performing addition in multiple times
        for i in range(4, 6):
            c = add(c, i)

    # Rturning the final result
        return c
    else:
        #performs sub and returns the result.
        return sub(a, b)
