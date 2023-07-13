#!/usr/bin/python3
"""Module defines safe_print_integer_err"""
import sys


def safe_print_integer_err(value):
    """Prints an integer
    Args:
        value (int): The integer to print.
    Returns: True, or False (TypeError or ValueError)
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
