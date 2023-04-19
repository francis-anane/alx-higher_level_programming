#!/usr/bin/python3

""" 2-matrix_divided module for a matrix division.
"""


def matrix_divided(matrix, div):
    """ Divides the elements of a matrix

    Args:
        matrix (list): A list of lists of integers/floats
        div (int/float): The divisor
    Raises:
          TypeError: If matrix is not a list of lists of integers or floats.
                   If the rows of matrix differ in size.
                   If div is not a number
          ZeroDivisionError: If div is 0
    Returns:
        list: list of lists of the division.
    """

    # type_error messages for matrix data type
    type_err = "matrix must be a matrix(list of lists) of integers/floats"
    type_err2 = "Each row of the matrix must have the same size"
    if type(matrix) != list:
        raise TypeError(type_err)
    elif type(matrix[0]) != list:
        raise TypeError(type_err)
    elif type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []  # holds division result
        len_0 = len(matrix[0])  # To check elements length
        for m in matrix:
            if type(m) != list:
                raise TypeError(type_err)
            elif len(m) != len_0:
                raise TypeError(type_err2)
            else:
                element = []
                for e in m:
                    if type(e) in [int, float]:
                        element.append(round(e / div, 2))
                    else:
                        raise TypeError(type_err)
            new_matrix.append(element)

        return new_matrix
