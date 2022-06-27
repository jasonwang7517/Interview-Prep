"""
A square matrix is said to be an X-Matrix if both of the following conditions hold:
    - All the elements in the diagonals of the matrix are non-zero.
    - All other elements are 0.

Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.
"""

class Solution(object):
    def checkXMatrix(self, grid):
        index = 0
        bound = len(grid[0]) - 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == index or j == bound - index:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False
            index += 1
        return True