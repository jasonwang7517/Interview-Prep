"""
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.
"""

class RangeAdditionII(object):
    def maxCount(self, m, n, ops):
        if len(ops) == 0:
            return m * n
        return min(op[0] for op in ops) * min(op[1] for op in ops)