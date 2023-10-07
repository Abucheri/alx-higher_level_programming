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
    is_matrix_list = isinstance(matrix, list)
    is_matrix_valid = all(isinstance(row, list) for row in matrix)
    is_elements_valid = all((isinstance(num, (int, float))
                            for row in matrix for num in row))
    if not (is_matrix_list and is_matrix_valid and is_elements_valid):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return result_matrix
