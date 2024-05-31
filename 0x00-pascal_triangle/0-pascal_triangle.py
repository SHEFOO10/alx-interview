#!/usr/bin/python3

def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for row in range(1, n):
        previous_row = triangle[-1]
        new_row = [1]
        for i in range(1, row):
            new_row.append(previous_row[i - 1] + previous_row[i])
        new_row.append(1)
        triangle.append(new_row)

    return triangle