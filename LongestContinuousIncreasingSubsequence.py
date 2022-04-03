"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        if len(nums) == 1:
            return 1
        ans = 0
        index = 1
        current_sequence = 1
        while index < len(nums) - 1:
            if nums[index] > nums[index - 1]:
                current_sequence += 1
            else:
                ans = max(ans, current_sequence)
                current_sequence = 1
            index += 1
        if nums[-1] > nums[-2]:
            current_sequence += 1
        return max(ans, current_sequence)
        