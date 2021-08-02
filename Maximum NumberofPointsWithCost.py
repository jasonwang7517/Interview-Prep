"""
  You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

  To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

  However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

  Return the maximum number of points you can achieve.

  abs(x) is defined as:
  - x for x >= 0.
  - (-x) for x < 0.

"""

class MaximumNumberOfPointsWithCost(object):
    def maxPoints(self, points):
        currRow = points[0]
        for i in range(1, len(points)):
            currRow = self.compRows(currRow, points[i])
        return max(currRow)
                
    def compRows(self, row1, row2):
        left = [0 for i in range(0, len(row1))]
        left[0] = row1[0]
        for i in range(1, len(left)):
            left[i] = max(left[i - 1] - 1, row1[i])
        right = [0 for i in range(0, len(row1))]
        right[-1] = row1[-1]
        for i in range(len(right) - 2, -1, -1):
            right[i] = max(right[i + 1] - 1, row1[i])
        ans = [0 for i in range(0, len(row1))]
        for i in range(0, len(row2)):
            ans[i] = max(left[i], right[i]) + row2[i]
        return ans
