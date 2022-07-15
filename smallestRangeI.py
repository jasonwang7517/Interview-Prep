"""
Given an array nums of integers, for each integer nums[i] we may choose any x with -k <= x <= k, and add x to nums[i].

After this process, we have some array result.

Return the smallest possible difference between the maximum value of result and the minimum value of result.
"""

class SmallestRangeI(object):
    def smallestRangeI(self, A, K):
        return max(0, max(A) - min(A) - 2*K)