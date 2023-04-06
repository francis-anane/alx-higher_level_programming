#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    """ This function prints a list of integers in reverse order. """

    if my_list == None:
        return None
    idx = len(my_list) - 1
    while idx >= 0:
        print("{:d}".format(my_list[idx]))
        idx = idx - 1
