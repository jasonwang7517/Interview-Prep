"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
"""

from collections import defaultdict

class LargestHarmoniousSubsequence(object):
    def findLHS(self, nums):
        counts = defaultdict(lambda: 0)
        for i in nums:
            counts[i] += 1
        curr_max = 0
        for i in counts:
            curr_length = max(counts.get(i - 1), counts.get(i + 1))
            if curr_length is None:
                continue
            curr_max = max(curr_max, counts[i] + curr_length)
        return curr_max
            