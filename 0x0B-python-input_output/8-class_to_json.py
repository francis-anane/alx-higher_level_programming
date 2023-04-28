#!/usr/bin/python3

"""8-class_to_json module to create json serializable object from a class """


def class_to_json(obj):
    """returns a json serializable object
    Args:
        obj: A class instance to get the serializable object
    Return: The json serializable object
    """

    return obj.__dict__
