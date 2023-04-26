#!/usr/bin/python3
"""2-is_same_class module for checking a object intance of a class """


def is_same_class(obj, a_class):
    """Checks a class object instance.
    Args:
        obj: The object to check
        a_class: The class to check if the object is an instance of
    Return: True if obj is an instance of a_class, else False
    """

    return type(obj) == a_class
