#!/usr/bin/python3
"""function that converts a Roman numeral to an integer."""
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_in = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_nu = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_in[roman_string[i]] > roman_in[roman_string][i - 1]:
            roman_nu += roman_in[roman_string[i]] - 2 * \
        else:
            roman_in += roman_in[roman_string[i]]
    return roman_nu
