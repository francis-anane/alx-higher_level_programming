#!/usr/bin/python3
"""Module defines complex_delete"""


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary.
    Args:
        a_dictionary: The dictionary to lookup
        value: The value to search for
    """
    keys = list(a_dictionary.keys())

    for key in keys:
        if value == a_dictionary.get(key):
            del a_dictionary[key]

    return (a_dictionary)
