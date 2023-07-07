#!/usr/bin/python3
"""Module defines magic_calculation"""

def magic_calculation(a, b, c):
    """Imitates the behaviour of a bytecode
    """
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
