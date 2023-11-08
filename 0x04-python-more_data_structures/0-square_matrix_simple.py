#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        squared = [a ** 2 for a in row]
        new_matrix.append(squared)
    return new_matrix
