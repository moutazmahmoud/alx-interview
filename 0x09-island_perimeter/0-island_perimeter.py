#!/usr/bin/python3
"""Module for Island Perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): 2D grid representing the island and water.

    Returns:
        int: The perimeter of the island.
    """
    # Determine the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the perimeter variable to 0
    perimeter = 0

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # bottom edge
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # right edge
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    # Return the total perimeter
    return perimeter
