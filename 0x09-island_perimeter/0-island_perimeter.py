#!/usr/bin/python3
"""
This module provides a function to calculate the perimeter
    of an island in a given 2D grid.
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    height = len(grid)
    width = len(grid[0])
    size = 0
    edges = 0
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                size += 1
                if row > 0 and grid[row - 1][col]:
                    edges += 1
                if col > 0 and grid[row][col - 1]:
                    edges += 1
    return size * 4 - edges * 2
