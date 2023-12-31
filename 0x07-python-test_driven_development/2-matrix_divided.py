#!/usr/bin/python3

"""This module defines the matrix_divided function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a specified divisor.

    Args:
        matrix (list of lists): The matrix.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix isn't a list of lists if integers/floats.
        TypeError: If div is not a number.
        TypeError: If the matrix contains rows of different sizes.
        ZeroDivisionError: If div is equal to zero.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return result_matrix
