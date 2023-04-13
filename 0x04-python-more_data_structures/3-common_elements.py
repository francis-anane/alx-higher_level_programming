#!/usr/bin/python3

def common_elements(set_1, set_2):

    """ This function returns a set of common elements in two sets.
    """
    try:
        cmn_set = set(set_1&set_2)
        return cmn_set
    except TypeError:
        print("Arguments parsed is not a set")
