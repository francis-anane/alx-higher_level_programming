#!/usr/bin/python3

""" 4-inherits_from module for checking object is an instance of
a child class, directly or indirectly
"""


def inherits_from(obj, a_class):
    """ Checks a class object instance
    Args:
        obj: The object to check
        a_class: The class to check if the object is
        an instance of directly or indirectly.
    Return: True if obj is an instance of a_class, else False
    """

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
