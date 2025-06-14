# Pascal's Triangle Generator

## Overview
This project contains a Python script that generates Pascal's Triangle for a given number of rows `n`. The script is implemented in the file `0x00-pascal_triangle.py`.

## Files
- **0-pascal_triangle.py**: Contains the `pascal_triangle(n)` function that returns a list of lists representing Pascal's Triangle of `n` rows.

## Function Description
### `pascal_triangle(n)`
- **Input**: An integer `n` representing the number of rows for Pascal's Triangle.
- **Output**: A list of lists of integers representing Pascal's Triangle.
- **Behavior**:
  - If `n <= 0`, returns an empty list `[]`.
  - For `n > 0`, generates Pascal's Triangle where each row is calculated based on the sum of the two numbers directly above it from the previous row.
  - The first and last element of each row is always `1`.

## Example Usage
```python
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

# Generate Pascal's Triangle for n = 5
triangle = pascal_triangle(5)
for row in triangle:
    print(row)

# Output:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
```

## Installation
1. Ensure you have Python 3 installed on your system.
2. Clone or download this repository.
3. Navigate to the project directory containing `0x00-pascal_triangle.py`.

## Running the Script
You can use the function by importing it into your Python script or interactive session:
```bash
python3
>>> from 0x00-pascal_triangle import pascal_triangle
>>> pascal_triangle(3)
[[1], [1, 1], [1, 2, 1]]
```

## Requirements
- Python 3.x
- No external dependencies are required.

## Author
SHEFOO10

## License
This project is licensed under the MIT License.


