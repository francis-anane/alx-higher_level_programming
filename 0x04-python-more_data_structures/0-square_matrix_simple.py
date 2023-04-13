#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ This function computes the square value of all integers of
    a matrix.
    """
    try:
        mat = [[(x*x) for x in matrix[i]] for i in range(0, len(matrix))]
        return mat
    except TypeError:
        print("Argument parsed is not a matrix")
