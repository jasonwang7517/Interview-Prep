"""
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
"""

class SpecialPositionsInABinaryMatrix(object):
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        row, col = [0]*m, [0]*n
        for i, j in product(range(m), range(n)): 
            if mat[i][j]: row[i], col[j] = 1 + row[i], 1 + col[j]
        return sum(mat[i][j] and row[i] == 1 and col[j] == 1 for i, j in product(range(m), range(n)))