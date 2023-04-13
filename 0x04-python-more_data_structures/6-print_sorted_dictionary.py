#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ This function prints a dictionary by ordered keys.
    """

    sorted_dic = sorted(a_dictionary)

    for k in sorted_dic:
        print(f"{k}: {a_dictionary[k]}")
