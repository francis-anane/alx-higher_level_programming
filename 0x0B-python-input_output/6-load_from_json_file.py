#!/usr/bin/python3

"""6-load_from_json_file module to create an object from a file"""

import json


def load_from_json_file(filename):
    """creates an Object from a JSON file
    Args:
        filename: The file to create object from
    Return: The object
    """

    with open(filename, "r") as a_file:
        return json.load(a_file)
