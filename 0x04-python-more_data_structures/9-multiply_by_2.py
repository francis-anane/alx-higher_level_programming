#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """ This function returns a new dictionary with all values multiplied by 2
    """

    dic_keys = a_dictionary.keys()
    new_dic = {}
    for k in dic_keys:
        d = {k: a_dictionary[k] * 2}
        new_dic.update(d)
    return new_dic
