#!/usr/bin/python3
"""The module for dividing matrix"""
def matrix_divided(matrix, div):
    """divides every menber of the matrix
    Args:
        matrix: The list of list that forms the matrix
        div: the number used to divide the member of the matrix
    Raises:
        TypeError: If matrix is not a list of int or float
        TypeError: If row in matrix is not thesame size
        Typeerror: If div is not an integer or a float
        ZeroDivisionError: If div is 0
    Return:
        return a new matrix(dividend of matrix and div)
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
