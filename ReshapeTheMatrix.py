"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""

class ReshapeTheMatrix(object):
    def matrixReshape(self, nums, r, c):
        if (len(nums) * len(nums[0])) != (r * c):
            return nums
        newMatrix = [[0 for i in range(c)] for j in range (r)]
        values = []
        for i in nums:
            for j in i:
                values.append(j)
        index = 0
        for i in range(0, r):
            for j in range(0, c):
                newMatrix[i][j] = values[index]
                index += 1
        return newMatrix