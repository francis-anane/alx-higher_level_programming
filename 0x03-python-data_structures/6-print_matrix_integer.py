#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    """ This function prints a matrix of integers. """

    for mat in matrix:
        idx = 0
        for i in mat:
            if idx < len(mat) - 1:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
            idx += 1
        print()
