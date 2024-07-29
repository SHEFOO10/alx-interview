# Island Perimeter

This module contains a function to solve the Island Perimeter problem from LeetCode. The problem is described as follows:

You are given a 2D grid of integers, where:
- '0' represents water,
- '1' represents land.

The grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The function provided in this module calculates the perimeter of the island.

## Function

### `island_perimeter(grid: List[List[int]]) -> int`

#### Parameters:
- `grid` (`List[List[int]]`): A 2D list of integers representing the grid.

#### Returns:
- `int`: The perimeter of the island.

#### Example:
```python
>>> grid = [
...     [0, 1, 0, 0],
...     [1, 1, 1, 0],
...     [0, 1, 0, 0],
...     [1, 1, 0, 0]
... ]
>>> island_perimeter(grid)
16
