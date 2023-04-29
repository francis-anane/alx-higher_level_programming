#!/usr/bin/python3

""" 12-pascal_triangle module """


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle
    Args:
        n (int): size of the triangle
    Return: The triangle
    """
    if n <= 0:
        return []
    triangle = [[1], [1, 1]]  # first two rows of triangle list
    idx = 1
    while len(triangle) < n:
        i = 0
        lst = []  # creates a row to add
        # Add rows and columns up to the size of n
        while i < len(triangle[idx]) - 1:
            lst.append(triangle[idx][i] + triangle[idx][i+1])
            i += 1
        lst.insert(0, 1)
        lst.append(1)
        triangle.append(lst)
        idx += 1

    return triangle
