#!/usr/bin/python3
"""module defines remove_char_at"""

def remove_char_at(str, n):
    """Makes a copy of a string by removing character at index n.
    Attribute:
        str: The string to copy from
        n (int): Index to ignore
    """
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
