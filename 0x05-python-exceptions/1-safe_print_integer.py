#!/usr/bin/python3
def safe_print_integer(value):
    """ This function prints an integer with "{:d}".format(). """

    try:
        print("{:d}".format(value))
        return True

    except ValueError:
        return False
