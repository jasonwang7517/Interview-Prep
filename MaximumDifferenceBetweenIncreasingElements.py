"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""

class MaxDifferenceBetweenIncreasingElements(object):
    def maximumDifference(self, nums):
        ans = -1
        current_minimum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < current_minimum:
                current_minimum = nums[i]
            elif nums[i] - current_minimum > 0 and nums[i] - current_minimum > ans:
                ans = nums[i] - current_minimum
        return ans