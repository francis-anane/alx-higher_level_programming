#!/usr/bin/python3
"""Module defines safe_function"""
from __future__ import print_function
import sys


def safe_function(fct, *args):
    """ Executes a function safely
    Args:
        fct: The function to execute
        agrs: arguments to the function to execute
    """
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
