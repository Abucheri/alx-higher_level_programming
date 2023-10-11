#!/usr/bin/python3

"""Definition for pascal_triangle function."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] if i == 0 else [1, 1]
        if i > 1:
            for j in range(1, i):
                row.insert(j, triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
