#!/usr/bin/python3
'''2D matrix'''


def rotate_2d_matrix(matrix):
    """This function first transposes the matrix by swapping elements
    across its main diagonal and then reverses each row to achieve
    the 90-degree clockwise rotation.
    n = len(matrix)
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for row in matrix:
        row.reverse()
