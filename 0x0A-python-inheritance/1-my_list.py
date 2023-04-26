#!/usr/bin/python3

""" 1-my_list module for defining a list
"""


class MyList(list):
    """ Defines a list
    """

    def print_sorted(self):
        """ Print a list, sorted """

        print(sorted(self))
