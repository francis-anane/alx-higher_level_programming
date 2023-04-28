#!/usr/bin/python3

"""5-save_to_json_file module to write json representation"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj: the object to write
        filename: The file to write to
    """

    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)
