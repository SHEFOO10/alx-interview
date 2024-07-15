#!/usr/bin/python3
""" Rotate by 90 degrees """


def rotate_2d_matrix(matrix):
    """ rotates 2d matrix
    Actually can rotate any square matrix
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
