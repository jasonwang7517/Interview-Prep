"""
    Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""

class ToeplitzMatrix(object):
    def isToeplitzMatrix(self, matrix):
        for i in range(0, len(matrix) - 1):
            for j in range(0, len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
