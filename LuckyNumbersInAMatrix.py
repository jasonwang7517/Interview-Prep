"""
    Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

    A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
"""

class LuckyNumbersInAMatrix(object):
    def luckyNumbers (self, matrix):
        ans = []
        rowMin = {}
        colMax = {}
        for i in range(0, len(matrix)):
            rowMin[i] = 100001
        for i in range (0, len(matrix[0])):
            colMax[i] = 0
        for i in range(0, len(matrix)):
            for j in range (0, len(matrix[i])):
                currentElement = matrix[i][j]
                if currentElement > colMax[j]:
                    colMax[j] = currentElement
                if currentElement < rowMin[i]:
                    rowMin[i] = currentElement
        for i in range(0, len(matrix)):
            for j in range (0, len(matrix[i])):
                if rowMin[i] == colMax[j]:
                    ans.append(rowMin[i])
        return ans