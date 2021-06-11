"""
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

class CountingBits(object):
    def countBits(self, n):
        ans = []
        for i in range(0, n + 1):
            binRep = bin(i)[2:]
            total = 0
            for j in binRep:
                total += int(j)
            ans.append(total)
        return ans
        