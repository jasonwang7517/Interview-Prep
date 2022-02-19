"""
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
"""

class CheckIfEveryRowAndColumnContainsAllNumbers(object):
    def checkValid(self, matrix):
        length = len(matrix)
        for row in matrix:
            s = set(row)
            for i in range(1, length + 1):
                if i not in s:
                    return False
        for i in range(length):
            col = set()
            for j in range(length):
                col.add(matrix[j][i])
            for k in range(1, length + 1):
                if k not in col:
                    return False
        return True
                          
                 