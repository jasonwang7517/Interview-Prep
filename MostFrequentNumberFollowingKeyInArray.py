"""
You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:

    - 0 <= i <= nums.length - 2,
    - nums[i] == key and,
    - nums[i + 1] == target.

Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.
"""

from collections import defaultdict

class Solution(object):
    def mostFrequent(self, nums, key):
        counts = defaultdict(lambda: 0)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                counts[nums[i + 1]] += 1
        return max(counts, key=counts.get)
                
        