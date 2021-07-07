"""
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

class PascalsTriangle(object):
    def generate(self, numRows):
        triangle = [[1]]
        for i in range(1, numRows):
            newRow = [0 for j in range(0, i + 1)]
            newRow[0] = 1
            newRow[-1] = 1
            for k in range(1, len(newRow) - 1):
                newRow[k] = triangle[i - 1][k] + triangle[i - 1][k - 1]
            triangle.append(newRow)
        return triangle
        