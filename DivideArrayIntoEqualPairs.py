"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:
    - Each element belongs to exactly one pair.
    - The elements present in a pair are equal.

Return true if nums can be divided into n pairs, otherwise return false.
"""

from collections import defaultdict

class DivideArrayIntoEqualPairs(object):
    def divideArray(self, nums):
        counts = defaultdict(lambda: 0)
        for i in nums:
            counts[i] += 1
        for i in nums:
            if counts[i] % 2 == 1:
                return False
        return True
        