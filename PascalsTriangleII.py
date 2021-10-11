"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

class PascalsTriangleII(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1 for i in range(1)]
        current_index = 1
        last_row = [1 for i in range(2)]
        while current_index <= rowIndex:
            current_row = [1 for i in range(current_index + 1)]
            for i in range(1, len(current_row) - 1):
                current_row[i] = last_row[i - 1] + last_row[i]
            current_index += 1
            last_row = current_row
        return last_row
        