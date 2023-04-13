#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """ This function replaces or adds key/value in a dictionary.
    """

    d = {key: value}
    a_dictionary.update(d)
    return a_dictionary
