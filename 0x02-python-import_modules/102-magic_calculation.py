#!/usr/bin/python3
"""This module defines magic_calculation"""


def magic_calculation(a, b):
    """Imitates the behaviour of a given byte code instructions"""

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
