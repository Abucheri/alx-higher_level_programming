#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newM = []
    for r in matrix:
        newR = []
        for elm in r:
            newR.append(elm ** 2)
        newM.append(newR)
    return newM
