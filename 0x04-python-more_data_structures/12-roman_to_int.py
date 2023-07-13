#!/usr/bin/python3
"""This modules defines roman_to_int"""


def roman_to_int(roman_string):

    """Converts a roman numeral to an integer
    Args:
        roman_string: The string to convert
    Return: The converted value
    """
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0

    for char in roman_string:
        value = roman_dict.get(char, 0)

        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value

        prev_value = value

    return result
