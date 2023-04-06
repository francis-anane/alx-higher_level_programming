#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """ This function replaces an element in list at a specified index """

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
