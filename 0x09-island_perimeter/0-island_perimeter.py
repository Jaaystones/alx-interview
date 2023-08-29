#!/usr/bin/python3
'''0x09. Island Perimeter'''


def is_valid_position(row, col, grid):
    '''Check if the given row and column are within valid bounds'''
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                neighbors = [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1)
                ]
                land_neighbors = sum(
                    1 for r, c in neighbors if is_valid_position(r, c, grid)  and grid[r][c] == 1
                )
                perimeter += 4 - land_neighbors

    return perimeter
