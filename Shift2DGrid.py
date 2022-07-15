"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:
    - Element at grid[i][j] moves to grid[i][j + 1].
    - Element at grid[i][n - 1] moves to grid[i + 1][0].
    - Element at grid[m - 1][n - 1] moves to grid[0][0].
    
Return the 2D grid after applying shift operation k times.
"""

class Shift2DGrid(object):
    def shiftGrid(self, grid, k):
        elements = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                elements.append(grid[i][j])
        iterations = k % (len(grid) * len(grid[0]))
        startRow = iterations / len(grid[0])
        startCol = iterations % len(grid[0])
        for j in range(startCol, len(grid[0])):
            grid[startRow][j] = elements.pop(0)
        for i in range(startRow + 1, len(grid)):
            for j in range(0, len(grid[0])):
                grid[i][j] = elements.pop(0)
        for i in range(0, startRow):
            for j in range(0, len(grid[0])):
                grid[i][j] = elements.pop(0)
        for i in range(0, startCol):
            grid[startRow][i] = elements.pop(0)
        return grid