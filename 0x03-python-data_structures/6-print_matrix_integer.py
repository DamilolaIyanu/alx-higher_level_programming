#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        if len(row) == 0:
            print()
        for num in range(len(row)):
            print("{:d}".format(row[num]), end="\n"
                  if num is len(row) - 1 else " ")
