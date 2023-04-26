#!/usr/bin/python3

""" 0-lookup module for looking an object.
"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object

    Args:
        obj : The object to lookup
    Returns:
        list: A list of object attributes and methods
    """
    return dir(obj)
