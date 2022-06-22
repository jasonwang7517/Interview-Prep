"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the 
staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""

class ArrangingCoins(object):
    def arrangeCoins(self, n):
        next_val = 2
        columns = 1
        cumulative = 1
        while cumulative < n:
            cumulative += next_val
            next_val += 1
            columns += 1
        if cumulative == n:
            return columns
        return columns - 1
        