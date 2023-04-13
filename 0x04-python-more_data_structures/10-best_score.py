#!/usr/bin/python3

def best_score(a_dictionary):
    """ This function returns a key with the biggest integer value.
    """

    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    dic_keys = list(a_dictionary)
    h_score = dic_keys[0]
    for k in dic_keys:
        if a_dictionary[k] > a_dictionary[h_score]:
            h_score = k
    return h_score
