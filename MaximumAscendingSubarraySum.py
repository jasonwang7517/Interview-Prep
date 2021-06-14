"""
    Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

    A subarray is defined as a contiguous sequence of numbers in an array.

    A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.
"""

class MaximumAscendingSubarraySum(object):
    def maxAscendingSum(self, nums):
        maximum = nums[0]
        currVal = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                currVal += nums[i]
            else:
                if currVal > maximum:
                    maximum = currVal
                currVal = nums[i]
        return max(currVal, maximum)
        