#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    """ This function returns a set of all elements present in only one set.
    """
    try:
        dif_set = set(set_1 ^ set_2)
        return dif_set
    except TypeError:
        print("Arguments parsed is not a set")
