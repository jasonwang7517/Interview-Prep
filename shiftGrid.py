class Solution(object):
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