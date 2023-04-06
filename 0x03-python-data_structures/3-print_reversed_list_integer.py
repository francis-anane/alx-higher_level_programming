#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    """ This function prints a list of integers in reverse order. """

    idx = len(my_list) - 1
    if idx < 0:
        return None
    while idx >= 0:
        print("{:d}".format(my_list[idx]))
        idx = idx - 1
