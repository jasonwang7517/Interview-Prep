"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:
    - x if x >= 0.
    - -x if x < 0.
 
"""

class CountNumberOfPairsWithAbsoluteDifference(object):
    def countKDifference(self, nums, k):
        pairs = 0
        elements = {}
        for i in nums:
            target_up = i + k
            target_down = i - k
            if target_up in elements:
                pairs += elements[target_up]
            if target_down in elements:
                pairs += elements[target_down]
            if i in elements:
                elements[i] += 1
            else:
                elements[i] = 1
        return pairs