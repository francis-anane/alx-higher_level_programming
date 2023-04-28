#!/usr/bin/python3

"""4-from_json_string module to deserialize an object"""

import json


def from_json_string(my_str):
    """returns an object  (Python data structure) represented by a JSON string
    Args:
        my_str: the json string to decode
    Return: decoded object
    """

    return json.loads(my_str)
