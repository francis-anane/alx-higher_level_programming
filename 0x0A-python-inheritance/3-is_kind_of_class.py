#!/usr/bin/python3
""" 3-is_kind_of_class module for checif object is an instance of
either the child or parent class
"""


def is_kind_of_class(obj, a_class):
    """ Checks a class object instance.
    Args:
        obj: The object to check
        a_class: The class to check if the object is an instance of
    Return: True if obj is an instance of a_class, else False
    """
    return isinstance(obj, a_class)
