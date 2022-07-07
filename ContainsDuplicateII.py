"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from collections import defaultdict

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        positions = defaultdict(lambda: [])
        for i in range(len(nums)):
            positions[nums[i]].append(i)
            if len(positions[nums[i]]) >= 2:
                current = positions[nums[i]]
                if current[-1] - current[-2] <= k:
                    return True
        return False