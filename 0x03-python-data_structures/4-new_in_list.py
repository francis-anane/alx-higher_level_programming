#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ This function inserts an element a copy of a list """

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list_cp = []
        for i in my_list:
            my_list_cp.append(i)
        my_list_cp[idx] = element
        return my_list_cp
