#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """ This function deletes a key in a dictionary.
    """

    dic_keys = a_dictionary.keys()
    if key in dic_keys:
        a_dictionary.pop(key)
    return a_dictionary
