#!/usr/bin/python3

"""3-to_json_string module to serialize an object"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object
    Args:
        my_obj: the object to encode
    Return 1(str): Encoded object
    """

    return json.dumps(my_obj, sort_keys=True)
