#!/usr/bin/python3
"""Module defines weighted_average"""


def weight_average(my_list=[]):
    """Calculates the weighted average of a list of integer tuples
    Args:
        my_list: List of integer tuples (<score>, <weight>)
    Return: The computed value
    """
    if len(my_list) == 0:
        return 0

    total_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_sum += score * weight
        total_weight += weight

    return total_sum / total_weight
