"""
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, 
return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. 
For example, the two 1's in "1001" have a distance of 3.
"""

class BinaryGap(object):
    def binaryGap(self, n):
        A = [i for i in range(32) if (n >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i+1] - A[i] for i in range(len(A) - 1))