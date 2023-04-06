#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    """ This function prints a matrix of integers. """

    for l in matrix:
        idx = 0
        for i in l:
            if idx < len(l) - 1:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
            idx += 1
        print()
