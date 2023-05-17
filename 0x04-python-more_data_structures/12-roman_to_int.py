#!/usr/bin/python3
def roman_to_int(roman_string):
    """" converts a Roman numeral to an integer. """
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        "M": 1000,
        "C": 100,
        "D": 500,
        "X": 10,
        "L": 50,
        "I": 1,
        "V": 5
    }

    sum = 0
    for i in range(len(roman_string) - 1):
        if roman_numerals[roman_string[i]] < roman_numerals[roman_string[i+1]]:
            sum -= roman_numerals[roman_string[i]]
        else:
            sum += roman_numerals[roman_string[i]]
    sum += roman_numerals[roman_string[-1]]
    return sum
